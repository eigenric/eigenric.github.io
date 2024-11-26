Title: Advent of Code en Rust y un poco de Probabilidad 
Date: 2021-10-09 
Tags: Rust, Advent of Code, Probabilidad, Matemáticas, Programación

El problema [**Report Repair**](https://adventofcode.com/2020/day/1){target=_blank} del primer día del Advent of Code 2020 nos plantea un desafío interesante: encontrar dos números en una lista que sumen exactamente 2020 y luego multiplicarlos. Aunque este problema puede resolverse utilizando algoritmos simples, también ofrece una oportunidad única para explorar las matemáticas detrás de este tipo de problemas, especialmente desde la perspectiva de la probabilidad.

En este artículo, resolveremos el problema utilizando el lenguaje de programación **Rust** y lo analizaremos desde un enfoque probabilístico. 

## El Problema

El enunciado del problema es el siguiente:

> Se te proporciona una lista de números, y tu tarea es encontrar dos números en la lista cuya suma sea exactamente 2020, y luego multiplicar esos dos números. Además, se te pedirá encontrar tres números que sumen 2020 y multiplicarlos.

Por ejemplo, si la lista contiene los siguientes números:

```
[1721, 979, 366, 299, 675, 1456]
```

Los dos números que suman $2020$ son $1721$ y $299$ y al multiplicarlos obtenemos $1721 \cdot 299 = 514579$

## Resolución en Rust

```rust
use itertools::Itertools;
use crate::utils;

pub fn exercise1() {
    // Cargar los valores de entrada como una lista de enteros
    let expenses: Vec<i64> = utils::loadints_from_file("input/day1");

    // Encontrar las combinaciones de dos números cuya suma sea 2020
    let found = expenses.into_iter()
        // Generar todas las combinaciones de 2 números
            .combinations(2) 
        // Filtrar aquellas cuya suma es 2020
            .filter(|v| v[0] + v[1] == 2020) 
        // Asegurar que solo hay una combinación que cumple
            .exactly_one()  
        // Desempaquetar el resultado
            .unwrap();

    // Calcular el producto de los dos números
    let product = found[0] * found[1];

    // Imprimir el resultado
    println!("{} * {} = {}", found[0], found[1], product);
}
```

En este código, utilizamos la biblioteca `itertools` para generar todas las combinaciones posibles de dos números en la lista de gastos y luego filtramos aquellas cuya suma sea exactamente 2020. Finalmente, calculamos el producto de los dos números encontrados y lo imprimimos en la consola.

## Análisis Probabilístico

No obstante, podríamos preguntarnos que probabilidad hay de que existan dos números en la lista que sumen exactamente 2020. Para responder a esta pregunta, podemos utilizar un enfoque probabilístico.

### Distribución Uniforme Discreta

Supongamos que los números de la lista se generan de manera aleatoria siguiendo una **distribución uniforme discreta**. En una distribución uniforme, cada número tiene la misma probabilidad de ser seleccionado de un rango determinado. Si el rango de valores es de $0$ a $200.000$, la probabilidad de que un número $X_i$ específico sea igual a $x$ es:

$$
P[X=x] = \frac{1}{200000}
$$

### Suma de Dos Variables Aleatorias Uniformes

El siguiente paso es calcular la probabilidad de que dos números $X$ y $Y$ de esta lista sumen exactamente $2020$. La probabilidad de que $X + Y = 2020$ es extremadamente baja debido al gran rango de valores posibles ($0$ a $200.000$).

Debido a que estamos trabajando con dos distribuciones uniforme discreta, la probabilidad de que $X + Y$ sigue una distribución triangular. 

$$
P[X + Y = 2020] = \frac{2020+1}{(200000+1)^2} \approx 5.05 \times 10^{-8}
$$

Así, **¿qué cantidad de números debemos generar como mínimo para esperar encontrar al menos un par que sume 2020?**

### Valor Esperado

El **valor esperado** del número de pares que suman $2020$ se calcula multiplicando el número de combinaciones posibles por la probabilidad de éxito de cada combinación:

Si queremos encontrar dos números que sumen $2020$ en una lista de $N$ números, el valor esperado de pares que suman $2020$ debe ser igual a 1

$$
E[X+Y] = \binom{n}{2} \cdot \frac{2021}{200,001^2} = \frac{n(n-1)}{2} \cdot \frac{2021}{200,001^2} = 1
$$

### Resolución para $n$

Reorganizando la ecuación para resolver $n$:

$$
\frac{n(n-1)}{2} = \frac{200,001^2}{2021}
$$

$$
n(n-1) = \frac{2 \cdot 200,001^2}{2021}
$$

Resolviendo la ecuación cuadrática y redondeando, obtenemos $n = 6808$. Por lo tanto, si generamos al menos $6808$ números aleatorios en el rango de $0$ a $200,000$, podemos esperar encontrar al menos un par que sume $2020$.
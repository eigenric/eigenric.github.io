Title: Rvalues y Lvalues en C++11
Date: 2018-11-19
Tags: 

En este artículo, exploramos el manejo de rvalues y lvalues en C++11, desentrañando un error común de compilación y ofreciendo una solución para corregirlo.

En particular, nos encontramos con el siguiente error de compilación:

```c++
template <class T>
T& Stackl<T>::pop() {
    return lista.pop_front();
}
```

```
./include/stackl.cpp:6:28: error: invalid initialization 
of non-const reference of type 'int&' from an rvalue of 
type 'void'
```

Este error se produce porque `lista.pop_front()` retorna un rvalue, lo que implica que no es posible inicializar una referencia no constante (en este caso, `int&`) con un rvalue de tipo `void`.

Es importante comprender que en C++, cada expresión se clasifica como lvalue o rvalue:

- **Lvalues** son aquellos objetos que persisten más allá de la expresión en la que se utilizan. Ejemplos de lvalues incluyen variables nombradas (`obj`), el resultado de la desreferenciación de un puntero (`*ptr`), el acceso a elementos de un arreglo (`ptr[index]`), y el incremento de una variable (`++x`).

- **Rvalues**, por otro lado, son temporales que no persisten después de la expresión actual. Algunos ejemplos son literales numéricos (`1729`), el resultado de una operación aritmética (`x+y`), la creación de un objeto temporal (`std::string("now")`), y el incremento de una variable en una expresión (`x++`).

Para poder utilizar el operador de dirección (`&`), es necesario que el objeto en cuestión sea un lvalue. De lo contrario, estamos tratando con un rvalue.

Con la introducción de C++11, se añadió el concepto de referencia a rvalue (`&&`), lo que permite una manipulación más eficiente de los rvalues y habilita la optimización de la semántica de movimiento, entre otras características avanzadas de este lenguaje.

Para corregir el error en el código, habría que modificar el método `pop()` para que no intente devolver un valor de un método que devuelve `void`. Una solución sería cambiar el diseño de `pop()` para que simplemente ejecute `pop_front()` sin intentar devolver un valor. Si quisiera devolver el valor que está siendo eliminado, habría que almacenar temporalmente el valor antes de eliminarlo y luego devolver ese valor:

```c++
template <class T>
T Stack<T>::pop() {
    if (lista.empty()) {
        throw std::out_of_range("Stack underflow");
    } 
    // Almacena temporalmente el valor a devolver
    T valor = lista.front();

    // Elimina el elemento del frente de la lista
    lista.pop_front();

    // Devuelve el valor almacenado
    return valor; 
}
```

Este enfoque asume que `lista` es una estructura de datos que permite acceso al primer elemento (`front()`) y que tiene un método para eliminar el primer elemento (`pop_front()`), pero que `pop_front()` no devuelve el elemento eliminado. También se añade una comprobación para asegurar que la lista no esté vacía antes de intentar eliminar un elemento, lanzando una excepción si se intenta hacer `pop()` en una lista vacía.

## Más en información en:

- [Hardfloat Blog - Ralues y Lvalues](https://hardfloat.es/blog/2021/02/08/entendiendo-rvalues-y-lvalues.html){:target=_blank}
- [Stackoverflow - Diferencias entre rvalues y lvalue](https://es.stackoverflow.com/questions/914/diferencias-entre-rvalue-y-lvalue){:target=_blank}
- [IBM - Lvalues y Rvalues](https://www.ibm.com/docs/es/i/7.5?topic=operators-lvalues-rvalues){:target=_blank}
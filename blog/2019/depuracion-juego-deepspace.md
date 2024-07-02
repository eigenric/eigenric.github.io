Title: Depuración juego Deepspace - PDOO
Date: 2019-03-23
Tags: deepspace, pdoo, ruby

La Programación Orientada a Objetos (POO) es un paradigma de programación que utiliza "objetos" para representar datos y métodos. Estos objetos son instancias de clases, que definen las propiedades y comportamientos de los objetos. La POO facilita la modularidad, la reutilización de código y la abstracción, permitiendo a los desarrolladores crear sistemas complejos de manera más manejable.

## Práctica Deepspace: Desarrollo de la clase `SpaceStation`

Nos encontramos en el desarrollo del juego **Deepspace**, específicamente trabajando en la práctica para el examen de la asignatura de Programación Orientada a Objetos (PDOO). Actualmente, estamos enfocados en el constructor de la clase `SpaceStation`.

### Constructor de `SpaceStation`

Inicialmente, nos sorprendió que el constructor de `SpaceStation` tomara únicamente un nombre y un objeto `SuppliesPackage`, a pesar de que la clase parece tener muchos más atributos. Ahora comprendemos que el objeto `SuppliesPackage` incluye todos los suministros necesarios (`ammoPower`, `fuelUnits`, `shieldPower`).

Sin embargo, aún nos falta determinar cómo obtener el atributo `nMedals`. Hemos identificado que este atributo aparece en la clase `Loot`, pero `SpaceStation` no parece tener dependencias directas de esta clase.

### Dependencias y Atributos Iniciales

Otra cuestión es la implementación de las dependencias con multiplicidad 0..1. Suponemos que, a priori, dichos atributos se inicializan con `nil` hasta que se indique lo contrario.

### Método `adjust` en la Clase `Damage`

El método `adjust` es una fuente de confusión, así que vamos a desglosarlo y entender su funcionalidad.

La clase `Damage` puede estar compuesta de dos maneras:

1. Una lista de `weaponTypes`, un número de `shields` y un número de armas (>= -1).
2. Un número de `weapons` y un número de `shields`, donde `weapons == []`.

El método `adjust` toma una lista de `Weapon` y una lista de `ShieldBoosters`. Devuelve una copia del objeto `Damage` modificado, ajustado según las colecciones de armas y potenciadores de escudos proporcionados como parámetros.

### Ajuste de `Damage`

El objetivo del ajuste es que la instancia de `Damage` resultante no pueda implicar la pérdida de más armas o escudos de los que realmente se tienen. En otras palabras, los atributos de `Damage` deben coincidir con los tipos y cantidades presentes en las colecciones de los parámetros.

### Pasos para implementar `adjust`


- **Para armas (`weaponTypes`):**

   * Comparar la lista de tipos de armas actuales con la lista proporcionada.
   * Crear una lista con los tipos de armas que están tanto en el objeto `Damage` como en la lista de parámetros.
   * La nueva lista será la diferencia entre los tipos de armas actuales y los tipos suministrados.

- **Para escudos (`ShieldBoosters`):**

   - No hay un atributo de lista de `shieldBoosters`, por lo que trabajamos con `nShields`.
   - `nShields` debe ser ajustado a la longitud de la lista de `ShieldBoosters` proporcionada como parámetro, si es menor.

### Ejemplo

Supongamos que `Damage` tiene 3 tipos de armas y 2 escudos:
- `Damage.weaponTypes = ["laser", "missile", "plasma"]`
- `Damage.nShields = 2`

Y se llama al método `adjust` con:
- `weapons = ["laser", "ion"]`
- `shieldBoosters = ["basic", "advanced"]`

El resultado ajustado será:
- `Damage.weaponTypes = ["laser"]` (ya que "missile" y "plasma" no están en los parámetros)
- `Damage.nShields = 2` (ya que el número de escudos en los parámetros no es menor)

### Conclusión

En conclusión, la clase `Damage` ajustada reflejará únicamente las armas y escudos presentes en los parámetros, asegurando que no se requiera perder más recursos de los disponibles.

Puedes consultar [el repositorio completo de la práctica en Ruby](https://github.com/eigenric/deepspace){:target="_blank"} para más detalles.

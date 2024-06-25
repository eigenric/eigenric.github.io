Title: Depuración final Deepspace - PDOO
Date: 2019-05-28
Tags: deepspace, pdoo, java

Me encuentro en el V Centenario con la necesidad de depurar finiquitando la
Práctica 5, es decir, la incorporación de una interfaz gráfica al juego
`Deepspace` desarrollado en Prácticas anteriores en el contexto de la asignatura
de Programación y Diseño Orientado a Objetos.

Se seguirá el Modelo-Vista-Controlador.  Sintetizando, el controlador hace de
intermediario entre la vista y el modelo. Puede haber varias vistas para un
único modelo-controlador.

La idea es que las vistas respeten la API declarada por el controlador y se
adapten a ella, representando los elementos del modelo (manipulados) de la forma
deseable.

Así pues, a lo largo de todas las prácticas hemos usado la Vista `TextView`
ofrecida por el profesor.  Ahora hemos creado una vista principal `MainView` que
descibre la Ventana Principal. Es una clase que hereda de `JFrame`. En esta vista,
se incluyen 2 paneles (heredan de la clase `JPanel`), uno para SpaceStation y otro
para `Enemy`. A estos paneles se les añade con `.add()` las vistas respectivas
(`SpaceStationView` y `EnemyView`).

Cuando se actualiza la vista de `MainView`, se sustituye el `SpaceStationView` por
la `currentStation` que tenga `GameUniverse` (el modelo del juego). El Enemigo va
cambiado de acuerdo a las cartas que fueron instanciadas en `CardDeck`.


Disponemos de 5 botones asociados con ciertos comportamientos. Los botones
Combatir, Salir, Siguiente turno, Equipar, Descartar y Descartar Hangar
Completo.

Iremos encontrando los Bugs con una metodología sistemática que nunca falla
hasta eliminarlos por completo.

## Bug #1 - Equipar no funciona

Cuando ciertos elementos de combate están seleccionados y se pulsa Equipar
(Montar), estos elementos no se montán.

El método controlador de equipar se ejecuta como confirma haber añadido "Botón
pulsado" en el método y este habiéndose mostrado por pantalla.

Por tanto, el resto del código también se ha ejecutado, incluyendo los mensajes
que deberían haberse mostrado para elementos en el for. Como no se han mostrado,
los Arrays que se recorrían estaban vacíos.


Esto reduce el bug a que `getSelectedWeaponsFromHangar()` y
`getSelectedShieldsFromHangar()` devuelven Arrays vacíos y no los arrays de las
posiciones de enteros que deberían mostrar.

Estos dos métodos son realmente un wrapper que llaman a los métodos del mismo
nombre de la clase `HangarView`.

Comprobaremos el funcionamiento de estos métodos en esta clase para encontrar el
fallo.

El código de `getSelectedWeapons` realiza lo siguiente:

Creamos un array vacío de Integer. Inicializamos un contador i a 0.

Recorremos los componentes de `jPanelHangar`, el cual es el panel que incluye el
`jScrollPanel1`.  Creemos que los elementos se añaden a `jPanelHangar` y no a
`ScrollPanel`. Estamos en lo cierto, como se observa en el método `setHangar`.

Estos componentes son de la clase Componente.  Realizamos un casting
(DownCasting) de cada uno de estos componentes a la clase `CombatElementView` la
cual realmente implementa el método `isSelected()` el cual únicamente devuelve ese
atributo `selected=0` que recordamos que está a true como confirma el color de los
`Weapons`. (solo se muestra el color si son opacos y sólo son opacos sin está
`selected` a `true`).

Además para confirmar que son Weapons debemos añadir otra condición y es que i <
nWeapons.  Recordamos que nWeapons es un atributo privado de instancia de esta
clase `HangarView`, el cual se actualiza en `setHangar` al número elementos que
tenga la lista weapons de `WeaponsToU` devuelta por la función `HangarToUI::getWeapons()`

Análogamente para `nShields.`

Así pues, el hangar contiene `nWeapons` weapons y `nShields` shields, y `nWeapons +
nShields <= capacity` (es decir el número máximo de elementos del hangar). La
idea, es que primero se insertar `nWeapons` Weapons y luego `nShields` Shields.

Luego, si obtenemos cada uno de estos componentes, solo bastará controlar el
índice para saber si estamos ante un `Weapon` o un `Shield`.

Como vemos, tenemos un `println` dentro de este `if`, el cual debería mostrarse en
la llamada a esta funciona. Com` no se muestra, determinamos que esta condición
nunca se cumple y se devuelve un Array vacío.

El bug se reduce a ver por qué no se cumple la condición. Es bastante obvio que
`isSelected()` tiene que ser `true`, por tanto veremos por qué `i` nunca es menor que
nWeapons.

Debido a que el Hangar está lleno de elementos, determinamos que se ha ejecutado
la función `setHangar` la cual rellena el hangar de `WeaponView` y
`ShieldBoosterView.`

En primer lugar, vamos a printear el valor de nWeapons en el for para ver que
nuestras suposiciones parciales son ciertas.

Como curiosidad, se ha mostrado lo de nWeapons en `SelctedWeapon`: 0 dos veces.
Nos preguntamo si es que hemos seleccionado dos Weapons en lugar de 1 y por
tanto el número de mensajes mostrados depende del número de armas seleccionadas
(lo cual no debería ocurrir).

Observamos que ya se pulse Equipar teniendo montado un Weapon o un
ShieldBooster, se muestra lo de 0 dos veces.

Nos extraña porque mount sólo llama a `SelectedWeapons` una vez.

Comprobaremos usando un nWeapons en `ShieldBooster`.  Según parece, ni siquiera
entra en el for, luego por tanto getComponents devuelve un Array vacío.

Es quizás que `jPanelHangar` no sea el elemento adecuado, sino el Scroll.

Sustituimos el código por `jScrollPanel` por probar suerte.

Confirmamos que con `jScrollPanel` se entra en el for y por tanto los
getComponents() no es vacío.

Se realiza solo una iteración y acto seguido da error. El error es:

`JViewport `no puede ser convertido a `CombatElementView`.

Procederemos a leer la información sobre un `ScrollPanel` del ejemplo propuesto
por el profesor.

Al parecer el problema es la creación de 2 hangares. cuantas veces se
llega al constructor de Hangar.

Al parecer llamar a `updateView` en la creación del botón es incorrecto.

> ¡El fallo estaba en el seteo al hangar! Se creaba uno nuevo y se añadia lo cual es un gran error.
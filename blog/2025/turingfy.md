Title: ¿Cómo suena una Máquina de Turing?
Date: 2025-07-16

![](/images/turing_musical.png){width="400px", height="275px"}

Las Máquinas de Turing son uno de los pilares fundamentales sobre los que se construye toda la ciencia de la computación. Propuestas por Alan Turing en 1936, no son máquinas físicas en el sentido tradicional, sino un modelo matemático abstracto que formaliza el concepto de "algoritmo".

En este post, vamos a desglosar este concepto: desde su densa definición formal hasta un ejemplo práctico, y finalmente, os mostraré mi propio experimento para traer este modelo a la vida: **Turingfy**.

### ¿Qué es una Máquina de Turing? La Definición Formal

A primera vista, la definición de una Máquina de Turing puede parecer intimidante. Es un formalismo matemático puro. Para no abrumar, he aquí primero la idea intuitiva:

Imagina una **cinta infinita** dividida en casillas. Un **cabezal** puede leer el símbolo de una casilla, escribir un nuevo símbolo y moverse a la izquierda o a la derecha. La máquina opera siguiendo un conjunto de **reglas** simples basadas en su **estado** actual y el símbolo que está leyendo.

**Definición.** Una **Máquina de Turing** se define formalmente como una 7-tupla:
 $$M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$$

donde:

> *   **$Q$**: Es un conjunto finito de **estados** en los que la máquina puede estar.
> *   **$\Sigma$**: Es el **alfabeto de entrada**, un conjunto finito de símbolos ($\Sigma \subseteq \Gamma$).
> *   **$\Gamma$**: Es el **alfabeto de la cinta**, que contiene a $\Sigma$ y al símbolo en blanco $B$.
> *   **$\delta$**: Es la **función de transición**, el "programa" de la máquina. Se define como:
    $$\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$$
    Mapea un estado y un símbolo a un nuevo estado, un nuevo símbolo y una dirección.
> *   **$q_0$**: Es el **estado inicial** ($q_0 \in Q$).
> *   **$B$**: Es el **símbolo en blanco** ($B \in \Gamma$).
> *   **$F$**: Es el conjunto de **estados finales o de aceptación** ($F \subseteq Q$).

### Equivalencia con el Lenguaje Post-Turing y un Ejemplo Práctico

Mientras que la Máquina de Turing es poderosa, su función de transición $\delta$ es poco intuitiva para escribir programas. Aquí entra en juego el **modelo Post-Turing**. Emil Post propuso un modelo equivalente con instrucciones más simples, parecidas a un lenguaje ensamblador:

1.  **Escribir un símbolo** en la posición actual.
2.  **Mover el cabezal** a la derecha (`RIGHT`).
3.  **Mover el cabezal** a la izquierda (`LEFT`).
4.  **Bifurcación condicional (`IF ... GOTO ...`)**: Ir a una instrucción X si el símbolo actual es Y.
5.  **Detener (`HALT`)**.

Se ha demostrado que ambos modelos son **computacionalmente equivalentes**. Para ilustrarlo, veamos cómo se escribe el programa para verificar palíndromos usando una sintaxis Post-Turing. El algoritmo sigue siendo el mismo: leer en un extremo, comparar en el otro y repetir.

Aquí está el programa, mucho más legible que una tabla de transiciones:

```text
# Programa Palindrome en sintaxis Post-Turing
# '#' representa el símbolo en blanco.
# Las líneas están numeradas para las instrucciones GOTO.

"START AGAIN",      # 0: Mueve el cabezal al inicio de la cinta.
"GOTO 2",           # 1: Salto incondicional al bucle principal.

# --- Bucle Principal (en la posición actual) ---
"IF #", "GOTO 29",  # 2-3: Si la cinta está vacía, es un palíndromo -> YES.
"IF 0", "GOTO 9",   # 4-5: Si lee '0', salta a la lógica del 0.
"IF 1", "GOTO 17",  # 6-7: Si lee '1', salta a la lógica del 1.
"GOTO 30",          # 8: Si es otro símbolo, rechaza -> NO.

# --- Lógica si el primer símbolo es '0' ---
"DELETE",           # 9: Borra el '0' del inicio (escribe #).
"RIGHT TO THE END", # 10: Va hasta el final de la palabra.
"LEFT",             # 11: Retrocede para leer el último carácter.
"IF #", "GOTO 29",  # 12-13: Si la cinta se acabó (palíndromo de un solo carácter), acepta -> YES.
"IF 0", "GOTO 25",  # 14-15: Si el final es '0', ¡coincide! Salta a borrar y repetir.
"GOTO 30",          # 16: No coincide, rechaza -> NO.

# --- Lógica si el primer símbolo es '1' ---
"DELETE",           # 17: Borra el '1' del inicio.
"RIGHT TO THE END", # 18: Va hasta el final de la palabra.
"LEFT",             # 19: Retrocede para leer el último carácter.
"IF #", "GOTO 29",  # 20-21: Si se acabó la cinta, acepta -> YES.
"IF 1", "GOTO 25",  # 22-23: Si el final es '1', ¡coincide!
"GOTO 30",          # 24: No coincide, rechaza -> NO.

# --- Subrutina de Éxito Parcial y Repetición ---
"DELETE",           # 25: Borra el carácter coincidente del final.
"START AGAIN",      # 26: Vuelve al inicio de la cinta.
"RIGHT",            # 27: Se mueve a la derecha para empezar en la siguiente posición no borrada.
"GOTO 2",           # 28: Vuelve al bucle principal.

# --- Estados Finales ---
"YES",              # 29: Aceptación.
"NO"                # 30: Rechazo.
```

Notarás instrucciones como `DELETE`, `START AGAIN` o `RIGHT TO THE END`. Son abstracciones comunes en simuladores que, a su vez, se pueden implementar con bucles de las instrucciones más básicas (`LEFT`, `RIGHT`, `IF...GOTO...`). Este estilo de programación demuestra por qué la equivalencia es tan útil: nos permite razonar sobre algoritmos de una forma mucho más natural.

### Turingfy: Un Máquina de Turing Musical

Leer sobre la teoría está muy bien, pero como entusiasta de la tecnología, ¡quería verlo en acción!

Por eso creé Turingfy: un proyecto personal que combina mi pasión por la música con la computación teórica.
La idea surge de un juego de palabras: tanto las Máquinas de Turing como los reproductores de música usan "cintas". 

En Turingfy, los programas son playlists de Spotify donde cada canción representa una instrucción del programa. La descripción de la playlist contiene el input inicial de la cinta, y mientras el programa se ejecuta paso a paso, cada instrucción reproduce su canción correspondiente.

Es un intérprete que utiliza la API de Spotify para cargar programas como el que analizamos anteriormente.
Lo fascinante es que la música que se escucha es el algoritmo que se ejecuta.


### Turingfy en Acción: Videos de Demostración

¡Un video vale más que mil palabras! Aquí os dejo un par de demostraciones de Turingfy ejecutando programas.

1.  **Demostración: Verificador de Palíndromos: Palabra Rechazada**

    En este video, cargo el programa de Post-Turing en Turingfy y lo ejecuto con la entrada `10010`. Podéis ver cómo el cabezal viaja de un extremo a otro, "borrando" los símbolos coincidentes, siguiendo exactamente las instrucciones que hemos definido.
    **La canción final es "Rejekto" de Robotiko Rejekto que indica que la palabra no es un palíndromo.**

    <!-- Reemplaza con el iframe de tu video -->
    <iframe width="560" height="315" src="https://www.youtube.com/embed/IOZc2kXENnY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

2.  **Demostración: Verificador de palíndromos: Palabra Aceptada**

    En este segundo video, ejecuto el mismo programa con la entrada `010`. Aquí veréis cómo el cabezal se mueve de forma similar, pero esta vez termina aceptando la palabra como un palíndromo. **La canción final en este caso es "Yes It Is" de The Beatles, que indica que la palabra es un palíndromo.**

    <!-- Reemplaza con el iframe de tu video -->
    <iframe width="560" height="315" src="https://www.youtube.com/embed/dnAf5fu6DmA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    

El código fuente está disponible en [GitHub](https://github.com/eigenric/turingfy) para quien quiera explorar la implementación.

### Conclusión

La Máquina de Turing es mucho más que una curiosidad matemática. Es la esencia de lo que significa "computar". Y su equivalencia con modelos como el de Post nos permite diseñar algoritmos complejos usando bloques de construcción increíblemente simples.

Espero que este viaje desde la 7-tupla formal hasta mi modesto proyecto Turingfy os haya resultado interesante y, quizás, os inspire a crear vuestras propias implementaciones. Al final del día, la mejor forma de entender algo es construyéndolo.
Title: Descifrando a Will Hunting
Date: 2026-10-05
Category: Matemáticas
Tags: Will Hunting, Teoría de Grafos, Matrices, Funciones Generatrices, Árboles
Summary: Resolución matemática rigurosa y paso a paso de los famosos problemas expuestos en el MIT en la película Good Will Hunting: matrices de adyacencia, funciones generatrices de recorridos y árboles homeomórficamente irreducibles.
Image: /images/matrixproblem.png

![Problema de grafos y matrices expuesto en la pizarra de El indomable Will Hunting](/images/matrixproblem.png){width="650px"}

La película *El indomable Will Hunting* (*Good Will Hunting*, 1997) dejó para la historia del cine una de las escenas más memorables para los amantes de las matemáticas: el profesor Gerald Lambeau deja planteado en la pizarra del pasillo del MIT un problema de teoría de grafos para sus estudiantes de doctorado. Will Hunting, un joven conserje sin educación formal pero con un talento genial, lo resuelve anónimamente por la noche.

En este artículo abordamos la resolución matemática completa, detallada y rigurosa de los **dos problemas** que aparecen expuestos en las pizarras de la película.

---

# Problema 1: Álgebra de Grafos, Matrices y Funciones Generatrices

El primer problema planteado en la pizarra exige el estudio algebraico de un grafo no dirigido $G$ mediante matrices de adyacencia y funciones generatrices.

### Descripción del Grafo $G$

A partir del diagrama expuesto en la primera pizarra de la película:

![Esquema visual del grafo G con 4 vértices y aristas paralelas entre 2 y 3](/images/graph.png){width="360px"}

El grafo $G = (V, E)$ es un multigrafo no dirigido definido formalmente por:

* **Vértices:** $V = \{1, 2, 3, 4\}$.
* **Aristas ($|E| = 5$):** 
  * Un subgrafo en forma de **triángulo** simple entre los vértices $1$, $2$ y $4$, correspondiente a las aristas $\{1,2\}$, $\{2,4\}$ y $\{1,4\}$.
  * Un **ciclo doble** (dos aristas paralelas o multiarista) uniendo exclusivamente los vértices $2$ y $3$, denotadas como $e_{23}^{(1)}$ y $e_{23}^{(2)}$.
* **Grados de los vértices:**
  * $\operatorname{deg}(1) = 2$ (conectado con $2$ y $4$).
  * $\operatorname{deg}(2) = 4$ (conectado con $1$, $4$, y mediante $2$ aristas con $3$).
  * $\operatorname{deg}(3) = 2$ (conectado mediante $2$ aristas con $2$).
  * $\operatorname{deg}(4) = 2$ (conectado con $1$ y $2$).

Suma total de grados: $\sum_{v \in V} \operatorname{deg}(v) = 2 + 4 + 2 + 2 = 10 = 2 |E|$, cumpliendo el Lema del Apretón de Manos.

---

### 1) Matriz de adyacencia $A$

La entrada $a_{ij}$ representa el número de aristas directas entre el vértice $i$ y el vértice $j$:
* El vértice $1$ está conectado con $2$ y $4$.
* El vértice $2$ está conectado con $1$, con $4$, y tiene **2 aristas** con $3$.
* El vértice $3$ tiene **2 aristas** con $2$.
* El vértice $4$ está conectado con $1$ y $2$.

Por tanto, la matriz de adyacencia es:

$$A = \begin{pmatrix} 
0 & 1 & 0 & 1 \\ 
1 & 0 & 2 & 1 \\ 
0 & 2 & 0 & 0 \\ 
1 & 1 & 0 & 0 
\end{pmatrix}$$

---

### 2) Matriz del número de recorridos de longitud 3 ($A^3$)

Por teoría espectral de grafos, la entrada $(A^k)_{ij}$ indica el número de caminos (*walks*) de longitud exactamente $k$ entre el vértice $i$ y el vértice $j$.

#### Paso 1: Calculamos $A^2$
Multiplicando $A$ por sí misma:

$$A^2 = A \cdot A = \begin{pmatrix} 
0 & 1 & 0 & 1 \\ 
1 & 0 & 2 & 1 \\ 
0 & 2 & 0 & 0 \\ 
1 & 1 & 0 & 0 
\end{pmatrix} 
\begin{pmatrix} 
0 & 1 & 0 & 1 \\ 
1 & 0 & 2 & 1 \\ 
0 & 2 & 0 & 0 \\ 
1 & 1 & 0 & 0 
\end{pmatrix}
= \begin{pmatrix} 
2 & 1 & 2 & 1 \\ 
1 & 6 & 0 & 1 \\ 
2 & 0 & 4 & 2 \\ 
1 & 1 & 2 & 2 
\end{pmatrix}$$

*(Por ejemplo, $(A^2)_{22} = 6$ corresponde a ir y volver por cada una de sus aristas incidentes: $1 + 1 + 2^2 = 6$).*

#### Paso 2: Calculamos $A^3 = A^2 \cdot A$

$$A^3 = \begin{pmatrix} 
2 & 1 & 2 & 1 \\ 
1 & 6 & 0 & 1 \\ 
2 & 0 & 4 & 2 \\ 
1 & 1 & 2 & 2 
\end{pmatrix}
\begin{pmatrix} 
0 & 1 & 0 & 1 \\ 
1 & 0 & 2 & 1 \\ 
0 & 2 & 0 & 0 \\ 
1 & 1 & 0 & 0 
\end{pmatrix}
= \begin{pmatrix} 
2 & 7 & 2 & 3 \\ 
7 & 2 & 12 & 7 \\ 
2 & 12 & 0 & 2 \\ 
3 & 7 & 2 & 2 
\end{pmatrix}$$

Esta es la matriz que proporciona el número de recorridos de 3 pasos entre cualquier par de vértices.

---

### 3) Función generatriz para recorridos de $i \to j$

La función generatriz ordinaria que codifica el número de recorridos de longitud $k$ como coeficientes de una serie formal es:

$$G_{ij}(x) = \sum_{k=0}^{\infty} (A^k)_{ij} x^k$$

En forma matricial compacta, sumando la serie geométrica de matrices:

$$G(x) = \sum_{k=0}^{\infty} (x A)^k = (I - x A)^{-1}$$

{% toggle %}

Definimos

$$
S(x)=I+xA+x^2A^2+x^3A^3+\cdots
$$

Entonces

$$
(I-xA)S(x)
$$

es

$$
\begin{aligned} 
&(I-xA) (I+xA+x^2A^2+x^3A^3+\cdots) \\ 
&=I+xA+x^2A^2+x^3A^3+\cdots \\ 
&\quad-xA-x^2A^2-x^3A^3-\cdots \\ 
&=I 
\end{aligned}
$$

Todo lo que queda después del $I$ se cancela término a término.

Por tanto,

$$
S(x)=(I-xA)^{-1}
$$

{% end_toggle %}

Por la regla de la matriz adjunta (o regla de Cramer), para cualquier par de nodos $i, j$:

$$G_{ij}(x) = \left[(I - xA)^{-1}\right]_{ij} = \frac{(-1)^{i+j} \det\big((I - xA)_{ji}\big)}{\det(I - xA)}$$

donde $(I - xA)_{ji}$ es la submatriz resultante de eliminar la fila $j$ y la columna $i$.

---

### 4) Función generatriz de recorridos de $1 \to 3$

Aplicamos la fórmula anterior específicamente para $i = 1$ y $j = 3$:

$$G_{13}(x) = \left[(I - xA)^{-1}\right]_{13} = \frac{C_{31}}{\det(I - xA)}$$

siendo $C_{31} = (-1)^{3+1} \det(M_{31}) = \det(M_{31})$ el cofactor correspondiente.

La matriz $I - xA$ es:

$$I - xA = \begin{pmatrix} 
1 & -x & 0 & -x \\ 
-x & 1 & -2x & -x \\ 
0 & -2x & 1 & 0 \\ 
-x & -x & 0 & 1 
\end{pmatrix}$$

#### 1. Cálculo del denominador: $\det(I - xA)$
Desarrollando por la tercera fila (que contiene dos ceros):

$$\begin{aligned}
\det(I - xA) &= -(-2x) \begin{vmatrix} 1 & 0 & -x \\ -x & -2x & -x \\ -x & 0 & 1 \end{vmatrix} \\
&\quad + 1 \begin{vmatrix} 1 & -x & -x \\ -x & 1 & -x \\ -x & -x & 1 \end{vmatrix}
\end{aligned}$$

* Primer menor: Desarrollando por la segunda columna:
  $$\begin{vmatrix} 1 & 0 & -x \\ -x & -2x & -x \\ -x & 0 & 1 \end{vmatrix} = -2x(1 - x^2)$$
* Segundo menor:
  $$\begin{vmatrix} 1 & -x & -x \\ -x & 1 & -x \\ -x & -x & 1 \end{vmatrix} = 1 - 3x^2 - 2x^3$$

Combinando ambos términos:
$$\begin{aligned}
\det(I - xA) &= 2x[-2x(1 - x^2)] + (1 - 3x^2 - 2x^3) \\
&= 1 - 7x^2 - 2x^3 + 4x^4
\end{aligned}$$

Este polinomio factoriza de manera exacta extrayendo la raíz $x = -1$:
$$\det(I - xA) = (1 + x)(1 - x - 6x^2 + 4x^3)$$

---

#### 2. Cálculo del numerador: $\det(M_{31})$
Eliminando la fila 3 y la columna 1 de $I - xA$:

$$M_{31} = \begin{pmatrix} 
-x & 0 & -x \\ 
1 & -2x & -x \\ 
-x & 0 & 1 
\end{pmatrix}$$

Desarrollando por la segunda columna:
$$\det(M_{31}) = -2x \begin{vmatrix} -x & -x \\ -x & 1 \end{vmatrix} = -2x(-x - x^2) = 2x^2(1 + x)$$

---

#### 3. Simplificación final
Sustituyendo el numerador y el denominador:

$$G_{13}(x) = \frac{2x^2(1 + x)}{(1 + x)(1 - x - 6x^2 + 4x^3)}$$

Cancelando el factor común $(1 + x)$:

$$\boxed{G_{13}(x) = \frac{2x^2}{1 - x - 6x^2 + 4x^3}}$$

---

### Comprobación (desarrollo en serie):
Si efectuamos la división polinómica o la recurrencia de coeficientes:

$$G_{13}(x) = 0 + 0x + \mathbf{2}x^2 + \mathbf{2}x^3 + \mathbf{14}x^4 + \dots$$

* Longitud 0: $(A^0)_{13} = 0$
* Longitud 1: $(A^1)_{13} = 0$
* Longitud 2: $(A^2)_{13} = 2$ (recorridos: $1 \to 2 \xrightarrow{e_1} 3$ y $1 \to 2 \xrightarrow{e_2} 3$)
* Longitud 3: $(A^3)_{13} = 2$ (coincide con la entrada calculada en el apartado 2)
* Longitud 4: $(A^4)_{13} = 14$

La solución concuerda plenamente con las propiedades combinatorias del grafo.

---

# Problema 2: Árboles Homeomórficamente Irreducibles de 10 Vértices

El segundo problema presentado en la película (tras la célebre fórmula de Cayley $n^{n-2}$ para el número de árboles etiquetados) plantea la siguiente cuestión combinatoria:

> **Enunciado:** Dibujar todos los árboles homeomórficamente irreducibles (*homeomorphically irreducible trees*) de $n = 10$ vértices.

![Árboles homeomórficamente irreducibles de 10 vértices en la pizarra](/images/10homeomorphic.png){width="650px"}

### ¿Qué es un Árbol Homeomórficamente Irreducible?

* **Árbol:** Un grafo conexo y acíclico de $n$ vértices tiene exactamente $|E| = n - 1$ aristas. Para $n = 10$, tenemos $|E| = 9$ aristas.
* **Homeomórficamente irreducible:** Un árbol es homeomórficamente irreducible si **no contiene vértices de grado 2** ($\operatorname{deg}(v) \neq 2$ para todo $v \in V$).

*Justificación matemática:* Subdividir una arista insertando un vértice de grado 2 no altera la estructura topológica esencial de la red (es un homeomorfismo de grafos). Por tanto, al prohibir los vértices de grado 2, se clasifican las topologías puras de ramificación.

---

### Clasificación Álgebraica por Secuencias de Grados

Sea $T = (V, E)$ un árbol con $n = 10$ vértices y $|E| = 9$ aristas. Por el Lema del Apretón de Manos (*Handshaking Lemma*):

$$\sum_{v \in V} \operatorname{deg}(v) = 2 |E| = 2 \times 9 = 18$$

Dado que no se permiten vértices de grado 2, los grados posibles de cada vértice son $d_i \in \{1, 3, 4, 5, 6, 7, 8\}$.

Sean:
* $L$: número de hojas ($\operatorname{deg}(v) = 1$).
* $I$: número de vértices internos ($\operatorname{deg}(v) \ge 3$).

Cumpliéndose $L + I = 10$ (lo que implica $L = 10 - I$). La suma total de grados satisface la desigualdad:

$$\begin{aligned}
18 = \sum_{v \in V} \operatorname{deg}(v) &= L + \sum_{i=1}^{I} \operatorname{deg}(v_i) \\
&\ge L + 3I \\
&= (10 - I) + 3I \\
&= 10 + 2I
\end{aligned}$$

Por lo tanto:

$$18 \ge 10 + 2I \implies 2I \le 8 \implies I \le 4$$

Analizamos a continuación las particiones posibles de la suma de grados según el número de vértices internos $I \in \{1, 2, 3, 4\}$, identificando cada caso con su número correspondiente en la imagen:

{% toggle 1. Caso I = 1 vértice interno (L = 9 hojas) %}

* Suma de grados del único vértice interno: $18 - 9 = 9$.
* Secuencia de grados: $(9, 1, 1, 1, 1, 1, 1, 1, 1, 1)$.
* Genera **1 árbol**: **Árbol 1** en la imagen (la estrella pura $K_{1,9}$ con un nodo central morado de grado 9).

{% end_toggle %}

{% toggle 2. Caso I = 2 vértices internos (L = 8 hojas) %}

* Suma de grados de las 8 hojas: $8 \times 1 = 8$.
* Suma de grados de los 2 vértices internos: $18 - 8 = 10$.
* Particiones de 10 en 2 enteros $\ge 3$:
  * $7 + 3 = 10 \implies$ **Árbol 2** en la imagen (nodo rojo de grado 7 unido a nodo verde de grado 3).
  * $6 + 4 = 10 \implies$ **Árbol 3** en la imagen (nodo naranja de grado 6 unido a nodo verde de grado 4).
  * $5 + 5 = 10 \implies$ **Árbol 4** en la imagen (dos nodos naranjas de grado 5 unidos directamente).
  * Total para $I = 2$: **3 árboles no isomórficos** (Árboles 2, 3 y 4).

{% end_toggle %}

{% toggle 3. Caso I = 3 vértices internos (L = 7 hojas) %}

* Suma de grados de las 7 hojas: $7 \times 1 = 7$.
* Suma de grados de los 3 vértices internos: $18 - 7 = 11$.
* Las particiones de 11 en 3 enteros $\ge 3$ son:
  * **Subcaso 3.1 ($4 + 4 + 3 = 11$):** Genera 2 estructuras con nodos de grado 4:
    * **Árbol 5** en la imagen (cadena $P_3$ con secuencia de grados 4-4-3).
    * **Árbol 6** en la imagen (cadena $P_3$ con secuencia de grados 4-3-4 y el nodo de grado 3 en la posición central).
  * **Subcaso 3.2 ($5 + 3 + 3 = 11$):** Genera 2 estructuras con un nodo de grado 5:
    * **Árbol 7** en la imagen (ramificación $K_{1,2}$ interna con el nodo de grado 5 en la raíz).
    * **Árbol 8** en la imagen (cadena $P_3$ con el nodo de grado 5 en el extremo superior).
  * Total para $I = 3$: **4 árboles no isomórficos** (Árboles 5, 6, 7 y 8).

{% end_toggle %}

{% toggle 4. Caso I = 4 vértices internos (L = 6 hojas) %}

* Suma de grados de las 6 hojas: $6 \times 1 = 6$.
* Suma de grados de los 4 vértices internos: $18 - 6 = 12$.
* Única partición de 12 en 4 enteros $\ge 3$: $3 + 3 + 3 + 3 = 12$.
* Secuencia de grados: $(3, 3, 3, 3, 1, 1, 1, 1, 1, 1)$.
* El árbol esqueleto formado por los 4 nodos de grado 3 genera 2 estructuras:
  * **Árbol 9** en la imagen (esqueleto en estrella $K_{1,3}$, con 1 centro de grado 3 unido a 3 nodos de grado 3).
  * **Árbol 10** en la imagen (esqueleto en cadena $P_4$, con 4 nodos lineales de grado 3).
  * Total para $I = 4$: **2 árboles no isomórficos** (Árboles 9 y 10).

{% end_toggle %}

---

### Recuento Total

Sumando todos los casos estructurales posibles:

$$\text{Total} = \underbrace{2}_{I=4} + \underbrace{4}_{I=3} + \underbrace{3}_{I=2} + \underbrace{1}_{I=1} = \mathbf{10 \text{ árboles homeomórficamente irreducibles}}$$

![Diagrama etiquetado con la lista completa de los 10 árboles homeomórficamente irreducibles](/images/trees_labeled.png){width="550px"}

---

### Conclusión

Los problemas de *El indomable Will Hunting*, aunque presentados en la gran pantalla con cierto aura de inalcanzable misterio académico, son magníficos ejemplos de la elegancia de la **teoría espectral de grafos** y de la **combinatoria topológica**. 

El primero demuestra cómo el álgebra lineal trasciende al cálculo de caminos y funciones generatrices en redes; el segundo ilustra el poder de las invariantes de grado para clasificar estructuras complejas a partir de restricciones fundamentales.

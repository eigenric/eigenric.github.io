Title: Demostración del Lema de Zorn - Draft
Date: 2020-07-01
Tags: demostración, lema, zorn
Status: Hidden

Es un Lema básico en Teoría de Conjuntos que permite probar la existencia de bases de Espacios Vectoriales, entre otros resultados de Álgebra abstracta.

> **Lema de Zorn.** Si $(X, \leq)$ es un conjunto preordenado en el que toda cadena está acotada superiormente. Entonces $(X, \leq)$ tiene un elemento maximal.

## Definiciones previas

Se dice que $(X, \leq)$ es un **conjunto preordenado (o proset)** cuando algunos elementos pueden ser comparados $a \leq b$ o $b \leq a$


Se dice que $(X, \leq)$ es un **conjunto parcialmente ordenado (o poset)** cuando es un proset con la propiedad antisimétrica $a \leq b$ y $b \leq a$ $\Leftrightarrow$ $a = b$


Se dice que $(X, \leq)$ es un **conjunto totalmente ordenado (o toset)** cuando es un poset con todos los elementos comparables.

En lo siguiente $(X, \leq)$ es un conjunto preordenado o proset.


Sea $S \subset X$. Diremos que $m \in S$ es un **elemento maximal** (resp. **minimal**) cuando no hay elemento de $S$ (estrictamente) mayor (respectivamente estrictamente menor). Formalmente, $m$ es maximal en $S$ si para todo $s \in S$ si $m \leq s$ entonces $m = s$. Análogamente para el minimal.

Sea $S \subset X$. Diremos que $m \in S$ es el **máximo** (resp. **mínimo**) cuando es mayor (resp. menor) que todos los elementos de $S$. Formalmente, $m$ es máximo en $S$ si para todo $s \in S$ $s \leq m$. Análogamente para el mínimo.

**Observación:** el elemento maximal/minimal no tiene por qué ser único. No confundir con el máximo/mínimo. Éste es mayor/menor que todos (y por tanto comparable) lo cual no tiene por que suceder con el elemento maximal/minimal.

**Proposición.** Si $S \subset X$ es un conjunto parcialmente ordenado o poset y tiene máximo (resp. mínimo) entonces es el único elemento maximal (resp. minimal).

<details>
<summary>Demostración</summary>
**Dem.**
> -  Sea $m \in S$, si $s \in S$ tal que $m \leq s$   necesariamente por ser $m$ máximo $s \leq m$ y por tanto por la propiedad antisimétrica de los posets $m = s$ ($m$ es maximal, pues no hay elemento estrictimente mayor). $\square$

> - Sea $m' \in S$, si $s \in S$ tal que $s \leq m'$ necesariamente por ser $m'$ mínimo $m '\leq s$ y por la propiedad antisimétrica de los posets, $m' = s$. ($m'$ es minimal pues no hay elemento estrictamente menor) $\square$

> - Para la unicidad, sea $m$ el máximo de $S$. Supongamos que existe otro elemento $m' \in S$ tal que $m'$ es maximal. Por ser $m$ el máximo, $m' \leq m$. Pero $m'$ es maximal, lo que implica que no puede haber un elemento mayor que $m'$, entonces $m = m'$. Por lo tanto, $m$ es el único elemento maximal. $\square$

> - Análogamente para el mínimo.
</details>

**Proposición** Si $S \subset X$ es un conjunto totalmente ordenado o toset y tiene un elemento maximal (resp. minimal) entonces coincide con el máximo (resp. mínimo).

> **Dem.**
Sea $m \in S$ un elemento maximal entonces no existe elemento estrictamente mayor que él. Como $S$ es toset todos los elementos son comparables y por tanto todos son menores que $m$. La unicidad se da por ser poset en particular.
Sea $n \in S$ un elemento minimal entonces no existe elemento estrictamente menor que él. Como $S$ es toset todos los elementos son comparables y por tanto todos son mayores que $n$.

**Definición.** Se dice que $A \subset X$ es un conjunto **bien ordenado** cuando es totalmente ordenado y todo subconjunto suyo no vacío tiene mínimo.  La clase de subconjuntos de $X$ bien ordenados se denota como $Well(X)$

**Definición.** $S \subseteq X$ es un **conjunto cerrado inferiormente** en $X$ si para cualquier $u \in S$, si $v \in X$ tal que $v \leq u$ entonces $v \in S$. 

**Observación:** Todo conjunto es cerrado inferiormente en sí mismo.

Se dice que $C \subset X$ es una **cadena de $X$** sii por def $(C, \leq)$ es totalmente ordenado.

**Definición.** Si $C$ es cadena de $X$ y $x \in C$, entonces llamamos **segmento inicial** de $x$ en $C$ a los elementos de $C$ estrictamente menores que $x$.
$$
    I_c(x) = \{y \in C : y \lt x\}
$$

**Observación:** los segmentos iniciales son cerrados inferiormente.

En efecto, sea $u \in I_c(x)$ entonces $u \lt x$. Si $v \in X$ tal que $v \leq u$ entonces $v \lt x$ y por tanto $v \in I_c(x)$.

**Axioma de Elección.** Dado un conjunto no vacío $X$, existe una función $f$ que asigna a cada subconjunto no vacío de $X$ un elemento de él.

## Teorema (Lema de Zorn). 

> **Lema de Zorn.** Si $(X, \leq)$ es proset en el que toda cadena está acotada superiormente. Entonces $(X, \leq)$ tiene un elemento maximal.

Supongamos que $(X, \leq)$ no tiene elemento maximal y lleguemos a contradicción. Sea $C$ una cadena en $X$, y por hipótesis $u \in X$ una cota superior de $C$. Como no hay elemento maximal, necesariamente existe $v \in X$ tal que $u \lt v$. Luego $C$ admite una **cota superior estricta.**

Utilizando el Axioma de Elección, existe una función $f$ que asigna a una cadena $C \subset X$ bien ordenada una cota superior estricta $f(C)$.

La contradicción buscada consistirá en encontrar una cadena $U \subset X$ tal que $f(U) \in U$.

Para ello, definimos la noción de conjunto $f$-inductivo.

**Definición** $A \in Well(X)$ es **f-inductivo** si para todo $x \in A$
$$
x = f(I_A(x))
$$


Los conjuntos f-inductivos cumplen el siguiente **lema de comparación**.

> **Lema:** Si $A, B \subset X$ son f-inductivos y $A \neq B$, entonces uno de los dos es segmento inicial del otro.

**Dem**.

Como $A \neq B$ podemos asumir sin pérdida de generalidad que $A \setminus B \neq \emptyset$.

Sea $x = \min(A \setminus B)$, probaremos que $B$ es segmento inicial de $x$ en $A$

$$I_A(x) = B$$


$\boxed{\subset}\;\;$

Sea $y \in I_A(x)$ entonces $y \in A$ tal que $y \lt x$. Como $x = \min(A \setminus B)$. Si $y \notin B$ entonces $y \in A \setminus B$ siendo menor que el mínimo. Luego $y \in B$


$\boxed{\supset}\;\;$

Supongamos $B \setminus I_A(x) \neq \emptyset$ y lleguemos a contradicción.

Sea $y = \min(B \setminus I_A(x))$.
Sea $z = \min(A \setminus I_B(y))$.

**Lema de Cierre.** Dado cualquier $u \in I_B(y)$, si $v \in A$ y $v \lt u$ entonces:

- $v \lt y$  (por def. de $I_B(y)$)
- $v \in B$ 

Luego $v \in I_B(y)$

> **Dem**.
Basta ver que $v \in B$.
Como $u \in I_B(y)$, $u \in B$ y $u \lt y$. 
Por def. $y = \min(B \setminus I_A(x))$, luego si $u \notin I_A(x)$, entonces $u \in B \setminus I_A(x)$  siendo menor que el mínimo.
Por tanto $u \in I_A(x)$
Como $v \in A$ tal que $v \lt u$, es claro que $v \in I_A(x) \subset B$. $\square$


Con este resultado podemos probar que
$$
I_A(z) = I_B(y)
$$

- $I_A(z) \subset I_B(y)$

Sea $u \in I_A(z)$, entonces $u \in A$ tal que $u \lt z$.
Como $z = \min(A \setminus I_B(y))$, si $u \notin I_B(y)$ entonces $u \in A \setminus I_B(y)$ siendo menor que el mínimo.
Por tanto $u \in I_B(y)$


- $I_A(z) \supset I_B(y)$

Sea $u \in I_B(y)$ entonces $u \in I_A(x)$ (por def. de $y$), luego $u \in A$ y podemos compararlo con $z$.
Es claro que $u \neq z$ por def de $z$.
Además si $z \lt u$, por el *Lema de Cierre*, se tendría que $z \in I_B(y)$ contradiciendo la def. de $z$.
Por tanto $u \lt z$. Como $u \in A$, se sigue que $u \in I_A(z)$.

Además, $z \leq x$ por ser

$$ A \setminus B \subset A \setminus I_B(y)$$

Usando la **f-inductividad** de $A$ y $B$ tendríamos que 

$z = f(I_A(z)) = f(I_B(y)) = y$

Y como $y \in B$ no puede ser $z = x$ (ya que $x \notin B$ por def.).
Por tanto, $z \lt x$ y concluimos que 
$$y = z \in I_A(x)$$

en contra de la def. de $y$.

Esto implica $B \setminus I_A(x) = \emptyset$ o equivalentemente $B \subset I_A(x)$. $\square$.


Aplicando el **Lema de comparación** a la colección de conjuntos $f$-inductivos llegamos a que es totalmente ordenada por la inclusión de conjuntos cerrados inferiormente.

La unión $U$ de todos ellos es por el **Lema de Union de c.c.i** un conjunto bien ordenado. ($U \in Well(X)$)

Además, sea 
$$
x \in U = \bigcup_{S \ f-ind} S
$$

entonces existe $S_x$ $f$-inductivo tal que $x \in S_x$ por lo que
$$
x = f(I_{S_x}(x)) = f(I_U(x))
$$

usando el **Corolario** del **Lema de Union de c.c.i**.

Luego $U$ es el subconjunto $f$-inductivo maximal.

Considerando su cota superior estricta $f(U)$ entonces $U' = U \cup \{f(U)\}$ está totalmente ordenado por estarlo $U$ y por ser $u \lt f(U)$ para todo $u \in U$. Además, 

$$
I_{U'}(f(U)) = I_{U\cup \{f(U)\}}(f(U)) = U
$$

luego

$$
f(I_{U'}(f(U))) = f(U)
$$

concluyendo que $U \cup \{f(U)\}$ es un conjunto $f$-inductivo que estaría necesariamente en el maximal obteniendo $f(U) \in U$ en contra de la def. $f(U)$ como cota superior estricta de $U$. $\square$

> **Lema de Union de c.c.i** 
> - Sea $P_\alpha$ una colección de subconjuntos de $X$, cada uno con un buen-orden $\leq_\alpha$, tal que para cualquier $\alpha, \beta$, uno de $P_\alpha$, $P_\beta$ (cada uno con su orden) es cerrado inferiormente en el otro. 
> - Sea $P$ la unión $\cup_\alpha \ P_\alpha$, con el orden $x \leq y$ sii por def. $x \leq_\alpha y$ en algún $P_\alpha$ que contenga a ambos. 

> Entonces $P$ está bien ordenado por $\leq$, con cada $P_\alpha$ cerrado inferiormente en $P$

**Dem**

Observamos que $\leq$ está bien definido y es un orden total. Sean $x, y \in P$, entonces $x \in P_\alpha$ e $y \in P_\beta$ para ciertos $\alpha, \beta$, donde uno de $P_\alpha, P_\beta$ es segmento inicial del otro. Sin pérdida de generalidad, suponemos $P_\alpha \subset P_\beta$ entonces $x, y$ son comparables en $P_\beta$.

Sea $u \in P_\alpha$ y $v \in P$, entonces $v \in P_\beta$ para cierto $\beta$. Supongamos además $v \leq u$. Por hipótesis, uno de $P_\alpha, P_\beta$ es cerrado inferiormente en el otro. Si $P_\alpha$ es c.i en $P_\beta$, se sigue que $v \in P_\alpha$. Por el contrario, si $P_\beta$ es c.i en $P_\alpha$ trivialmente $v \in P_\alpha$. Luego cada $P_\alpha$ es cerrado inferiormente en $P$:

Si $\emptyset \neq T \subset P$  entonces $T \cap P_\alpha \neq \emptyset$ para cierto $\alpha$ luego hay un mínimo $t \in T \cap P_\alpha$ con respecto a $\leq_\alpha$. Este $t$ es mínimo en $T$ con respecto a $\leq$.  Para $s \in T$ con $s \leq t$, por ser $P_\alpha$ c.i en $P$ necesariamente $s \in P_\alpha$.
Así $s \in T \cap P_\alpha$ y por def. de mínimo $t \leq_\alpha s$. Por tanto, $t \leq s$. $\square$

**Observación**: realmente hemos probado que $t$ es un elemento minimal en $(T, \leq)$ pero esto es equivalente a ser el mínimo por el orden total de $\leq$.

> **Corolario** 
En las condiciones del lema anterior, se verifica que para cualquier $x \in P$ de donde $x \in P_\alpha$
$$
I_{P_\alpha}(x) = I_P(x)
$$


- Sea $y \in I_{P_\alpha}(x)$ entonces $y \in P_\alpha \subset P$ tal que $y \lt x$. Luego $y \in I_P(x)$.
- Sea $y \in I_P(x)$ entonces $y \in P$ tal que $y \lt x$. Como $P_\alpha$ es c.c.i en $P$ por el **Lema de Union de c.i**, se tiene que $y \in P_\alpha$ y por tanto $y \in I_{P_\alpha}(x)$..
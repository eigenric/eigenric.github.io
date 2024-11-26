Title: El grupo fundamental de la cinta de Möbius
Date: 2024-11-26
Tags: topología, retracto, manim

<br>

<center>
<iframe width="500" height="300" src="https://www.youtube.com/embed/savG0a_MijQ?si=29DqwxaXU0VHxF2e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

La cinta de Möbius es una superficie no orientable que ha fascinado a matemáticos debido a sus propiedades geométricas y topológicas singulares

Esta figura se obtiene al darle una media vuelta a una tira de papel y unir sus extremos y presenta características inusuales cuando se estudian desde la topología. 

El grupo fundamental de un espacio topológico $X$, $\Pi_1(X, x_0)$  describe las clases de homotopía de lazos cerrados y es un invariante topológico crucial para caracterizar su estructura. 

En este artículo, haremos el cálculo del grupo fundamental de la cinta de moebius. Se ha creado además una animación en [Manim](https://www.manim.community/) que ilustra el argumento utilizando mediante el concepto de *retracto de deformación*, que consiste basicamente en una transformación continua hacia la circunferencia.

# Lema: Función continua inducida en los cocientes.

Sean $(X_j, \tau_j)$ espacios topológicos. $R_j$ relación de equivalencia en $X_j$.
$\pi_j: X_j \rightarrow \frac{X_j}{R_j}$ la proyección al cociente. $j=1,2$.

Sea $f: (X_1, \tau_1) \rightarrow (X_2, \tau_2)$ una aplicación continua que cumple:

$$
\forall p,q \in X_1 \quad p R_1 q \Rightarrow f(p) R_2 f(q)
$$

Entonces existe una única aplicación

$$
\tilde{f}: (X_1/R_1, \tau_1(\pi_1)) \rightarrow (X_2/R_2, \tau_2(\pi_2))
$$ 

tal que $\tilde{f} \circ \pi_1 = \pi_2 \circ f$.

En efecto: $\tilde{f}([p]_1) = [f(p)]_2$

![Diagrama conmutativo](/images/diagrama_lema.png){width=200px}

Además, $\tilde{f}$ es continua.

{% toggle %}

$\tilde{f}$ continua $\Leftrightarrow \tilde{f} \circ \pi_1$ continua. Pero $\tilde{f} \circ \pi_1 = \pi_2 \circ f$.

{% end_toggle %}

# Proposición: El grupo fundamental de la cinta de Möebius es isomorfo a $\mathbb{Z}$

En efecto, la cinta de Möeboius compacta es

$$
M = \frac{[-1, 1] \times [-1, 1]}{R}
$$
donde en $[-1, 1] \times [-1, 1]$ tenemos la topología usual y $R$ es la relación de equivalencia dada por

$$
(x, y) R (x', y') \Leftrightarrow \begin{cases}
(x,y) = (x', y') \\
{x, x'} = \{-1, 1\}, y=y'
\end{cases} 
$$

Es decir aquella que identifica los bordes izquierdo y derecho del rectángulo de manera cruzada.

![](/images/moebius_quotient.png){width=300px}

Sen $\pi: [-1, 1] \times [-1, 1] \rightarrow M$ la proyección al cociente y 

$$
A := \pi([-1, 1] \times \{0\}) \subset M
$$

Claramente $A \cong \mathbb{S}^1$, luego $\Pi_1(A) \cong \mathbb{Z}$.

Veamos que $A$ es retracto de deformación de $M$.

Para eso, definimos $r_0: [-1, 1] \times [-1, 1] \rightarrow [-1, 1] \times \{0 \}$ dada por
$$
r_0(x,y) = (x, 0)
$$

Claramente $r$ es continua y su restricción a $[-1, 1] \times \{0\}$ es la identidad.

Resulta que:

$$
(x,y) R (x', y') \Rightarrow r_0(x,y) R r_0(x',y')
$$

Por lo tanto aplicando el Lema anteriormente probando, obtenemos que existe una única aplicación continua $r: M \rightarrow A$ con $r_0 \circ \pi = \pi \circ r_0$

![](/images/diagrama_moebius.png){width=400px}

$$
\pi(x,y) = [(x,y)] \longrightarrow [(x, 0)] = \pi(x,0) = \pi(r_0(x,y))
$$

Tenemos que $r$ es continua y $r_\vert{A} = Id_A$. Por lo que $r$ es una retracción.

Por otro lado, definimos $H: M \times [0, 1] \rightarrow M$ tal que

$$
H([(x,y), s)]) = [(x, (1-s)y)] = \pi(x, (1-s)y)
$$

Claramente $H$ es continua por ser composición de funcioness continuas y además:

$$
H([(x,y)], 0) = [(x,y)]
$$

$$
H([(x,y)], 1) = [(x,0)] = (i_A \circ r)([(x,y)])
$$

Luego $H: Id_m \simeq i_A \circ r$

Por tanto $A$ es un retracto de deformación de $M$.

Por la conservación de los grupos fundamentales:

$$
\Pi_1(M) \cong \Pi_1(A) \cong \mathbb{Z}
$$
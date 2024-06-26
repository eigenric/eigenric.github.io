Title: Búsqueda en anchura en un Grafo
Date: 2020-05-22
Tags: 

La Búsqueda en Anchura (BFS) es un algoritmo fundamental utilizado en teoría de grafos para explorar y recorrer los nodos de un grafo nivel por nivel. Este método es especialmente útil para encontrar la ruta más corta en términos de número de aristas entre dos nodos en grafos no ponderados.

## Descripción del Algoritmo

El algoritmo BFS utiliza una cola y un conjunto de nodos generados para realizar la búsqueda. Comienza añadiendo el nodo raíz a la cola y al conjunto de nodos generados. Luego, mientras la cola no esté vacía y el nodo actual no sea el nodo destino, se realiza el siguiente procedimiento:

1. Se extrae el primer elemento de la cola y se añade al conjunto de nodos generados.
2. Se generan los hijos del nodo actual a través de las acciones posibles (GiroDerecha, GiroIzquierda y Avanzar).
3. Se actualiza el vector de secuencia de cada nodo hijo con las acciones necesarias para llegar a él desde el nodo actual.
4. Los nodos hijos se añaden a la cola si no están ya en el conjunto de nodos generados, utilizando una función de comparación (ComparaEstados) para verificar su existencia.
5. No se genera un nodo de avance si hay obstáculos delante (muros, etc.).

Una vez que la búsqueda encuentra el nodo destino, el algoritmo finaliza. La progresión de la búsqueda se puede ilustrar con el siguiente ejemplo de un grafo:

```
          1
     /    |    \ 
  2       3      4
 / \     / \    /
5  6   7   8   9
```


La secuencia de exploración sería:

```
[1] -> [2, 3, 4] -> [3, 4, 5, 6]  ->
-> [4, 5, 6, 7, 8] -> [5, 6, 7, 8, 9]
```

Este enfoque garantiza la búsqueda por niveles, explorando todos los nodos de un nivel antes de pasar al siguiente.

## Determinación del Plan de Acciones

Una vez que la búsqueda ha finalizado exitosamente encontrando el nodo destino, el plan de acciones para llegar a él se puede determinar siguiendo las secuencias de acciones almacenadas en cada nodo.

Por ejemplo, si el destino es el nodo 5, podríamos tener las siguientes secuencias:

- Nodo 2: Secuencia = [GiroDerecha]
- Nodo 3: Secuencia = [GiroIzquierda]
- Nodo 4: Secuencia = [Avanzar]
- Nodo 5: Secuencia = [GiroDerecha]

Para ilustrar este proceso, consideremos la siguiente estructura del grafo y las acciones:

```
Nodo 1 -> Nodo 2 [GiroDerecha]
Nodo 2 -> Nodo 5 [GiroDerecha]
```


La secuencia total de acciones para llegar al nodo 5 desde el nodo 1 sería:

```
[GiroDerecha, GiroDerecha]
```


De esta manera, al almacenar y seguir las secuencias de acciones en cada nodo, podemos reconstruir fácilmente el plan de acciones necesario para alcanzar el nodo destino.

## Implementación del Algoritmo en Pseudocódigo

A continuación se presenta una implementación en pseudocódigo del algoritmo BFS:

```pseudo
function BFS(inicio, destino):
    cola = Queue()
    generados = Set()
    inicio.secuencia = []
    cola.enqueue(inicio)
    generados.add(inicio)
    
    while not cola.isEmpty():
        nodo_actual = cola.dequeue()
        
        if nodo_actual == destino:
            return nodo_actual.secuencia
        
        hijos = generar_hijos(nodo_actual)
        
        for hijo in hijos:
            if not generados.contains(hijo):
                hijo.secuencia = nodo_actual.secuencia + [accion_para_llegar_a(hijo)]
                cola.enqueue(hijo)
                generados.add(hijo)
    
    return None
```

## Implementación y Aplicaciones

El BFS es útil para encontrar el camino más corto en grafos no ponderados, y es utilizado en aplicaciones como:

- Redes de pares (P2P) para localizar nodos vecinos.
- Motores de búsqueda y crawlers web para indexar páginas web.
- Sistemas de navegación para encontrar rutas.
- Difusión en redes para propagar información eficientemente.

## Referencias

- [HackerEarth: Breadth First Search (BFS)](https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/){:target="_blank"}
- [Khan Academy: Breadth-First Search](https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/breadth-first-search){:target="_blank"}
- [DevsEnv: Breadth First Search Algorithm](https://www.devsenv.com/algorithms/breadth-first-search){:target="_blank"}
- [Guru99: Breadth First Search (BFS) Algorithm](https://www.guru99.com/breadth-first-search-algorithm.html){:target="_blank"}

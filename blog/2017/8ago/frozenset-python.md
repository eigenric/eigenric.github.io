Title: Tipo de datos Frozenset  - Python
Date: 2017-08-14
Tags: python, tipos

He descubierto un nuevo tipo de conjunto en python, el `frozenset`. La diferencia
con el conjunto normal tipo `<class 'set'>` es que el `frozenset` es **inmutable**. 

```python
foo = frozenset([1,2,3,4])
foo.add(5)
> AttributeError: 'frozenset' object has no attribute 'add'

foo.remove(1)
> AttributeError: 'frozenset' object has no attribute 'remove'
```

A pesar de que no se pueden modificar, se pueden realizar operaciones de conjuntos tales
como unión, intersección, diferencia, etc.

## Unión

Para realizar la unión de dos `frozenset` se utiliza el operador `|`.

```python
bar = frozenset(1,2,3,4)
foo = frozenset(2,3,4,5,6,7)

bar | foo

> frozenset(1,2,3,4,5,6,7)
```

## Intersección

Para realizar la intersección de dos `frozenset` se utiliza el operador `&`.

```python
bar = frozenset(1,2,3,4)
foo = frozenset(2,3,4,5,6,7)

bar & foo

> frozenset(2,3,4)
```

## Diferencia

Para realizar la diferencia de dos `frozenset` se utiliza el operador `-`.

```python
bar = frozenset(1,2,3,4)
foo = frozenset(2,3,4,5,6,7)

bar - foo

> frozenset(1)
```

Puedes obtener más información en la [Documentación oficial](https://docs.python.org/3/library/stdtypes.html#frozenset){:target="_blank"}.
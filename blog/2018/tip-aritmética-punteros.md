Title: C/C++ Tip - Aritmética de punteros
Date: 2018-03-06
Tags: punteros, c, aritmética

En el lenguaje de programación C, los punteros son variables que almacenan direcciones de memoria.

La aritmética de punteros es una característica que nos permite aplicar ciertos operadores aritméticos enteros (suma, resta, incremento o decremento) a un puntero para producir una nueva dirección de memoria.

Dado algún puntero `ptr`, `ptr + 1` devuelve la dirección del siguiente objeto en memoria (basado en el tipo al que apunta). Así que si `ptr` es un `int*`, y un `int` es de 4 bytes, `ptr + 1` devolverá la dirección de memoria que está 4 bytes después de `ptr`, y `ptr + 2` devolverá la dirección de memoria que está 8 bytes después de `ptr`.

Por ejemplo, si tenemos dos punteros `p` y `q` que apuntan a
posiciones consecutivas de un arreglo, entonces `q - p` es igual a 1.

```c
#include <stdio.h>

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int *p = &a[0];
    int *q = &a[1];

    printf("%d\n", p - q); // -1
    printf("%d\n", q - p); // 1

    return 0;
}
```
Más información en [Geek for Geeks - Pointer Airthmetic ](https://www.geeksforgeeks.org/pointer-arithmetics-in-c-with-examples/){:target="_blank"}
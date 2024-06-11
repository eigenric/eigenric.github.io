Title: Vim Tip - Buscar y remplazar
Date: 2017-09-02
Tags: vim, buscar, remplazar

![Vim](/images/vim.png)

Como comentamos en un [post anterior](/blog/2017/08/una-odisea-de-depuracion-top-down-con-vim), [Vim](https://www.vim.org/){:target=_blank} es un editor de texto potente y versátil muy popular entre los desarrolladores. 

Si alguna vez has necesitado buscar y sustituir texto en un archivo sin interfaz gráfica, Vim tiene una serie de comandos que pueden facilitar esta tarea.

Para sustituir **en todo el archivo**, puedes usar el siguiente comando:

```vim
:%s/foo/bar/g
```

En este comando, `%` significa que la sustitución debe realizarse en todo el archivo. `s` es el comando de sustitución. `foo` es la cadena de texto que Vim buscará, y `bar` es la cadena de texto con la que `foo` será reemplazado. `g` significa que la sustitución debe realizarse globalmente en cada línea, es decir, sustituirá todas las ocurrencias de `foo` y no solo la primera en cada línea.

Si solo quieres sustituir **en la línea actual**, puedes usar este comando:

```vim
:s/foo/bar/g
```

Este comando es similar al anterior, pero sin el `%`, por lo que la sustitución solo se realiza en la línea actual.

Para **distinguir entre mayúsculas y minúsculas**, puedes agregar la opción `i` al final del comando:

```vim
:%s/foo/bar/gi
```

Así, `foo`, `Foo`, `FOO`, etc., serán reemplazados por `bar`.


Finalmente, si deseas **confirmar cada sustitución**, puedes agregar la opción `c` al final del comando:

```vim
:%s/foo/bar/gc
```

Vim te preguntará si deseas sustituir cada ocurrencia de `foo` con `bar`. Puedes responder `y` para confirmar, `n` para omitir o `a` para reemplazar todas las ocurrencias restantes.

Más información sobre los comandos de sustitución de Vim y otras características avanzadas se pueden encontrar en la [documentación oficial](https://vimdoc.sourceforge.net/htmldoc/usr_12.html){:target=_blank} o en [la siguiente wiki](https://vim.fandom.com/wiki/Search_and_replace){:target=_blank}.
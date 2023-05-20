Title: Una odisea de depuración top-down con VIM.
Tags: jrnl, vim 
Date: 2013-08-27

![Jrnl](/images/jrnl.png)

[Jrnl](https://jrnl.sh/en/stable/) es un proyecto que permite a las personas llevar un diario desde la línea de comandos. Proporciona una plataforma segura y fácil de usar para escribir y organizar tus pensamientos, recuerdos y experiencias.

Por otro lado, [Termux](https://termux.com/) es una aplicación de terminal de código abierto para dispositivos Android que permite a los usuarios ejecutar comandos y acceder a un entorno similar a una terminal de Linux en sus dispositivos móviles.

En este post, describiré el proceso que seguí para configurar un número de columnas fijo cuando VIM abriese ficheros de tipo JRNL y así escribir desde el teléfono gracias a termux. Y cómo durante el proceso encontré un bug en una [biblioteca externa que acabé corrigiendo](https://github.com/raimon49/requirements.txt.vim)

Yo utilizaba VIM con mi configuración antigua de `~/.vimrc`, la siguiente línea:

```vim
au BufRead,BufNewFile *.txt setlocal tw=50
```

El problema consistía en que ahora mi `~/.vimrc` venía dado por [Vim-bootstrap](https://vim-bootstrap.com/), un generador de configuraciones de Vim.

Investigando, descubrí un método para ver el fichero en el que una variable en VIM fue asigada por última vez.
 
```vim
:verbose set tw
```
 
Así pues, en nuestro caso es el `vim.vim` del `ftplugin`. Por cierto, para cargar el `.vimrc`sin reiniciar VIM
se puede usar `:so ~/.vim/vimrc` o si se está en el propio archvo `:so %`.

Si no usamos el archivo `~/.vim/vimrc` de *Vim-Bootstrap*, podemos trabajar más facilmente con la depuración de VIM.

Cómo no era capaz de encontrar el fallo, acabé [preguntando en Stackoverflow](https://stackoverflow.com/questions/45905694 execute-a-line-in-vimrc-at-the-end). Donde comuniqué lo que había intentado y cuál era mi hipótesis.

Tuve la suerte de que me respondieran e intenté reproducir sus instruciones:

- Escribo en vimrc


```vim
au BufRead, BufNewFile jrnl*.txt set filetype=jrnl
```

-  Añado en la carpeta  `~/.vim/ftplugin`

```vim
set formatoptions+=t
set textwidth=50
```
   
Entonces, comenté todos los plugins y compruebo que funcionaba sin los plugins de `Vim-bootstrap`. Posteriormente, fui añadiendo uno a uno los plugins para encontrar el que generaba el problema.

**¡Capturado la biblioteca culpable!** El plugin requirements.txt.vim es el encargado de sobreescribir la configuración. Cuando está activo, Vim no llama  `~/.vim/after/ftplugin/jrnl.vim`

Inspeccionando el código de requirements.txt.vim
vemos que la *línea 37* contiene lo siguiente:

```vim
au BufNewFile,BufRead *.{txt,ini} if
s:isRequirementsFile() | set ft=requirements
```

Es decir, que la función `isRequirementsFile()` es
llamada cada vez que se ejecuta un `*.txt.`
  
```vim
function! s:isRequirementsFile()
     let l:filename = expand("%:p")
 
    return Requirements_matched_filename(l:filename)
endfunction
 
function! Requirements_matched_filename(filename)
    if a:filename =~# '\v.*require(ment)?s\.(txt|in)$'
        return 1
    endif

    if a:filename =~# '\vrequire(ment)?s/.*\.(txt|in)$'
        return 1
    endif

    if a:filename =~# '\vconstraints\.(txt|in)$'
        return 1
    endif

    if len(g:requirements#detect_filename_pattern)
        \ && a:filename =~# g:requirements#detect_filename_pattern
         return 1
     endif
 
     return 0
endfunction
```
 
Como vemos, esta función crea una variable `filename` que contiene la ruta completa del archivo. Devuelve el resultado de aplicarle la función `Requirements_matched_filename` a la ruta. Comprobamos que la función `isReq` devolvía 0. Por
lo tanto, el *bug parecía inencontrable...*
 
Fue entonces cuando se me ocurrió la, quizás obvia pero efectiva, idea de [leer la documentación de la sintaxis de vim](https://vimdoc.sourceforge.net/htmldoc/syntax.html) y nos sorprendemos al ver que a la instrucción

```vim
au BufNewFile,BufRead *.{txt,ini} if 
    s:isRequirementsFile() | set ft=requirements
```

**¡le lalta un endif!**

```vim 
au BufNewFile,BufRead *.{txt,ini} if
 s:isRequirementsFile() | set ft=requirements |
endif
```
 
En efecto, la simple ausencia de un `endif` en uno de los plugins de configuración estaba sobreescribiendo nuestra orden.

Luego, me propuse a escribir un Pull Request que fue aceptado inmediatamente.

> **Comentario del futuro:**
   La nueva versión de JRNL abre los archivos en
   formato `.jrnl`. Ahora basta con cambiar el `au BufNewFil` a `*.jrnl` para que
   funcione.
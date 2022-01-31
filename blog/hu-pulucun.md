Title: Hu pulucun
Tags: python, pelican, static, blog
Date: 2013-09-12
Status: Hidden

Nuevo blog gracias a [Pelican](http://www.getpelican.com), un sencillo generador de sitios estáticos escrito en python. ¿Le echas un vistazo?

En Pelican, los posts se pueden escribir con dos lenguajes de marcado ligeros: [ReStructuredText](http://code.nabla.net/es/rest.html) o [Markdown](http://daringfireball.net/projects/markdown/). Cada uno ofrece un estilo distinto como se explica en este artículo: [Markdown vs ReStructuredText](https://jasonstitt.com/markdown-vs-rst-pelican). El diseño del sitio se construye con ayuda del motor de plantillas Jinja2. Procedamos a instalarlo.

## Instalación

Pelican está escrito en Python, por lo que para instalarlo basta con usar pip. Para evitar problemas, podéis usar `pyenv`, `virtualenv`, o `conda`.

```console
$ source activate blog
(blog) $ pip install pelican
```

Una vez instalado pelican, creamos un nuevo proyecto. El comando `pelican-quickstart` nos facilita el trabajo mediante un asistente que nos pregunta por la configuración deseada (nombre del sitio, autor, servidor ftp, etc.). Personalmente, yo activo el Makefile y el Devserver.

Escribamos pues nuestro primer post. Usaremos el lenguaje de marcado `ReStructuredText`.

### post.rst

```restructuredtext
Mi primer post
##############

:date: 2013-09-03 16:28
:slug: first-post
:category: python
:tags: blog, post, first, me, pelican

**ReStructuredText is awesome**
```

Después de guardarlo en `content`, volvemos al directorio raíz y ejecutamos las siguientes órdenes:

```console
$ make html
$ make serve
```

`make html` genera los archivos en la carpeta `output` y `make serve` inicia un pequeño servidor local en localhost:8000 para poder ver nuestro sitio.

Así es como tendrá que quedarnos

![Magnifica imagen de muestra]({static}/images/screenshot.png){width="740px"}

Por defecto se utiliza el tema `notmyidea`, pero puedes [descargar otros](http://pelicanthemes.com) o crear uno (más información en la propia [Documentación de Pelican](http://docs.getpelican.com/en/stable/)).

Hasta aquí el pequeño tutorial de instalación. Un saludo!

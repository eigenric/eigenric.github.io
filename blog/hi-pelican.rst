Hi Pelican
##########

:tags: python, pelican, static, blog

Nuevo blog gracias a Pelican_, un sencillo generador de sitios estáticos
escrito en python. ¿Le echas un vistazo?

.. readmore

En Pelican, los posts se pueden escribir con dos lenguajes de marcado ligeros:
ReStructuredText_ o Markdown_ . Cada uno ofrece un estilo distinto como se explica
en este artíulo: `Markdown vs Pelican`__.
El diseño del sitio se construye con ayuda del motor de plantillas Jinja2.
Procedamos a instalarlo.

.. readmore

.. _Pelican: http://www.getpelican.com
.. _ReStructuredText: http://code.nabla.net/es/rest.html
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _Jinja2: http://jinja.pocoo.org/

__ https://jasonstitt.com/markdown-vs-rst-pelican

Instalación
-----------

Pelican está escrito en Python, por lo que para instalarlo basta con usar pip.
Para evitar problemas, podéis usar ``pyenv``, ``virtualenv``, o ``conda``.

.. code-block:: console

    $ source activate blog
    (blog) $ pip install pelican

Una vez, instalado pelican, creamos un nuevo proyecto. El comando ``pelican-quickstart`` nos facilita el trabajo mediante un asistente que nos
pregunta por la configuración deseada (nombre del sitio, autor, servidor ftp,
etc.). Personalmente, yo activo el Makefile y el Devserver.


Escribamos pues nuestro primer post. Usaremos el lenguaje de marcado
``ReStructuredText``.

post.rst
''''''''

.. code-block:: restructuredtext

    Mi primer post
    ##############

    :date: 2013-09-03 16:28
    :slug: first-post
    :category: python
    :tags: blog, post, first, me, pelican

    **ReStructuredText is awesome**

Después de guardarlo en ``content``, volvemos al directorio raíz y ejecutamos las
siguientes órdenes:

.. code-block:: console

    $ make html
    $ make serve

``make html`` genera los archivos en la carpeta ``output`` y ``make serve`` inicia un
pequeño servidor local en localhost:8000 para poder ver nuestro sitio.

Así es como tendrá que quedarnos

.. image:: |filename|/images/screenshot.png
    :width: 740px
    :alt: Magnifica imagen de muestra


Por defecto se utiliza el tema ``notmyidea``, pero puedes `descargar otros`__
o crear uno (más información en la propia `Documentación de Pelican`__)

__ http://pelicanthemes.com
__ http://docs.getpelican.com/en/stable/


Hasta aquí el pequeño tutorial de instalación. Un saludo!

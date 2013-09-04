Hi Pelican
#############

:slug: hi-pelican
:tags: python, pelican, static, blog

**Los sitios estáticos han muerto**

.. image:: |filename|/images/pelican.png
    :width: 201px
    :height: 44px

**¡Vivan los sitios estáticos!**


Nuevo blog, éste, ha sido creado gracias a Pelican_, un simple generador de
contenido blogs estáticos. Los posts se escriben con lenguajes de marcado ligeros,
como ReStructuredText_ o Markdown_, y el sitio, con ayuda del motor de
plantillas Jinja2_

.. _Pelican: http://www.getpelican.com
.. _ReStructuredText: http://code.nabla.net/es/rest.html
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _Jinja2: http://jinja.pocoo.org/

¿Quieres probarlo? ¡Sigue leyendo!

Instalación
-----------

Pelican está escrito en Python, basta con usar *pip*, el gestor de paquetes de
python, para instalarlo. Pero antes, os recomiendo usar virtualenv para evitar errores de
dependencias entre paquetes.


.. code-block:: Bash Session
    
    $ sudo apt-get install python-virtualenv
    $ mkdir blog; cd blog
    $ virtualenv --no-site-packages --distribute env
    $ source env/bin/activate
    $ pip install pelican

Bien, ya tenemos instalado pelican. Ahora crearemos un nuevo proyecto gracias a
la orden *pelican-quickstart*. Seguidamente aparecerá un asistente para
configurarlo (nombre del sitio, autor, ftp server).

Activad el *Makefile* y el *Auto-reload & SimpleHTTP*. **DRY!**.


Escribamos pues nuestro primer post. Usaremos el lenguaje de marcado
*ReStructuredText*.

post.rst
''''''''

.. code-block:: ReST

    Mi primer post
    ##############

    :date: 2013-09-03 16:28
    :slug: first-post
    :category: python
    :tags: blog, post, first, me, pelican

    **ReStructuredText is awesome**

Después de guardarlo en *content*, volvemos al directorio raíz y ejecutamos las
siguientes órdenes:

.. code-block:: Bash Session
    
    $ make html
    $ make serve

*make html* genera los archivos en la carpeta *output* y *make serve* inicia un
pequeño servidor local en localhost:8000 para poder ver nuestro sitio.

Así es como tendría que quedarnos

.. image:: |filename|/images/pelican-blog.png
    :width: 760
    :height: 420


Por defecto se utilizar el tema *notmyidea*, pero puedes descargar otros en
http://pelicanthemes.com o crear uno -> pelican-docs.pdf_.


.. _pelican-docs.pdf: https://www.dropbox.com/s/orvvnkwentc5ptb/pelican.pdf

Pues esto es todo amigos, gracias por leer el post, ¡hasta otra! :)

YounGeek 
########

Repositorio para pruebas :)

* Probando como funciona esto de git, usando sublimegit en Sublime Text 3.
* Leyendo Git Magic.
* Viendo videotutoriales
Editado el README para la version 0.2

Código
******

.. code-block:: python

	from django.caca import caca2

	def vista_caca(response):

		caca_para_ti = "Caca para ti y para mi"

		return render_to_response('plantilla.html', **locals())
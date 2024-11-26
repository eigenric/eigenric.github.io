Title: Proceso de aprendizaje - Autociges
Date: 2017-09-18
Tags: 

## El desafío

El problema inicial era claro: **"No sabemos cuándo habrá cita en secretaría"**.
Para solucionarlo, decidimos automatizar el proceso mediante un **script en
Selenium**.

El objetivo principal del proyecto no era crear un código abstracto o versátil, sino lograr que el mecanismo funcionara lo más rápido posible.

### Primeros intentos

La primera versión funcional del script fue completada a las 19:15, pero los problemas surgieron al intentar ponerlo en producción.

Nuestra primera idea fue desplegar la aplicación en **Heroku**, siguiendo el desarrollo de **Inemonitor**. Pensábamos que, con escribir el script y usar un **Scheduler**, podríamos ejecutar el proceso periódicamente.

Sin embargo, nos dimos cuenta de que, al usar Selenium, son necesarias dos cosas:

- El binario del navegador utilizado (en este caso, **Google Chrome**).
- El binario del **webdriver** (en este caso, **chromedriver**).

### Desafíos con Heroku

En un primer intento, usamos los buildpacks `google-chrome-heroku-buildpack` y `chromedriver-heroku-buildpack`, pero surgieron errores relacionados con el intérprete de Python. El problema era que Heroku no detectaba correctamente la aplicación Python, como lo había hecho en otras ocasiones.

Así que, añadimos el **buildpack de Python-heroku** y especificamos la versión de Python en el archivo `runtime.txt`: `python-3.6.2`


Subimos nuevamente la aplicación, pero aunque esta vez Heroku detectaba Python e instalaba las dependencias del `requirements.txt`, el programa seguía sin funcionar.

### Decisión de cambiar a DigitalOcean

Frustrados con los problemas en Heroku, decidimos cambiar de estrategia y desplegar la aplicación en **DigitalOcean**, gracias a unos maravillosos **50€ gratis** que Github nos había proporcionado.

Siguiendo los tutoriales de **Jonathan Soma** para crear y configurar un servidor en DigitalOcean:

- [Creando un servidor](http://jonathansoma.com/lede/algorithms-2017/servers/creating/)
- [Configurando el servidor](http://jonathansoma.com/lede/algorithms-2017/servers/setting-up/)

Nos encontramos con un **servidor Ubuntu** accesible a través de SSH, y lo mejor de todo: ¡**increíblemente rápido**!

### Subiendo el proyecto a GitHub

Una vez configurado el servidor, decidimos subir el proyecto a un repositorio privado en GitHub, lo que también nos permitiría aumentar nuestras contribuciones. Para crear el repositorio desde la línea de comandos, usamos el siguiente comando:

```bash
curl -u 'pwaqo' https://api.github.com/user/repos -d '{"name":"autociges","private": "true"}'
```

Esto nos solicitó usuario y contraseña, ya que estábamos creando un repositorio privado.

### Instalación de dependencias en DigitalOcean
En el servidor de DigitalOcean, seguimos los pasos para instalar Python 3.6 compilado desde el código fuente, siguiendo este tutorial:

### Instalar Python 3.6 en Ubuntu

Una vez instalado, procedimos a instalar las dependencias del proyecto, aunque nos preocupaba que se instalaran directamente en el sistema y no en un virtualenv (pero eso lo resolveríamos más tarde).

### También instalamos Google Chrome y chromedriver en el servidor.

Uso de pyvirtualdisplay para Selenium
Un desafío importante con Selenium es que requiere de una pantalla para funcionar, ya que controla un programa gráfico. Para solucionar esto, usamos pyvirtualdisplay, que permite crear una pantalla virtual. El código para configurar la pantalla virtual es el siguiente:

```python
from pyvirtualdisplay import Display

display = Display(visible=0, size=(x, y))
display.start()
```

Sin embargo, al utilizar una resolución de size=(800, 600), el script dio un error al intentar hacer clic en los elementos de la página. La solución fue aumentar la resolución a size=(1920, 1200) para que coincidiera con la configuración del driver de Chrome:

```python
driver.set_window_size(1920, 1200)
```

También agregamos la opción --no-sandbox para evitar otros posibles errores:

```python
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
chrome = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
Gestión de procesos de Google Chrome
Al ejecutar el script, nos dimos cuenta de que los procesos de Google Chrome no se cerraban correctamente, lo que generaba procesos huérfanos. Para solucionarlo, usamos los siguientes comandos para verificar y terminar los procesos de Chrome:
```

```bash
ps --sort -rss -eo rss,pid,command | head
ps -ef | grep chrome | grep -v grep | awk '{print $2}' | xargs -r kill -9
```

Además, incluimos los siguientes comandos en el script para cerrar correctamente el navegador y detener la pantalla virtual al finalizar:

```python
driver.quit()  # Cierra todas las instancias del navegador
display.stop() # Detiene la pantalla virtual
```

## Ejecución periódica con Cron
El siguiente paso fue configurar el script para que se ejecutara periódicamente, similar al Scheduler de Heroku. Usamos el siguiente tutorial para configurar el cronjob:

## Configurar cronjob en DigitalOcean

Para ejecutar el script cada hora, añadimos la siguiente línea en el archivo crontab con crontab -e:

```
0 * * * * /usr/local/bin/python3.6 ~/autociges/autociges.py > ~/autociges/autociges.log
```

Sin embargo, al principio nos dimos cuenta de que python3.6 no era reconocido por cron. La solución fue usar la ruta absoluta de python3.6:

`/usr/local/bin/python3.6 ~/autociges/autociges.py > ~/autociges/autociges.log`

Solucionando problemas con el archivo citas.json
Nos encontramos con otro problema: el archivo citas.json no se estaba creando en la ubicación correcta. Para solucionarlo, utilizamos el siguiente código para obtener la ruta absoluta del archivo:

```python
import os
from pathlib import Path

current_dir = os.path.abspath(os.path.join(__file__, '..'))
citas_config = Path(os.path.join(current_dir, 'citas.json'))
```

### Configuración de variables de entorno
Otro problema fue que Python 3.6 no estaba obteniendo las variables de entorno correctas al ejecutarse desde cron. Para solucionarlo, añadimos las variables de entorno en el archivo /etc/environment para que se definieran a nivel global:

```bash
CIGES_USERNAME=""
CIGES_PASSWORD=""
```

### Ejecución final

Finalmente, después de todos los ajustes, logramos que el script se ejecutara correctamente a través de cron. Para comprobar su funcionamiento, configuramos el cronjob para que se ejecutara cada 2 minutos:

```
*/2 * * * * /usr/local/bin/python3.6 /root/autociges.py > /root/autociges.log
```

¡Y funcionó!

### Conclusión

A pesar de los numerosos obstáculos, logramos implementar y desplegar el script Autociges de manera exitosa en DigitalOcean, resolviendo problemas relacionados con la instalación de dependencias, la ejecución de Selenium en un servidor sin interfaz gráfica y la configuración de cronjobs para la ejecución periódica del script.
Title: Dockerización de un frontend en Express
Date: 2022-12-16
Tags: 
Status: Hidden

A partir de la API REST construida con Flask encapsulada en un contenedor docker
cuyo build es el dockerfile de /app el cual ejecuta docker compose que ejecuta el servidor flask en `localhost:8000/api/recipes` y devuelve un json,

Necesito construir un frontend en Javascript que se acople a esta api
(obtenga los objetos via llamada Ajax o fetch ).

## Pasos dados

A medida que hemos investigado por internet hemos concluido con un intento
satisfactorio de `hola mundo`via express con lo siguientes:

Creación de una carpeta frontent separada de `app`.  

Un Servicio especializado en `docker compose` para el frontend llamado frontend
y con las siguientes características:

`build: ./frontend` se encarga de construir el contenedor via el `dockerfile` de la
carpeta `frontend`.

Depende de `app` pues requiere que la api este funcionando (que requiere de mongo)
para hacer llamadas a esta.

`Volúmenes: ./frontend/frontend`

Esto hace que la carpeta `./frontend` se copie a la raíz del contenedor en
frontend donde estarán los archivos js index que corresponden al frontend

Tendremos que tratar con boostrap de nuevo para hacer una single app vía
modals lo más sencillo posible.

## Problemas:

- El puerto 5000 colapsa con la api flask asi que lo tendremos en el puerto 3000.
- Fallo de nodejs al buscar express como módulo

Intuición: alguna ruta relacionada con la instalación de express no queda clara.
Esto viene de `require('express')`

Idea del orden de ejecución:

Se ejecuta docker compose teniendo a frontend como servicio el cual se construye
llamado a su `dockerfile.`

El dockerfile requiere de la imagen de node 19
como viene en el txt:

1. Se crea una carpeta node_modules en `/frontend`
del contenedor y se le da permisos para el grupo node
a todo `/frontend`
`/frontend` refiere al volumen el cual deberia
haberse copiado integramente de la carpeta
frontend conteniendo los archivos:

```
- index.html
- package.json
- server.js
```

El fundamental es el archivo `server.js` el cual
iniciaria el servidor express.
`
Suponiendo que los archivos estan en `/frontend` el
contenedor
Se habria creado ademas una carpeta `node_module``

Luego se copia``package*.json` a esta carpeta 
 
Hemos conseguido que se renderice quitando el tema de los permisos y siguiendo
la mismas directrices
que el `Dockerfile`eneral a todo `/frontend.`

![Dockerizacion de un frontend en Express](/images/dockerizacion-express.png)
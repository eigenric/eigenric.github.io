Title: Vista en Flask para consultar a MongoDB
Date: 2022-10-28


En el contexto de la asignatura **Desarrollo de Aplicaciones para Internet (DAI)**, se nos ha pedido realizar una pequeña aplicación web que consulte una base de datos de recetas de cócteles. La base de datos se almacena en **MongoDB**, y la aplicación web se construye con **Flask** en la primera versión, y con **Flask-RESTful** en la segunda. Este artículo detalla cómo crear una vista que permita consultar las recetas que contengan un ingrediente específico, utilizando Flask y MongoDB.

## Introducción a Flask y MongoDB

**Flask** es un framework web minimalista para Python, que permite desarrollar aplicaciones web rápidamente. Es conocido por su simplicidad y flexibilidad, lo que lo convierte en una opción ideal para proyectos pequeños o medianos. Flask sigue el principio de "menos es más", lo que significa que no impone una estructura rígida a los desarrolladores, permitiéndoles tomar decisiones según las necesidades del proyecto.

Flask se integra bien con otras herramientas como bases de datos, plantillas HTML, y sistemas de autenticación, entre otros. La simplicidad de Flask no compromete la capacidad de escalar a aplicaciones más complejas, gracias a su extenso ecosistema de extensiones.

### ¿Qué es MongoDB?

**MongoDB** es una base de datos NoSQL orientada a documentos, lo que significa que almacena los datos en forma de documentos JSON (o BSON, que es una versión binaria de JSON). En lugar de utilizar las tablas y filas de una base de datos relacional, MongoDB organiza la información en colecciones y documentos, lo que la hace extremadamente flexible y adecuada para manejar grandes cantidades de datos no estructurados o semi-estructurados.

Una de las ventajas de MongoDB es su capacidad de almacenar arrays y documentos anidados, lo cual se adapta perfectamente al tipo de datos que manejan aplicaciones web modernas, como listas de ingredientes para recetas de cócteles.

### Ejemplo de Aplicación: Consulta de Recetas con Ingredientes Específicos

En este caso, queremos crear una vista que permita consultar todas las recetas que contengan un ingrediente en particular (como "vodka"). Para lograr esto, Flask servirá como la interfaz web, mientras que MongoDB contendrá la base de datos con las recetas y sus ingredientes.

## Código de la Vista en Flask para Consultar MongoDB

El siguiente código Python implementa una vista en Flask que permite consultar las recetas que contengan cierto ingrediente, pasando el nombre del ingrediente como parámetro en la URL:

```python
from flask import Flask, Response
from bson.json_util import dumps
from pymongo import MongoClient

app = Flask(__name__)

# Conexión a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.cocktails_db

@app.route("/recetas_con/<bebida>")
def mongo_recetas_con(bebida):
    """Devuelve las recetas con cierta bebida en sus ingredientes"""

    # Realiza la consulta en MongoDB buscando en el campo ingredients.name
    recetas_con_bebida = db.recipes.find({
        "ingredients.name": {"$eq": str(bebida) }
    })

    # Procesa los resultados de la consulta
    lista_recetas = []
    for receta in recetas_con_bebida:
        app.logger.debug(receta)
        lista_recetas.append(receta)

    # Construye la respuesta JSON
    response = {
        "len": len(lista_recetas),
        "data": lista_recetas
    }

    # Convierte a JSON y retorna la respuesta
    resJson = dumps(response)
    return Response(resJson, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)
```


## Resultado Final

Al realizar una petición a la siguiente url [](http://localhost:5000/recetas_con/vodka), el usuario puede consultar todas las recetas que contengan vodka, obteniendo una respuesta en formato JSON con la información de las recetas encontradas.

```json
{
  "len": 2,
  "data": [
    {
      "_id": "62d7a4ff3b31a95b2e7f7e4e",
      "name": "Bloody Mary",
      "ingredients": [
        {"name": "vodka", "amount": "50ml"},
        {"name": "tomato juice", "amount": "100ml"},
        {"name": "lemon juice", "amount": "10ml"}
      ]
    },
    {
      "_id": "62d7a4ff3b31a95b2e7f7e4f",
      "name": "Moscow Mule",
      "ingredients": [
        {"name": "vodka", "amount": "50ml"},
        {"name": "ginger beer", "amount": "150ml"},
        {"name": "lime juice", "amount": "10ml"}
      ]
    }
  ]
}
```
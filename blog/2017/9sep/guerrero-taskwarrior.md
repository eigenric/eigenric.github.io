Title: Sé un guerrero de la productividad con Taskwarrior (I)
Date: 2017-09-01
Tags: productividad, taskwarrior, gestión de tareas

Taskwarrior es una herramienta de línea de comandos para la gestión de tareas, diseñada para ser potente, flexible y personalizable. Ideal para usuarios que prefieren trabajar en terminal, permite capturar, rastrear y organizar tareas de manera eficiente.

# Ejemplos de Uso

- Añadir una tarea:

```shell
$ task add "Leer el capítulo 1 del libro X"
```

- Añadir una tarea con proyecto:

```shell
$ task add "Escribir introducción del blog" project:blog
```

- Listar tareas:

```shell
$ task list
```

Listar tareas de un proyecto:

```shell
$ task project:blog list
```

- Completar una tarea:

```shell
$ task 1 done
```

- Modificar una tarea:

```shell
$ task 1 modify priority:H
```

(También se puede usar `task x mod`)

- Añadir una tarea con fecha de vencimiento y etiqueta:

```shell
$ task add "Comprar leche" due:tomorrow +compras
```

- Filtrar tareas por etiqueta:

```shell
task +compras list
```

![Taskwarrior](/images/taskwarrior.png)


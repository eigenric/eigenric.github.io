Title: Sé un guerrero de la productividad con Taskwarrior
Date: 2017-09-01
Tags: productividad, taskwarrior, tareas

En el vertiginoso mundo de hoy, la gestión del tiempo y las tareas se ha convertido en una habilidad esencial para alcanzar tus objetivos. Afortunadamente, existen herramientas como Taskwarrior que están diseñadas para ayudarnos a organizar nuestras responsabilidades diarias y maximizar nuestra productividad.

## ¿Qué es Taskwarrior?

[Taskwarrior](https://taskwarrior.org/){:target=_blank} es un potente administrador de tareas de línea de comandos que te permite mantener un registro de tus actividades, establecer plazos, priorizar tareas y mucho más. Su enfoque minimalista lo hace ideal para usuarios que prefieren la eficiencia sobre la complejidad.

## Características

- **Interfaz de línea de comandos (CLI):** Aunque puede parecer intimidante al principio, la interfaz de línea de comandos de Taskwarrior es sorprendentemente intuitiva una vez que te acostumbras a ella. Te permite agregar, editar y completar tareas con comandos simples y rápidos.

- **Gestión flexible de tareas:** Taskwarrior te permite etiquetar, priorizar y organizar tus tareas de acuerdo con tus necesidades específicas. Puedes asignar etiquetas a tus tareas para categorizarlas y filtrarlas fácilmente más tarde.

- **Plazos y recordatorios:** Con Taskwarrior, nunca más olvidarás una fecha límite importante. Puedes establecer plazos para tus tareas y recibir recordatorios automáticos para asegurarte de cumplir con tus compromisos a tiempo.

- **Integraciones:** Taskwarrior se integra fácilmente con otras herramientas y servicios, lo que te permite sincronizar tus tareas con calendarios, correos electrónicos y más. Esta funcionalidad te permite tener una visión más completa de tu carga de trabajo y maximizar tu eficiencia.

# Ejemplos Básicos de Uso

Añadir una tarea:

```shell
$ task add "Leer el capítulo 1 del libro de historia"
```

Añadir una tarea con proyecto:

```shell
$ task add "Escribir post taskwarrior" project:blog
```

Listar tareas:

```shell
$ task list
```

Listar tareas de un proyecto:

```shell
$ task project:blog list
```

<a href="/images/taskwarrior-1.png" target="_blank"><img src="/images/taskwarrior.png" alt="Taskwarrior example" width="100%" height="100%"></a>

Completar una tarea:

```shell
$ task 1 done
```

Modificar una tarea:

```shell
$ task 1 modify priority:H
```

(También se puede usar `task x mod`)

Añadir una tarea con fecha de vencimiento y etiqueta:

```shell
$ task add "Comprar leche" due:tomorrow +compras
```

Filtrar tareas por etiqueta:

```shell
task +compras list
```

<a href="/images/taskwarrior-2.png" target="_blank"><img src="/images/taskwarrior-2.png" alt="Taskwarrior example" width="100%" height="100%"></a>

Para desbloquear todo el potencial de Taskwarrior, sugerimos revisar la
[documentación oficial](https://taskwarrior.org/docs/){:target=_blank}. Encontrarás una guía completa que te ayudará a aprovechar al máximo esta herramienta.
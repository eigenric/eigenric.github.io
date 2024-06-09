Title: Sé un guerrero de la productividad con Taskwarrior
Date: 2017-09-01
Tags: productividad, taskwarrior, tareas

En el vertiginoso mundo de hoy, la gestión del tiempo y las tareas se ha convertido en una habilidad esencial para alcanzar tus objetivos. 

Afortunadamente, existen herramientas como Taskwarrior que están diseñadas para ayudarnos a organizar nuestras responsabilidades diarias y maximizar nuestra productividad.

## ¿Qué es Taskwarrior?

[Taskwarrior](https://taskwarrior.org/){:target=_blank} es un potente administrador de tareas de línea de comandos que te permite mantener un registro de tus actividades, establecer plazos, priorizar tareas y mucho más. Su enfoque minimalista lo hace ideal para usuarios que prefieren la eficiencia sobre la complejidad.

## Características

- **Interfaz de línea de comandos (CLI):** Su interfaz de usuario basada en comandos es intuitiva una vez que te acostumbras, facilitando la agregación, edición y finalización de tareas.

- **Gestión flexible de tareas:** Permite etiquetar, priorizar y organizar tareas según tus necesidades, ofreciendo una personalización completa.

- **Plazos y recordatorios:** No más fechas límite olvidadas; Taskwarrior te permite establecer plazos y recibir recordatorios automáticos para mantenerte en el buen camino.

- **Integraciones:** Se integra con otras herramientas y servicios, como calendarios y correos electrónicos, para sincronizar tareas y maximizar la eficiencia.

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

Notemos como taskwarrior es capaz de asignar prioridades a las tareas. En este caso, la tarea 1 ha sido marcada con prioridad alta. Esto permite a los usuarios completar las tareas más importantes primero.

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

## Referencias

- [La Mirada del Replicante - Administra tu lista de tareas con Taskwarrior](https://lamiradadelreplicante.com/2018/04/30/administra-tu-lista-de-tareas-con-taskwarrior/){:target=_blank}
- [DebianHackers - Taskwarrior: Un guerrero en tu terminal](https://debianhackers.net/taskwarrior-un-guerrero-en-tu-terminal/){:target=_blank}
- [Documentación oficial](https://taskwarrior.org/docs/){:target=_blank}.
- [Taskwarrior en GitHub](https://github.com/GothenburgBitFactory/taskwarrior){:target=_blank}
Title: Sé un guerrero de la productividad con Taskwarrior
Date: 2017-09-01
Tags: productividad, taskwarrior, tareas

[Taskwarrior](https://taskwarrior.org/){:target=_blank} es una herramienta de línea de comandos para la gestión de tareas, diseñada para ser potente, flexible y personalizable. Ideal para usuarios que prefieren trabajar en terminal, permite capturar, rastrear y organizar tareas de manera eficiente.

# Características

- **Flexibilidad**: Permite crear, editar y organizar tareas de manera flexible, asignando fechas de vencimiento, prioridades, etiquetas y notas.

- **Interfaz de Línea de Comandos**: no requiere de altos recursos, pudiendo trabajar offline y sincronizar tareas posteriormente.

- **Personalización:** Es altamente personalizable, permitiendo configurar listas de proyectos, contextos y etiquetas según las necesidades individuales.

- **Gestión de Proyectos:** Organiza tareas en proyectos para un seguimiento claro de actividades, asignando tareas específicas a cada proyecto.

- **Priorización y Filtrado:** Permite priorizar y filtrar tareas según diversos criterios, como fecha de vencimiento, prioridad y etiquetas.

- **Recordatorios y Alertas:** Configura recordatorios y alertas para no perder plazos importantes.

- **Integración:**  Se integra con otras herramientas y servicios mediante complementos y scripts personalizados.

# Ejemplos Básicos de Uso

Añadir una tarea:

```shell
$ task add "Leer el capítulo 1 del libro de historia"
```

Añadir una tarea con proyecto:

```shell
$ task add "Escribir post sobre taskwarriorblog" project:blog
```

Listar tareas:

```shell
$ task list
```

Listar tareas de un proyecto:

```shell
$ task project:blog list
```

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

![Taskwarrior](/images/taskwarrior.png)

Para desbloquear todo el potencial de Taskwarrior, sugerimos revisar la
[documentación oficial](https://taskwarrior.org/docs/){:target=_blank}. Encontrarás una guía completa que te ayudará a aprovechar al máximo esta herramienta.
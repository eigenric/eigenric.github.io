Title: Restaurar Arch Linux tras instalación fallida.
Date: 2019-03-13
Tags: 

En ocasiones, después de una instalación fallida de paquetes, el sistema operativo Arch Linux o Manjaro puede no arrancar correctamente. Afortunadamente, es posible solucionar estos problemas y restaurar el sistema utilizando el GRUB y algunos comandos básicos. A continuación, se detallan los pasos para realizar esta recuperación.

## Acceder al Sistema mediante GRUB

1. Reinicia tu computadora y pulsa `F12` repetidamente antes de que el sistema inicie.
2. Selecciona la opción de arranque de Arch Linux Linux y sigue pulsando `F12` hasta acceder al GRUB.
3. En el menú de GRUB, selecciona la opción de arranque que deseas modificar y pulsa `e` para editarla.
4. Añade un `3` al final de la línea que comienza con `linux`, que es la línea que carga el núcleo. Esto permitirá acceder al sistema operativo vía terminal.
5. Guarda los cambios pulsando `Ctrl+x`.

## Actualizar el Sistema

Una vez que hayas accedido al sistema vía terminal, actualiza el sistema con el siguiente comando:

```shell
$ sudo pacman -Syu
```

## Manejo de Librerías Truncadas

En el caso de que una librería `.so` esté truncada, puedes eliminarla y reinstalarla. Además, es recomendable eliminar el directorio de caché asociado en `/var/lib/pacman/local/nombre-paquete`.

## Eliminar el Archivo de Bloqueo de Pacman

Si pacman está bloqueado, elimina el archivo de bloqueo con el siguiente comando:

```shell
$ sudo rm /var/lib/pacman/db.lck
```

Siguiendo estos pasos, deberías poder restaurar tu sistema Arch Linux y resolver los problemas causados por instalaciones fallidas de paquetes.
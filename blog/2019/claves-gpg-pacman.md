Title: Como resolver errores de claves GPG - Pacman
Date: 2019-03-04
Tags: pacman, linux, gpg, arch, manjaro

Durante la instalación de programas en Arch Linux o Manjaro, es posible que te enfrentes a errores relacionados con la aceptación de claves GPG. Estos errores pueden interrumpir la instalación y son causados por claves no confiables o no encontradas en el sistema.

## Ejemplo de Error de Clave GPG

Imaginemos que intentas instalar el paquete `example-package` usando `pacman` y encuentras el siguiente error:

```shell
error: example-package: signature from 
"John Doe <johndoe@example.com>" is unknown trust error: 
failed to commit  transaction (invalid or corrupted package
(PGP signature))
Errors occurred, no packages were upgraded.
```

El mensaje de error indica que la firma del paquete example-package es de una clave GPG que no está reconocida como confiable. El ID de la clave problemática es 12345678.

## Resolución del Error

Para resolver este problema, sigue estos pasos:

Ejecuta el siguiente comando, reemplazando 12345678 con el ID de la clave problemática que se mostró en el mensaje de error:

```shell
$ gpg --recv-key 12345678
```

Este comando descargará y añadirá la clave GPG a tu sistema, permitiendo que la instalación del programa continúe sin problemas.

Una vez que la clave se haya descargado correctamente, intenta instalar el paquete de nuevo:

```shell
$ sudo pacman -S example-package
```

Siguiendo estos pasos, deberías poder resolver el error de clave GPG y completar la instalación del paquete sin inconvenientes.
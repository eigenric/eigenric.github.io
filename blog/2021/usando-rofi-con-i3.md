Title: Configurando i3-gaps y rofi con i3 en Arch Linux
Date: 2021-02-07
Tags: arch, i3, rofi, polybar

En este artículo, exploraremos cómo configurar un entorno de escritorio minimalista y altamente personalizable utilizando i3-gaps, rofi y polybar en Arch Linux. Estas herramientas te permitirán crear un espacio de trabajo eficiente y visualmente atractivo, adaptado a tus necesidades específicas.

`i3-gaps` es una versión modificada del gestor de ventanas i3, que añade la capacidad de crear espacios entre las ventanas. `Rofi` es un lanzador de aplicaciones versátil y personalizable, mientras que `polybar` es una barra de estado moderna y configurable.

A lo largo de esta guía, aprenderás a instalar y configurar estos componentes para crear un entorno de escritorio único y funcional en Arch Linux. ¡Comencemos!

## Instalación de polybar

Puedes seguir [esta guía](https://nocin.eu/mint-install-polybar-on-linux-mint-19-2-cinnamon/){:target=_blank} para instalar polybar. Asegúrate de corregir python3-xcbgen y de instalar la dependencia adicional libjsoncpp-dev y python3-sphinx:

```bash
$ sudo pacman -S libjsoncpp-dev python3-sphinx
```

## Configurando i3-gaps

Para evitar problemas con i3-gaps, puedes seguir los pasos detallados en [esta guía](https://github.com/PhalanxHead/i3-gaps_MintInstaller){:target=_blank}. Es recomendable purgar completamente i3 y luego instalar i3-gaps según [este tutorial](https://lottalinuxlinks.com/how-to-build-and-install-i3-gaps-on-debian/){:target=_blank}. 
Recuerda que utilizarán `meson` en lugar de `autoreconf`.

## Integración de rofi con i3

Para integrar rofi con i3, primero asegúrate de tenerlo instalado en tu sistema. Puedes hacerlo ejecutando el siguiente comando en tu terminal:

```bash
$ sudo pacman -S rofi
```

Una vez instalado, puedes personalizar la configuración de rofi y su apariencia para que se ajuste a tu entorno i3. Rofi ofrece muchas opciones de configuración que puedes explorar según tus preferencias y necesidades.
Title: Configurando i3-gaps y rofi con i3 en Arch Linux
Date: 2021-02-07
Tags: arch, i3, rofi, polybar

He encontrado una página de temas para i3 que me ha parecido interesante. Aunque no es muy didáctica para sustituir, te guía para instalar i3-wm, polybar, rofi y stylish.

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
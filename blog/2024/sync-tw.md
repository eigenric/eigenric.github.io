Title: Sincronizar Taskwarrior con rclone
Date: 2024-11-08
Tags: taskwarrior, rclone, sync, termux

![Termux Taskwarrior](/images/termux.jpg){width="300px"}

En este post describiré el proceso que seguí para tener funcionando taskwarrior
en Termux (Android) y que sea sincronizable en un Laptop vía Dropbox.

En primer lugar, es necesario instalar taskwarrior y timewarrior en Termux

```bash
$ pkg install taskwarrior
$ pkg install timewarrior
```

Luego instalaremos `rclone` para sincronizar con Dropbox.

```bash
$ pkg install rclone
```

## Configuración de rclone

Para configurar `rclone` necesitas registrar una aplicación en Dropbox for developers y 
guardar los valores de `app_id`, `app_secret` y `access_token`. 

Además, hay que añadir las siguientes `Redirect URIs`

![Dropbox App](/images/dropbox_app.png)

Luego ejecutamos

```bash
$ rclone config
```

Sigues los pasos, para añadir un nuevo servicio llamado "Dropbox" del tipo 12 de la lista y
le pasas las `app_id`, `app_secret` guardadas. En configuración extra, sólo hace falta añadir 
el generado `access_token`. El resto lo dejas en blanco (default).


Así, crearemos un script llamado `syncw.sh` que sincronice la carpeta `.task` correspondiente a la base de datos de tareas y la carpeta `timewarrior` en Dropbox.

`pushw.sh``

```bash
#!/data/data/com.termux/files/usr/bin/bash

# Rutas de sincronización
LOCAL_TIMEWARRIOR_PATH="/data/data/com.termux/files/home/.local/share/timewarrior"
DROPBOX_TIMEWARRIOR_PATH="Dropbox:/timewarrior"
LOCAL_TASK_PATH="/data/data/com.termux/files/home/.task/taskchampion.sqlite3"
DROPBOX_TASK_PATH="Dropbox:/.task"

# Sincronización en ambos sentidos para Timewarrior
rclone sync "$LOCAL_TIMEWARRIOR_PATH" "$DROPBOX_TIMEWARRIOR_PATH"

# Sincronización en ambos sentidos para Taskwarrior
rclone sync "$LOCAL_TASK_PATH" "$DROPBOX_TASK_PATH"
```

`pullw.sh`

```bash
#!/data/data/com.termux/files/usr/bin/bash

# Rutas de sincronización
LOCAL_TIMEWARRIOR_PATH="/data/data/com.termux/files/home/.local/share/timewarrior"
DROPBOX_TIMEWARRIOR_PATH="Dropbox:/timewarrior"
LOCAL_TASK_PATH="/data/data/com.termux/files/home/.task/taskchampion.sqlite3"
DROPBOX_TASK_PATH="Dropbox:/.task"

rclone sync "$DROPBOX_TIMEWARRIOR_PATH" "$LOCAL_TIMEWARRIOR_PATH"
rclone sync "$DROPBOX_TASK_PATH" "$LOCAL_TASK_PATH
```

## Configuración en el Ordenador

Por otro lado, debemos crear un enlace simbólico en `.task` y
`~/.local/share/timewarrior` hacia las carpeta de Dropbox correspondientes.
Esto permite que se sincronice directamente desde el ordenador mediante el
demonio de Dropbox instalado.  `

> **Advertencia**
    Si se modifica la misma tarea en dos dispositivos distintos *antes* de realizar
    la sincronización, se encontrarán conflictos de fusión por parte de Dropbox.
    No dar pie a esta situación arregla el problema.
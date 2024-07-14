Title: Instalación Oracle ODBC en Apple Silicon
Date: 2021-01-12
Tags: Oracle, ODBC, M2

En este tutorial, aprenderás cómo instalar y configurar Oracle Instant Client y ODBC en dispositivos Apple Silicon, como el M1.

Vamos a descargar los archivos necesarios, configurar las variables de entorno, instalar `unixODBC` como Driver Manager, y finalmente conectar Python a una base de datos Oracle utilizando `cx_Oracle`. 

Sigue los pasos detallados a continuación para completar la instalación y configuración correctamente.

En primer lugar hay que [descargar Oracle Instant Client y OBDC](https://www.oracle.com/database/technologies/instant-client/macos-arm64-downloads.html){:target="_blank"}.

Para instalarlos, hay que abrir los archivos `.dmg`, lo cual lo monta en `/Volumes` y entrar vía terminal a la carpeta y ejecutar el script `install_ic.sh`. Acto seguido puedes desmontar la imagen del Finder, saliendo anteriormente de la terminal.

Ahora, moveremos los archivos a `/usr/local/oracle/instantclient_23_3`:

```sh
sudo mv $HOME/Downloads/instantclient_23_3 /usr/local/oracle/instantclient_23_3
```

Y añadiremos las variables de entorno a `.zshrc` :

```sh
export PATH=/usr/local/oracle/instantclient_19_8:$PATH
export DYLD_LIBRARY_PATH=/usr/local/oracle/instantclient_19_8:$DYLD_LIBRARY_PATH
export TNS_ADMIN=/usr/local/oracle/instantclient_19_8/network/admin
```

```sh
source ~/.zshrc
```

Debes instalar `unixODBC`, que es un Driver Manager para ODBC. Puedes hacerlo utilizando Homebrew:

```sh
brew install unixodbc
```

Ahora, debes crear un archivo `odbcinst.ini` en `/usr/local/etc` con el siguiente contenido:

```ini
[Oracle 23 ODBC driver]
Description     = Oracle ODBC driver for Instant Client 23
Driver          = /usr/local/oracle/instantclient_23_3/libsqora.dylib.23.1
```

Y un archivo `odbc.ini` en el directorio de usuario con el siguiente contenido:

```ini
[OracleODBC]
Driver = /usr/local/oracle/instantclient_23_3/libsqora.dylib.23.1
Server = your_oracle_server
UID = your_username
PWD = your_password
```

### Instala el paquete cx_Oracle usando pip

```sh
pip install cx_Oracle
```

### Conexión a la base de datos

```python
import cx_Oracle
import sys
from datetime import date, datetime

# Configura tu conexión
dsn = cx_Oracle.makedsn('your_oracle_server', 1521, sid='your_sid')
username = 'your_username'
password = 'your_password'

# Conectarse a la base de datos
try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    # Ejecutar una consulta
    cursor.execute("SELECT * FROM your_table")

    # Obtener resultados
    for row in cursor.fetchall():
        print(row)

except cx_Oracle.DatabaseError as e:
    error, = e.args
    print(f"Error code: {error.code}")
    print(f"Error message: {error.message}")

finally:
    # Cerrar la conexión
    if cursor:
        cursor.close()
    if connection:
        connection.close()
```
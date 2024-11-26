Title: Eliminar datos sensibles de un repositorio de git
Date: 2017-08-29
Tags: git, privacidad, seguridad

Aunque Git incluye un comando nativo para eliminar datos sensibles de un repositorio, conocido como `filter-branch`, existe una herramienta escrita en Java mucho más rápida y sencilla de usar para realizar esta tarea.

## Herramienta recomendada: BFG Repo-Cleaner

**BFG Repo-Cleaner** es una alternativa eficiente y fácil de usar para limpiar un repositorio Git de información sensible. Puedes encontrarla en [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

### Uso básico

Para reemplazar texto sensible en todo el repositorio, como contraseñas, simplemente usa el siguiente comando:

```bash
$ bfg --replace-text passwords.txt my-repo.git
```

**Advertencia:** El último commit no se verá afectado por este proceso. Para eliminarlo, deberás borrarlo manualmente y luego volver a ejecutar la limpieza.

### Cómo verificar que los datos sensibles han sido eliminados

Para asegurarte de que no quedan restos de la información sensible en la historia del repositorio, puedes buscar cadenas específicas en todo el historial de Git. Aunque no es la respuesta más votada, este método ha funcionado en varios casos.

Consulta este [enlace de Stack Overflow](https://stackoverflow.com/questions/4468361/search-all-of-git-history-for-a-string) para más detalles.

El comando es el siguiente:

```bash
$ git rev-list --all | GIT_PAGER=cat xargs git grep 'search_string'
```

Este comando buscará una cadena específica (`search_string`) en todos los commits del repositorio, permitiéndote verificar si alguna información sensible permanece en el historial.

## Conclusión

Si bien `filter-branch` es la herramienta nativa de Git para eliminar datos sensibles, **BFG Repo-Cleaner** es una opción más rápida y fácil de usar, especialmente para repositorios grandes. Recuerda siempre verificar que no queden rastros de información sensible después de la limpieza, y eliminar manualmente el último commit si es necesario.
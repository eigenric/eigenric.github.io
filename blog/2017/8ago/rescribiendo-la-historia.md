Title: Reescribiendo la historia con git rebase interactive
Date: 2023-08-10
Tags: git, rebase

![Git rebase](/images/git-rebase.png)

En Git, es común que queramos mejorar la historia de nuestros commits para que sea más clara y organizada, especialmente antes de compartir nuestro trabajo con otros desarrolladores. Una herramienta poderosa para hacerlo es `git rebase -i --root`, que permite modificar de forma interactiva todos los commits del repositorio desde el commit raíz.

## ¿Qué es `git rebase -i --root`?

El comando `git rebase -i --root` inicia un **rebase interactivo** desde el primer commit de tu repositorio. Este tipo de rebase te ofrece varias opciones para manipular la historia de commits. Puedes **fusionar**, **editar**, **reordenar** o **eliminar** commits anteriores de manera que el historial de tu proyecto sea más coherente y fácil de seguir.

Este comando es especialmente útil si has estado trabajando en un proyecto durante un tiempo y deseas hacer que la secuencia de commits sea más comprensible antes de publicarla en un repositorio remoto o de compartirla con otros colaboradores.

## Opciones en el rebase interactivo

Al ejecutar `git rebase -i --root`, Git abrirá tu editor de texto predeterminado con una lista de commits, en la que cada línea representará un commit. Junto a cada commit, verás un comando (por defecto, `pick`) que indica lo que se hará con él. Aquí tienes algunas de las acciones que puedes tomar:

- **pick**: Mantiene el commit tal como está.
- **reword**: Te permite cambiar el mensaje del commit, pero manteniendo su contenido.
- **edit**: Te permite modificar tanto el mensaje como el contenido del commit.
- **squash**: Fusiona el commit con el anterior. Es útil para combinar commits pequeños que representan un solo cambio lógico.
- **fixup**: Similar a `squash`, pero descarta el mensaje del commit que se fusiona.
- **drop**: Elimina el commit completamente de la historia.

### Ejemplo práctico

Supongamos que tienes un repositorio con la siguiente secuencia de commits:

```
Commit A
Commit B
Commit C
```

Ahora ejecutas el siguiente comando:

```bash
git rebase -i --root
```

Esto abrirá tu editor con algo parecido a esto:

```
pick abc1234 Commit A
pick def5678 Commit B
pick ghi9012 Commit C
```

Supongamos que deseas combinar el commit B con el commit A y eliminar el commit C. Modificas las líneas para que se vea así:

```
pick abc1234 Commit A
squash def5678 Commit B
drop ghi9012 Commit C
```

Esto le indica a Git que combine el commit B con el A (fusionándolos en uno solo) y que elimine el commit C. Después de guardar y cerrar el editor, Git te pedirá que escribas un nuevo mensaje de commit para el commit combinado. Una vez finalizado el proceso, tu historial se verá algo así:

```
Commit AB (fusión de A y B)
```

El commit C habrá desaparecido, y la historia de tu proyecto será más limpia.

## Consejos y advertencias

El uso de `git rebase -i --root` es muy poderoso, pero debe usarse con cuidado. Reescribir la historia está bien en ramas locales o en commits que no se han compartido con otros. Sin embargo, si ya has compartido tu trabajo, reescribir la historia puede generar conflictos para otros desarrolladores que trabajen en la misma rama.
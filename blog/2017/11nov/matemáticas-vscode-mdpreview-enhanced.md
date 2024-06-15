Title: Renderiza matemáticas en Visual Studio Code
Date: 2018-11-18
Tags: vscode, markdown, markdown-preview-enhanced, mathjax, katex

![Ecuaciones](/images/ecuaciones.png)

Para mejorar la experiencia de visualización de tus documentos Markdown en *Visual Studio Code*, puedes utilizar el plugin [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced){:target=_blank}. Este plugin te permite previsualizar tus documentos Markdown con una amplia gama de opciones de personalización, incluyendo soporte para fórmulas matemáticas, 

## Instalación

Para instalar la extensión, abre el apartado de extensiones en Visual Studio Code y busca *Markdown Preview Enhanced*. Haz click en instalar.

## Configuración de la extensión

Una vez instalado, busca *Markdown Preview Enhanced* en tus extensiones, haz clic sobre su icono de configuración (Administrar) y selecciona *Configuración de la extensión*.

## Exportar a PDF

Es posible exportar el documento Markdown a PDF mediante Pandoc. Para ello, necesitas tener instalado Pandoc en tu sistema y configurar la ruta de acceso en la configuración de la extensión.

![Pandoc](/images/pandoc.png)

Una vez configurado, puedes exportar el documento haciendo click derecho sobre la vista preview y seleccionando *Export > Pandoc*.

## Cambiar el tema a oscuro

Busca la opción *Preview-theme* y selecciona el tema `atom-dark.css`.

![Tema Oscuro](/images/markdown-preview.png)

## Cambiar el motor de renderizado de fórmulas matemáticas

Por defecto, Markdown Preview Enhanced utiliza KaTex para la renderización de fórmulas matemáticas. Sin embargo, puedes optar por cambiar a MathJax para una visualización menos rápida pero más precisa de las fórmulas, especialmente si estás utilizando notaciones complejas que KaTex aún no soporta completamente.

Busca la opción *Math Rendering Option* y selecciona *MathJax*.

![MathJax](/images/renderizado.png)


Más información sobre las opciones de configuración de Markdown Preview Enhanced en la [documentación oficial](https://shd101wyy.github.io/markdown-preview-enhanced/#/config){:target=_blank}.

> Pd: Ahora se puede editar directamente en el modo de vista previa. ¡Genial!
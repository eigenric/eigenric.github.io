Title: Renderiza matemáticas en VSCode con Markdown-preview-enhanced
Date: 2018-11-18
Tags: vscode, markdown, markdown-preview-enhanced, mathjax, katex
Status: Hidden

Para mejorar la experiencia de visualización de tus documentos Markdown en *Visual Studio Code*, puedes utilizar el plugin **Markdown Preview Enhanced**. Este plugin te permite previsualizar tus documentos Markdown con una amplia gama de opciones de personalización, incluyendo soporte para fórmulas matemáticas, 

Una vez instalado, puedes configurar este plugin en Visual Studio Code siguiendo estos pasos: 

1. Navega a `Archivo -> Preferencias -> Settings` (o usa el atajo de teclado `Ctrl+,`).
2. Busca `Extensiones -> Markdown-preview-enhanced`.

Por defecto, Markdown Preview Enhanced utiliza KaTex para la renderización de fórmulas matemáticas. Sin embargo, puedes optar por cambiar a MathJax para una visualización más precisa de las fórmulas, especialmente si estás utilizando notaciones complejas que KaTex aún no soporta completamente.

Para cambiar a MathJax, debes modificar las configuraciones de Visual Studio Code. Este cambio mejorará la madurez y precisión de la renderización de tus fórmulas matemáticas en tus documentos Markdown.

[Manual de Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/)

Por defecto, viene KaTex pero debemos elegir Mathjax para poder previsualizar
las // correctamente. A Katex todavía le falta madurez.

Para cambiarlo, vamos a las settings de vscode

Cambiamos:

Math Rendering Option: MathJax MermaidTheme: dark (Grafiquitos) Print
background: atom-dark

Cambio de Tipografía de Mathjax

En la página de manual encontramos:

[https://shd101wyy.github.io/markdown-preview-enhanced/#/math]

You can Also modify the MathJax config by cmd-shift-p then choose Markdown
Preview Enhanced: Open Mathjax config command


Luego, ejecutamos tal instruccion:

Nos encontramos con lo siguiente:

```javascript
module.exports = {
     extensions: ['tex2jax.js'], 
     jax: ['input/TeX','output/HTML-CSS'], 
     messageStyle: 'none', 
     tex2jax: {
        processEnvironments: false, 
        processEscapes: true 
    }, 
    TeX: { 
        extensions: ['AMSmath.js', 'AMSsymbols.js', 'noErrors.js', 'noUndefined.js'] 
    }, 
    'HTML-CSS': { availableFonts: ['TeX'], scale: 70 // Añadido }
}
```

Listo
Title: Advent of Code 2020 en Rust
Date: 2022-02-20
Tags: 
Status: hidden

[Planteamiento del problema](https://adventofcode.com/2020/day/7)

Analizamos como se ejecutaría `examine_neighbors()`
recursivamente:

Tenemos `shiny_gold` contenida en:

```
- Bright white
- Muted Yellow
```

Luego `vecinos_in = [NodeIndex(2), NodeIndex(1)]`

Ejecutamos `examine_neighbors(vecinos_in)`

total = 0

El primer vecino es Muted Yellow. Obtenemos sus
in_neightbors:

Muted Yellow contenida en:
```
- light red
- dark orange
```

Luego vecinos_in = [NodeIndex(3), NodeIndex(0)]

Ejecutamos examine_neighbors(vecinos_in)

El primer vecino es Dark Orange. Obtenemos sus
in_neightbors:

Dark Orange está contenida en: ninguno

luego total += 1


El segundo vecino es light red. Obtenemos sus
in_neighbors:

Light red está contenida en:
ninguno

Luego total = 2

Devolvemos total 2


El segundo vecino es Bright white.

Obtenemos sus in_neightbors:

Dark Orange
Light red
# Algoritmo 2: Algoritmo Bellman-Ford
Por Julissa Ponte

Este algoritmo fue publicado por primera vez por Moore en 1957, y después de forma independiente por Bellman en 1958, quien usó la idea de la relajación de arcos, que había sido
propuesta por Ford en 1956. Este algoritmo es conocido normalmente por Bellman-Ford. El algoritmo calcula la ruta más corta del nodo fuentes a todo nodo de la red `i`, además es 
eficiente incluso si en la red existen arcos con distancias negativas. También puede detectar la presencia de ciclos negativos.

Este método es iterativo y se basa en la etiquetación de nodos, donde en la iteración `k`, la etiqueta representa el costo de la ruta más corta del nodo fuentes a todo nodo `i`, 
la cual contiene `k + 1` o menos arcos.

## Pasos del algortimo:
- Inicializar la distancia desde el origen al destino como infinito.
- Seleccionar dos aristas al azar y haga la lista de aristas.
- Relajar los bordes hasta que la distancia más corta comience a repetirse o, en el peor de los casos, n-1 veces.

## Analisis Asintótico
Como necesitamos relajar los tiempos máximos de bordes `V - 1`, la complejidad del tiempo de este algoritmo será igual a `O (V * E)` donde `E` denota el número de bordes, 
si usamos la lista de adyacencia para representar el gráfico. Sin embargo, si se usa una matriz de adyacencia para representar el gráfico, la complejidad del tiempo será `O (V ^ 3)`.
La razón es que podemos iterar a través de todos los bordes en el tiempo O `(E)` cuando se usa la lista de adyacencia, pero toma el tiempo `O (V ^ 2)` cuando se usa la matriz de adyacencia.

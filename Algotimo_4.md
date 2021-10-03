# Complejidad del Algoritmo de Dijkstra

El algoritmo de Dijkstra es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto de los vértices en un grafo que tiene pesos en cada arista.

La complejidad computacional del algoritmo de Dijkstra se puede calcular contando las operaciones realizadas:

-El algoritmo consiste en n-1 iteraciones, como máximo. En cada iteración, se añade un vértice al conjunto distinguido. 

-En cada iteración, se identifica el vértice con la menor etiqueta entre los que no están en Sk. El número de estas operaciones está acotado por n-1. 

-Además, se realizan una suma y una comparación para actualizar la etiqueta de cada uno de los vértices que no están en Sk

-Luego, en cada iteración se realizan a lo sumo 2(n-1) operaciones.

Entonces, el algoritmo de Dijkstra realiza O(n^2) operaciones (sumas y comparaciones) para determinar la longitud del camino más corto entre dos vértices de un grafo ponderado simple, conexo y no dirigido con n vértices.

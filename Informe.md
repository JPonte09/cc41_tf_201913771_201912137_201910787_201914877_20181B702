# Problema de los Almacenes (VRP)
#### CC41 - TRABAJO FINAL DE COMPLEJIDAD ALGORÍTMICA 2021

## Integrantes
- Sebastián Martin Trujillo Hilares
- Julissa Karol Ponte Isminio
- Julio Enrique Barrios Aedo
- Paolo Manoel Pinzás R.

# Introducción
El problema de enrutamiento de vehículos (VRP) consiste en que se debe determinar el conjunto de caminos o rutas para un grupo de vehículos con base en uno o más depósitos para varias ciudades o clientes geográficamente dispersos en una ciudad. El objetivo del VRP es ofrecer un conjunto de clientes con demandas conocidas sobre rutas de vehículos de costo mínimo que se originan y terminan en un depósito.

<img src="https://github.com/JPonte09/cc41_tf_201913771_201912137_201910787_201914877_20181B702/blob/main/images/vrp_imagen.png" width="400">

# Objetivos
* Desarrollar la competencia general de razonamiento cuantitativo y la competencia específica de uso de técnicas y herramientas acorde a los objetivos del curso.
* Desarrollar algoritmos que permitan resolver completa o parcialmente el problema de enrutamiento de vehículos.
* Determinar la importancia de la aplicación de algoritmos eficientes a la hora de resolver un problema.
* Analizar la eficiencia y complejidad de los algoritmos planteados.

# Marco Teórico
## Algoritmo de Floyd-Warshall
Fue descrito por primera vez por Bernard Roy en 1959, se trata de un algoritmo de análisis sobre grafos para encontrar el camino mínimo en grafos dirigidos. Este algoritmo encuentra el mejor camino de todos los pares de vértices en una sola ejecución y es un claro ejemplo de programación dinámica.

Este algoritmo compara todos los posibles caminos entre cada par de vértices que se encuentra en el grafo en tan solo V^3 comparaciones, lo cual es logrado gracias a que poco a poco hace una estimación del mejor camino entre dos vértices, hasta que se sabe la estimación óptima.

Se define un grafo G con vértices V numerados de 1 a N, y una función CaminoMinimo(i, j, k) que devuelve el camino mínimo de i a j (los cuales conforman V) utilizando solo los vértices de 1 a k como puntos intermedios en el camino. Dada esta función se procede a calcular el camino mínimo de i a j utilizando solo los vértices de 1 hasta a k+1.

Una vez definido esto, se pueden presentar dos posibles situaciones; el camino mínimo se puede hallar directamente mediante la función CaminoMinimo(i, j, k) y se halla comprendido entre los vértices 1 a k+1; o se encuentra como el camino mínimo de k+1 a j, por lo cual se debiesen de concatenar dos caminos mínimos para formar el más óptimo.

## Algoritmo de Bellman-Ford
Este algoritmo fue publicado por primera vez por Moore en 1957, y después de forma independiente por Bellman en 1958, quien usó la idea de la relajación de arcos, que había sido propuesta por Ford en 1956. Este algoritmo es conocido normalmente por Bellman-Ford. El algoritmo calcula la ruta más corta del nodo fuentes a todo nodo de la red i, además es eficiente incluso si en la red existen arcos con distancias negativas. También puede detectar la presencia de ciclos negativos.

Este método es iterativo y se basa en la etiquetación de nodos, donde en la iteración k, la etiqueta representa el costo de la ruta más corta del nodo fuentes a todo nodo i, la cual contiene k + 1 o menos arcos.

Como necesitamos relajar los tiempos máximos de bordes V - 1, la complejidad del tiempo de este algoritmo será igual a O (V * E) donde E denota el número de bordes, si usamos la lista de adyacencia para representar el gráfico. Sin embargo, si se usa una matriz de adyacencia para representar el gráfico, la complejidad del tiempo será O (V ^ 3). La razón es que podemos iterar a través de todos los bordes en el tiempo O (E) cuando se usa la lista de adyacencia, pero toma el tiempo O (V ^ 2) cuando se usa la matriz de adyacencia.

## Algoritmo de Prim
El algoritmo de Prim busca un árbol con expansión mínima que se haya encontrado en un Grafo. Esto funciona si los vértices del grafo son conexos y no dirigidos. El algoritmo busca los recorridos posibles con el menor peso posible que hay en las aristas.

Al analizar las posibles acciones dentro del código. La complejidad algorítmica resulta ser de Big O(n^2) por la interacción de 2 bucles en el código que se usa para la asignación de los vertices y aristas visitados en el grafo.

## Algoritmo de Dijkstra
El algoritmo de Dijkstra es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto de los vértices en un grafo que tiene pesos en cada arista.

La complejidad computacional del algoritmo de Dijkstra se puede calcular contando las operaciones realizadas:

- El algoritmo consiste en n-1 iteraciones, como máximo. En cada iteración, se añade un vértice al conjunto distinguido.

- En cada iteración, se identifica el vértice con la menor etiqueta entre los que no están en Sk. El número de estas operaciones está acotado por n-1.

- Además, se realizan una suma y una comparación para actualizar la etiqueta de cada uno de los vértices que no están en Sk

- Luego, en cada iteración se realizan a lo sumo 2(n-1) operaciones.

Entonces, el algoritmo de Dijkstra realiza O(n^2) operaciones (sumas y comparaciones) para determinar la longitud del camino más corto entre dos vértices de un grafo ponderado simple, conexo y no dirigido con n vértices.

# Implementación de los Algortimos
## Algoritmo de Floyd-Warshall

## Algoritmo de Bellman-Ford

## Algoritmo de Prim
<pre>
def prim(Grafo, x, y):
  n = len(Grafo)
  visited = [False]*n
  path = [-1]*n
  primero = [(x,y)]
  almacen = []
  for i in range(n):
    almacen.append([0]*2)
  costo = [math.inf]*n
  cont2 = 0
  cont1 = 0
  while primero:
    _, padre = hq.heappop(primero)

    if not visited[padre]:
      visited[padre] = True
      for valor in Grafo[padre]:
        if valor != 'P' and valor != 'A':
          for valor2 in Grafo[padre]:
            if valor2 != 'P' and valor2 != 'A':
              if not visited[valor] and valor2 < costo[valor]:
                costo[valor] = valor2
                path[valor] = padre
                hq.heappush(primero, (valor2, valor))
              
              if Grafo[cont2][2] == 'A':
                almacen[cont1][0] = path[valor]
                almacen[cont1][1] = costo[valor]
                cont1 = cont1 +1 
          
      cont2 = cont2 + 1

  return path, costo, almacen
</pre>

## Algortimo de Dijkstra
<pre>
def Dijkstra(G, s):
  visited = {}
  path = {}
  cost = {}
  for key in g.keys():
    visited[k] = False
    path[k] = None
    cost[k] = math.inf

  cost[s] = 0
  queue = [(s, 0)]
  while queue:
    u, g_u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True        
      for v in G[u]:
        f = G_u + 1
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (v, f))
  return path

Dijkstra(ciudad, almacenes)
</pre>

# Conclusiones
* Tanto los algoritmos Bellman-Ford, Prim, Dijkstra y Floyd-Warshall son adecuados para la resolucion de este problema.
* Gracias a este trabajo, pudimos aprender masa sobre Phyton como lenguaje de programacion ,el cual hasta el principio del semestre era algo nuevo para nosotros.
* Finalmente el uso como tal de la plataforma de GitHub nos permitio conocer más acerca del uso de Issues y de los commits, lo cual nos ayudara muchisimo en futuros proyectos, ya sean proyectos pequeños o grandes.

# Bibliografía
* Favtutor, Floyd Warshall Algorithm (Python) | Dynamic Programming.  https://favtutor.com/blogs/floyd-warshall-algorithm

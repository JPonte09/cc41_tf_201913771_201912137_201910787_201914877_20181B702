# Algoritmo Floyd-Warshall
Fue descrito por primera vez por Bernard Roy en 1959, se trata de un algoritmo de análisis sobre grafos para encontrar el camino minimo en grafos dirigidos. Este algoritmo encuentra el mejor camino de todos los pares de vertices en una sola ejecución y es un claro ejemplo de programación dinamica.

Este algoritmo a su vez se trata de la mezcla de dos distintos algoritmos, los cuales son indicados en su nombre compuesto; así pues, para entender aún más el funcionamiento de este algoritmo se presentará una breve explicación de los algoritmos que lo componen:

# Algoritmo Floyd
Es bastante similar al algoritmo usado por Warshall, pero este permite el uso de grafos ponderados, permitiendo que la "flecha" que indica la union entre dos nodos tenga valores enteros o infinito, siendo infinito un indicador de que esos nodos no poseen una union directa entre ellos. De esta forma, este algoritmo es perfectamente aplicable para las distancias almacenadas entre cada par de nodos que se encuentren conectados.

# Algoritmo Warshall
Es un algoritmo booleano, ya que hace uso de una matriz compuesta de 0 e 1, los cuales indican que hay o no correspondencia en el grafo y, a travez de este algoritmo se obtiene una matriz transitiva la cual muestra si es que dos nodos se hallan conectados mediante una union indirecta.

# Funcionamiento Floyd-Warshall
Este algoritmo compara todos los posibles caminos entre cada par de vertices que se encuentra en el grafo en tan solo V^3 comparaciones, lo cual es logrado gracias a que poco a poco hace una estimación del mejor camino entre dos vértices, hasta que se sabe la estimación optima.

Se define un grafo G con vertices V numerados de 1 a N, y una funcion CaminoMinimo(i, j, k) que devuelve el camino minimo de i a j (los cuales conforman V) utilizando solo los vertices de 1 a k como puntos intermedios en el camino. Dada esta función se procede a calcular el camino minimo de i a j utilizando solo los vertices de 1 hasta a k+1.

Una vez definido esto, se pueden presentar dos posibles situaciones; el camino minimo se puede hallar directamente mediante la funcion CaminoMinimo(i, j, k) y se halla comprendido entre los vertices 1 a k+1; o se encuentra como el camino minimo de k+1 a j, por lo cual se debiesen de concatenar dos caminos minimos para formar el más optimo.

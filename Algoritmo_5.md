# Algoritmo Kruskal

Es un algoritmo de la teoría de grafos para encontrar un árbol recubridor mínimo e un grafo conexo y ponderado. Es decir, busca un subconjunto de aristas que, formando un árbol, incluyen todos los vértices y donde el valor total de todas las aristas del árbol es el mínimo. 

## Pasos para la implementación

- Ordenar todos los bordes de bajo peso a alto

- Tomar el borde con el peso más bajo y agréguelo al árbol de 
expansión. Si agregar el borde creó un ciclo, rechace este borde.

- Siguir agregando bordes hasta que lleguemos a todos los vértices. 

Para este algoritmo, como para todos los algoritmos de árboles de expansión minima, gira en torno a verificar que al agregar un borde este no cree un bucle.

La forma más común de averiguar esto es un algoritmo llamado Union-Find.

### Algoritmo Union Find
----------------------------------

Este algoritmo divide a los vértices en grupos y nos permite verificar si dos vertices pertenecen al grupo o no y, por lo tanto, se encarga de decidir si agregar una arista crea un ciclo.

**Metodo Find:** Este método determina a cual componente conexa pertenece un vértice X determinado, ello lo hace retornando el vértice raíz del árbol en el que se encuentra el vértice X.

**Metodo Union:** Este método permite unir 2 componentes conexas con los siguientes pasos:

- Obtenemos la raíz del vértice x.

- Obtenemos la raíz del vértice y.

- Actualizamos el padre de alguna de las raíces, asignándole como nuevo padre la otra raíz.

-----------------------------------
## Complejidad

<img src="https://github.com/JPonte09/cc41_tf_201913771_201912137_201910787_201914877_20181B702/blob/main/images/Kruskal_Complexity.png" width="500">

```

T(n) = O(1) + O(V) + O(E log E) + O(V log V)
     = O(E log E) + O(V log V)

|E| >= |V| - 1

T(n) = E log E + E log E
     = E log E

```

Por lo tanto podemos decir que ``O(E log E)``

Aunque existe una variación por lo que 

```
|E| <= |V|²  

log |E| < log |V|²   
log |E| < 2 log |V|

O(E log V)
```

Por lo tanto se puede decir que ``O(E log V)``

Si tomamos como referencia lo explicado en "Algorithms book by Dasgupta" nos menciona que ``log E ≈ log V``, por lo que concluimos en que la complejidad del algoritmo puede ser tanto ``O(E log E)`` como ``O(E log V)``.

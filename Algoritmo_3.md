# Algoritmo de Prim
El algoritmo de Prim busca un árbol con expansión mínima que se haya encontrado en un Grafo. Esto funciona si los vértices del grafo son conexos y no dirigidos. El algoritmo busca los recorridos posibles con el menor peso posible que hay en las aristas.
## Funcionamiento:
1)	Se marca cualquier vértice para el inicio del recorrido.
2)	Se escoge la arista que menos peso tiene y se avanza al vértice de aquella arista.
3)	Si la arista escogida forma un ciclo en el grafo, entonces, se buscará otra arista entre los vértices recorridos.
4)	Repetir el paso 2 y 3 hasta que se haya seleccionado todos los vértices asignados en el grafo. Finalmente, esto nos generará un árbol de expansión mínima.
## Complejidad:
Al analizar las posibles acciones dentro del código. La complejidad algorítmica resulta ser de Big O(n^2) por la interacción de 2 bucles en el código que se usa para la asignación de los vertices y aristas visitados en el grafo.


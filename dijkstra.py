#----------Implementacion del algortimo de Dijkstra para el grafo generado----------

import math

#---------------------Grafo------------------------

def leer_archivo(archivo):
  archivoCsv = list()
  with open(archivo) as a: 
    reader = csv.reader(a, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[0] != 'x':
          row[0], row[1] = int(row[0]), int(row[1])
          archivoCsv.append(row)
  archivoCsv.sort(key = lambda x: (x[0], x[1]))
  return archivoCsv


ciudad = leer_archivo("ciudad.csv")


grafoCiudad=[[] for _ in range(2700)]
for i,_ in enumerate(ciudad):
      grafoCiudad[ciudad[i][0]].append(ciudad[i][1])
    
#---------------------Dijkstra----------------------

def backtrace(parent, start, end):
  path = [end]
  while path[-1] != start:
    path.append(parent[path[-1]])
  path.reverse()
  return path


def dijkstra(G, start, end):
  n = len(G)
  queue = []
  visited = {}
  distance = {}
  shortest_distance = {}
  parent = {}

  for node in range(n):
    visited[node] = False
    distance[node] = None
    shortest_distance[node] = math.inf
    parent[node] = None
    
  queue.append(start)
  distance[start] = 0

  while len(queue) != 0:
    current = queue.pop(0)
    visited[current] = True
    
    if current == end:
      print(backtrace(parent, start, end))
      break
    
    for v in G[current]:
      if visited[v] == False:
        distance[v] = distance[current] + 1
        if distance[v] < shortest_distance[v]:
          shortest_distance[v] = distance[v]
          parent[v] = current
          queue.append(v)

#-----Pruebas para retornar la ruta mas corta desde un punto A a un punto B-----

dijkstra(grafoCiudad, 1, 227)
# [1, 72, 227]

dijkstra(grafoCiudad, 586, 1540)
# [586, 1540]

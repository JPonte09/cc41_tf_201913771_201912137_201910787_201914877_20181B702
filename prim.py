import numpy as np
import numpy.random as npr
import csv
import matplotlib.pyplot as plt
import graphviz as gv
import pandas as pd
import heapq as hq
import math


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


almacenes = leer_archivo("almacenes.csv")
puntos = leer_archivo("puntos.csv")
x, y = np.array(almacenes).T 
x2, y2 = np.array(puntos).T 
plt.figure(figsize=(20, 20)) 
plt.scatter(x,y, 20, c="red") 
plt.scatter(x2,y2, 20, c="black") 
plt.show() 


def escribir_archivo(cabezera, datos, archivo): #para hacer un nuevo csv
  with open(archivo, 'w') as a:   #para abrir un archivo que se crea desde 0 
    write = csv.writer(a)
    if cabezera != None: write.writerow(cabezera)
    write.writerows(datos)


grafo=[[] for _ in range(2000)]
for i,_ in enumerate(almacenes):
      grafo[almacenes[i][0]].append(almacenes[i][1])
escribir_archivo(None,grafo,'grafoAlmacenes.csv')


grafoPuntos=[[] for _ in range(2500)]
for i,_ in enumerate(puntos):
      grafoPuntos[puntos[i][0]].append(puntos[i][1])
escribir_archivo(None,grafoPuntos,'grafoPuntos.csv')


for i, _ in enumerate(almacenes): 
  almacenes[i].append('A')
for i, _ in enumerate(puntos):
  puntos[i].append('P')
ciudad = list()
ciudad.extend(almacenes)
ciudad.extend(puntos)
ciudad.sort(key = lambda x: (x[0], x[1])) 
escribir_archivo(['x', 'y', 'tipo'], ciudad, 'ciudad.csv') 


grafoCiudad=[[] for _ in range(2000)]
for i,_ in enumerate(ciudad):
      grafoCiudad[ciudad[i][0]].append(ciudad[i][1])
escribir_archivo(None,grafoCiudad,'grafoCiudad.csv')

#----------ALGORTIMO 3- ---Julio.. ----------

def prim(G):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  q = [(0, 0)]
  cost = [math.inf]*n
  while q:
    _, u = hq.heappop(q)
    if not visited[u]:
      visited[u] = True
      for v in G[u]:
        if v != 'P' and v != 'A':
          for w in G[u]:
            if w != 'P' and w != 'A':
              if not visited[v] and w < cost[v]:
                cost[v] = w
                path[v] = u
                hq.heappush(q, (w, v))

  return path, cost

prim(ciudad)

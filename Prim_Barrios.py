import numpy as np
import numpy.random as npr
import csv
import matplotlib.pyplot as plt
import graphviz as gv
import pandas as pd
import heapq as hq
import math
import numpy as np

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

#----------ALGORTIMO 3- ---Julio-----------

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



pat, co, almacen = prim(ciudad, 1, 0)

almacen1 = []
for i in almacen:
  if i not in almacen1 :
    almacen1.append(i)


print("[ Almacen Path, Costo ]")
print(almacen1)
print("************************************************")
print("Para hayar puntos y almacenes con costos cortos:")
print(pat)

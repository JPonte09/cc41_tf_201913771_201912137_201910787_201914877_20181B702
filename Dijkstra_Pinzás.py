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

for i,_ in enumerate(ciudad):
  if ciudad[i][2] == 'A':
    almacenes.append(ciudad[i])

for j,_ in enumerate(ciudad):
  if ciudad[j][2] == 'P':
    puntos_de_entrega.append(ciudad[j])

grafoCiudad=[[] for _ in range(2700)]
for i,_ in enumerate(ciudad):
      grafoCiudad[ciudad[i][0]].append(ciudad[i][1])


#----------Algoritmo 4 - Dijkstra-----------


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

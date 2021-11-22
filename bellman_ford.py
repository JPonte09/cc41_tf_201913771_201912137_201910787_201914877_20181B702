#-----IMPLEMENTACIÓN DE PRIMERA VERSIÓN DEL ALGORITMO BELLMAN FORD------
import math

def bellmanFord(G, s):
  n = len(G)
  cost = [float('inf')]*n
  parent = [None]*n
  
  cost[s] = 0
  
  # relax
  for _ in range(n-1):
    for current in range(n):
      for v in G[current]:
        if cost[current] + 1 < cost[v]:
          cost[v] = cost[current] + 1
          parent[v] = current

  # check negative cycle
  for current in range(n):
    for v in G[current]:
      if cost[current] + 1 < cost[v]:
        return None, None

  return parent, cost

parent, cost = bellmanFord(grafoCiudad, 10)

print(parent)
print(cost)

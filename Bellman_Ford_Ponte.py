#-----------------------------ALGORITMO 2-----------------------------
#--------------ELABORADO POR JULISSA KAROL PONTE ISMINIO--------------
#-----IMPLEMENTACIÓN DE PRIMERA VERSIÓN DEL ALGORITMO BELLMAN FORD----

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

parent, cost = bellmanFord(grafoCiudad, 0)

#-----IMPLEMENTACIÓN DE SENGUNDA VERSIÓN DEL ALGORITMO BELLMAN FORD----

import graphviz as gv
import numpy as np
import pandas as pd

def adjlShow(L, labels=None, directed=False, weighted=False, path=[],
             layout="sfdp"):
  g = gv.Digraph("G") if directed else gv.Graph("G")
  g.graph_attr["layout"] = layout
  g.edge_attr["color"] = "gray"
  g.node_attr["color"] = "orangered"
  g.node_attr["width"] = "0.1"
  g.node_attr["height"] = "0.1"
  g.node_attr["fontsize"] = "8"
  g.node_attr["fontcolor"] = "mediumslateblue"
  g.node_attr["fontname"] = "monospace"
  n = len(L)
  for u in range(n):
    g.node(str(u), labels[u] if labels else str(u))
  added = set()
  for v, u in enumerate(path):
    if u != None:
      g.edge(str(u), str(v), dir="forward", penwidth="2", color="blue")
      added.add(f"{u},{v}")
      added.add(f"{v},{u}")
  if weighted:
    for u in range(n):
      for v, w in L[u]:
        if not directed and not f"{u},{v}" in added:
          added.add(f"{u},{v}")
          added.add(f"{v},{u}")
          g.edge(str(u), str(v), str(1))
        elif directed:
          g.edge(str(u), str(v), str(1))
  else:
    for u in range(n):
      for v in L[u]:
        if not directed and not f"{u},{v}" in added:
          added.add(f"{u},{v}")
          added.add(f"{v},{u}")
          g.edge(str(u), str(v))
        elif directed:
          g.edge(str(u), str(v))
  return g

adjlShow(grafoCiudad, path=cost)

def Tercer_Algoritmo(g, s):
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
      for v in g[u]:
        f = g_u + 1
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (v, f))
  return path

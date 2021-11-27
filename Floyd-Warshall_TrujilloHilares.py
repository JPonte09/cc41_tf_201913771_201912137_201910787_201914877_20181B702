def floydWarshall(G, tamano):
    n=len(G)
    Costos = [[math.inf]*tamano for _ in range(tamano)]
    Padres = [[-1]*tamano for _ in range(tamano)]
    for nodos in range(n):
        for distancia, nodo, vecino in G[nodos]:
            Costos[nodo][nodo] = 0
            Costos[nodo][vecino] = distancia
            Padres[nodo][vecino] = nodo
            
            
    for k in range(tamano):
        for i in range(tamano):
            for j in range(tamano):
                pesoAcumulado = Costos[i][k] + Costos[k][j]
                if Costos[i][j] > pesoAcumulado:
                    Costos[i][j] = pesoAcumulado
                    Padres[i][j] = k       
    return Padres

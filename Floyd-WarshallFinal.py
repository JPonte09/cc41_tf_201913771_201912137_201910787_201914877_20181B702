def generarGrafoFloyd(G):
    n=len(G)
    grafo=[[] for _ in range(n)]
    i=0
    r=[]
    for _, nodo, _ in G:
        r.append(int(nodo))
        
    norep=repetidos(r)


    uCodigos=[]
    for nodo in norep:
        uCodigos.append((i, nodo))
        i=i+1

    for u in range(n):
        distancias=[x[0] for x in G]
        nodos=[x[1] for x in G]
        vecinos=[x[2] for x in G]
        nd=buscar(uCodigos, int(nodos[u]))
        v=buscar(uCodigos, int(vecinos[u]))
        if distancias[u]==None:
            distancias[u]=0
        grafo[u].append((distancias[u], nd, v))      
    return grafo, uCodigos
  
def floydWarshall(G, tamano):
    n=len(G)
    maCostos = [[math.inf]*tamano for _ in range(tamano)]
    maPadres = [[-1]*tamano for _ in range(tamano)]
    for nodos in range(n):
        for distancia, nodo, vecino in G[nodos]:
            maCostos[nodo][nodo] = 0
            maCostos[nodo][vecino] = distancia
            maPadres[nodo][vecino] = nodo
            
    for k in range(tamano):
        for i in range(tamano):
            for j in range(tamano):
                pesoAcumulado = maCostos[i][k] + maCostos[k][j]
                if maCostos[i][j] > pesoAcumulado:
                    maCostos[i][j] = pesoAcumulado
                    maPadres[i][j] = k
           
    return maPadres

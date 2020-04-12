#UVA 200 Rare Order

from sys import stdin

def topoSort(Graph, aux):
    n = len(Graph)
    indeg = [0 for i in range(n)]
    for u in range(n):
        for v in Graph[u]:
            pos = aux.index(v)
            indeg[pos] += 1
    topo = []

    while len(topo) < n:
        for i in range(n):
            if indeg[i] == 0:
                topo.append(aux[i])
                for j in Graph[i]:
                    pos = aux.index(j)
                    indeg[pos] -= 1
                indeg[i] -= 1
    print("".join(topo))
    return topo

def solve(palabras):
    letters = []
    for i in range(len(palabras)):
        p = palabras[i]
        for j in range(len(p)):
            if p[j] not in letters:
                letters.append(p[j])

    listAd = [[] for i in range(len(letters))]
    for i in range(1, len(palabras)):
        prev = palabras[i- 1]
        next = palabras[i]
        m = min(len(prev), len(next))
        j = 0
        while j < m:
            if(prev[j] != next[j]):
                index = None
                for k in range(len(letters)):
                    if prev[j] == letters[k]:
                        index = k
                listAd[index].append(next[j])
                j = m
            j += 1

    topoSort(listAd, letters)

def main():
    line = stdin.readline().strip()
    palabras = []
    while(len(line)):
        if line == "#":
            solve(palabras)
            palabras = []
        else:
            palabras.append(line)
        line = stdin.readline().strip()

main()

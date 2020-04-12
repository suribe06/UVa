#UVA 13127 Bank Robbery

from sys import stdin
from heapq import heappop,heappush

INF = float('inf')

def dijkstra(G):
    global queue, dist
    visited = [False for _ in range(len(G))]
    while len(queue) != 0:
        d, u = heappop(queue)
        if visited[u] == False:
            visited[u] = True
            for v, dv in G[u]:
                duv = d + dv
                if visited[v] == False and dist[v] > duv:
                    dist[v] = duv
                    heappush(queue,(duv, v))

def solve(G, banks, police):
    global dist, queue
    queue = []
    dist = [INF for _ in range(len(G))]

    for i in police:
        heappush(queue, (0, i))
        dist[i] = 0

    dijkstra(G)

    d = []
    for i in banks:
        d.append(dist[i])

    maximum, cont = max(d), 0
    temp = []
    for i in banks:
        if dist[i] == maximum:
            cont += 1
            temp.append(i)

    if maximum == INF:
        print(cont, end = " ")
        print("*")
    else:
        print(cont, end = " ")
        print(maximum)

    temp.sort()
    for i in range(len(temp)):
        if i + 1 != len(temp):
            print(temp[i],end = ' ')
        else:
            print(temp[i])

def main():
    global queue, dist
    data = stdin.readline().strip()
    while data != "":
        N,M,B,P = map(int, data.split())
        G = [[] for i in range(N)]
        banks = []
        police = []
        for i in range(M):
            u, v, d =  map(int,stdin.readline().split())
            G[u].append((v, d))
            G[v].append((u, d))

        banks = [int(i) for i in stdin.readline().split()]
        if P != 0:
            police = [int(i) for i in stdin.readline().split()]

        solve(G, banks, police)
        data = stdin.readline().strip()

main()

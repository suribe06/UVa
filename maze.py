#UVA 1112 Mice and Maze

from sys import stdin
from heapq import heappop,heappush

INF = float('inf')

def dijkstra(G, source):
    dist = [ INF for _ in range(len(G)) ]
    visited = [ False for _ in range(len(G)) ]
    dist[source] = 0
    queue = [ (0, source) ]
    while len(queue) != 0:
        d, u = heappop(queue)
        if visited[u] == False:
            visited[u] = True
            for v, dv in G[u]:
                duv = d + dv
                if visited[v] == False and dist[v] > duv:
                    dist[v] = duv
                    heappush(queue, (duv, v))
    return dist

def solve(G, exit, t):
    ans = dijkstra(G, exit)
    cont = 0
    for i in ans:
        if i <= t:
            cont += 1
    return cont

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        stdin.readline()
        lenv = int(stdin.readline())
        exit = int(stdin.readline()) - 1
        t = int(stdin.readline())
        lene = int(stdin.readline())
        G = [list() for _ in range(lenv)]
        for j in range(lene):
            u, v, d = map(int, stdin.readline().split())
            G[v-1].append((u-1, d))

        print(solve(G, exit, t))
        if i != cases-1:
            print()

main()

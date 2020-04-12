#UVA 1267 Network

from sys import stdin

def dfs(u):
    global visited, ap, parent, low, depth, time, graph
    children = 0
    visited[u] = 1
    depth[u] = time
    low[u] = time
    time += 1

    for v in graph[u]:
        if visited[v] == 0:
            parent[v] = u
            children += 1
            dfs(v)
            low[u] = min(low[u], low[v])
            if parent[u] == -1 and children > 1:
                ap[u] = 1
            if parent[u] != -1 and low[v] >= depth[u]:
                ap[u] = 1
        elif v != parent[u]:
            low[u] = min(low[u], depth[v])

def solve():
    global graph, visited, ap, parent, low, depth, time
    n = len(graph)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    low = [None for _ in range(n)]
    depth = [None for _ in range(n)]
    ap = [0 for _ in range(n)]
    time = 0

    for i in range(n):
        if visited[i] == 0:
            dfs(i)

    cont = 0
    for i in range(len(ap)):
        if ap[i] == 1:
            cont += 1

    return cont

def main():
    global graph,lenv
    lenv = int(stdin.readline())
    while lenv!=0:
        graph = [ set() for _ in range(lenv) ]
        tok = [ int(x) for x in stdin.readline().split() ]
        while tok[0]!=0:
            for i in range(1, len(tok)):
                graph[tok[0]-1].add(tok[i]-1)
                graph[tok[i]-1].add(tok[0]-1)
            tok = [ int(x) for x in stdin.readline().split() ]
        print(solve())
        lenv = int(stdin.readline())

main()

#UVA 11709 Trust Groups

from sys import stdin

def dfs(u,num):
	global vis, scc, G
	vis[u] = 1
	scc[u] = num
	for v in G[u]:
		if(vis[v] == 0):
			dfs(v,num)
	return

def dfs_list(u):
	global L, vis, I
	vis[u] = 1
	for v in I[u]:
		if(vis[v] == 0):
			dfs_list(v)
	L.append(u)
	return

def solve():
    global L,I, scc, vis
    n = len(G)
    scc = [-1 for i in range(n)]
    I = [[] for i in range(n)]
    for i in range(n):
        for j in G[i]:
            I[j].append(i)
    vis = [0 for i in range(n)]
    L = []
    for i in range(n):
        if(vis[i] == 0):
            dfs_list(i)
    vis = [0 for i in range(n)]
    cont = 0
    while(len(L)):
        i = L.pop()
        if(vis[i] == 0):
            dfs(i,cont)
            cont +=	1
    return cont

def main():
    global G
    numbers = stdin.readline().strip().split()
    numbers = list(map(int, numbers))
    p = numbers[0]
    t = numbers[1]
    while(p != 0 or t != 0):
        G = [[] for _ in range(p)]
        names = {}
        cont = 0
        for i in range(p):
            person = stdin.readline().strip()
            names[person] = cont
            cont += 1

        for i in range(t):
            person1 = stdin.readline().strip()
            person2 = stdin.readline().strip()
            G[names[person1]].append(names[person2])

        print(solve())
        G.clear()
        numbers = stdin.readline().strip().split()
        numbers = list(map(int, numbers))
        p = numbers[0]
        t = numbers[1]

main()

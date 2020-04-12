#UVA 10496 Collecting Beepers

from sys import stdin

def gen_comp_graph(N, beepers):
	graph = [[0 for _ in range(N)] for _ in range(N)]
	for i in range(N):
		for j in range(i+1, N):
			graph[i][j] = graph[j][i] = abs(beepers[i][0]-beepers[j][0]) + abs(beepers[i][1] - beepers[j][1])
	return graph

def phi(u, S):
    global m, univ, INF, graph, memo
    assert 0 < u < m+1 and S.issubset(univ) and (not(0 in S)) and u in S
    ans, key = None, (u, str(S))
    if key in memo: ans = memo[key]
    else:
        if len(S) == 1: ans = graph[u][0]
        else:
            ans, Swu = INF, S.difference([u])
            for v in Swu:
                ans = min(ans, graph[u][v] + phi(v, Swu))
        memo[key] = ans
    return ans

def solve(size_x, size_y, beepers):
    global m, univ, INF, graph, memo
    memo = dict()
    graph = gen_comp_graph(m+1, beepers)
    univ = set(i for i in range(m+1))
    INF = float('inf')
    ans = INF

    Vw0 = set(i for i  in range(1, m+1))
    for u in Vw0:
    	ans = min(ans, graph[u][0] + phi(u, Vw0))

    return ans

def main():
    global m
    c = int(stdin.readline())
    while c > 0:
        size_x, size_y = map(int, stdin.readline().split())
        x0, y0 = map(int, stdin.readline().split())
        beepers = [(x0,y0)]
        m = int(stdin.readline())
        for _ in range(m):
            i, j = map(int, stdin.readline().split())
            beepers.append((i, j))
        ans = solve(size_x, size_y, beepers)
        print("The shortest path has length {0}".format(ans))
        c -= 1

main()

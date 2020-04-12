#UVA 776 Monkeys in a Regular Forest

from sys import stdin
from collections import deque
import math

#Impresion hecha en colaboracion con Edixon Salas

direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(Graph, node, cont, n, m):
    global vis
    q = deque()
    q.append(node)
    vis[node[0]][node[1]] = cont
    while len(q):
        x, y = q.popleft()
        for i, j in direcciones:
            x1 = x + i
            y1 = y + j
            if(0 <= x1 < n and 0 <= y1 < m and Graph[x1][y1] == Graph[x][y] and vis[x1][y1] == 0):
                vis[x1][y1] = cont
                q.append((x1, y1))
    return

def solve(M):
    global vis
    N, M1 = len(M), len(M[0])
    vis = [[0 for i in range(M1)] for j in range(N)]
    especie = 1
    for i in range(N):
        for j in range(M1):
            if vis[i][j] == 0:
                node = (i, j)
                bfs(M, node, especie, N, M1)
                especie += 1


def main():
    global vis
    s = stdin.readline()
    M = []
    while len(s) > 0:
        line = s.strip('\n').split(" ")
        if line[0] != '%':
            M.append(line)
        else:
            solve(M)
            n = len(vis)
            m = len(vis[0])
            maxCol = []
            max = 0
            for i in range(m):
                for j in range(n):
                    if vis[j][i] > max:
                        max = vis[j][i]
                maxCol.append(max)
                max = 0

            for i in range(n):
                for j in range(m):
                    if(j == 0):
                        tam = maxCol[j]
                        tam = int(math.log(tam, 10)) + 1
                        print(repr(vis[i][j]).rjust(tam), end='')
                    else:
                        tam = maxCol[j]
                        tam = int(math.log(tam, 10)) + 1
                        print(repr(vis[i][j]).rjust(tam + 1), end='')
                print()
            print("%")
            M = []

        s = stdin.readline().strip()
        if len(s) == 0:
            solve(M)
            n = len(vis)
            m = len(vis[0])
            maxCol = []
            max = 0
            for i in range(m):
                for j in range(n):
                    if vis[j][i] > max:
                        max = vis[j][i]
                maxCol.append(max)
                max = 0

            for i in range(n):
                for j in range(m):
                    if(j == 0):
                        tam = maxCol[j]
                        tam = int(math.log(tam, 10)) + 1
                        print(repr(vis[i][j]).rjust(tam), end='')
                    else:
                        tam = maxCol[j]
                        tam = int(math.log(tam, 10)) + 1
                        print(repr(vis[i][j]).rjust(tam + 1), end='')
                print()
            print("%")

main()

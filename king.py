#UVA 11352 Crazy King

from sys import stdin
from collections import deque

dirKing = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
dirHorse = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def bfs(A, B, vis, n, m):
    distancias = [[0 for i in range(int(m))] for j in range(int(n))]
    visitados = [[0 for i in range(int(m))] for j in range(int(n))]
    q = deque()
    vis[A[0]][A[1]] = 1
    distancias[A[0]][A[1]] = 0
    q.append(A)
    while len(q):
        t = q.popleft()
        if t[0] == B[0] and t[1] == B[1]:
            return distancias[B[0]][B[1]]

        global dirKing
        for i, j in dirKing:
            x2 = t[0] + i
            y2 = t[1] + j
            if 0 <= x2 < int(n) and 0 <= y2 < int(m) and visitados[x2][y2] == 0 and vis[x2][y2] != 1:
                visitados[x2][y2] = 1
                distancias[x2][y2] = distancias[t[0]][t[1]] + 1
                v = (x2, y2)
                q.append(v)

    return -1


def solve(Mx, n , m):
    aux = [[0 for i in range(int(m))] for j in range(int(n))]
    A = None
    B = None
    for i in range(int(n)):
        for j in range(int(m)):
            if Mx[i][j] == "Z":
                aux[i][j] = 1
                global dirHorse
                for w, k in dirHorse:
                    x1 = i + w
                    y1 = j + k
                    if 0 <= x1 < int(n) and 0 <= y1 < int(m) and Mx[x1][y1] == ".":
                        aux[x1][y1] = 1
            elif Mx[i][j] == "A":
                A = (i, j)
            elif Mx[i][j] == "B":
                B = (i, j)
    resp = bfs(A, B, aux, n, m)
    if resp == -1:
        print("King Peter, you can't go now!")
    else:
        print("Minimal possible length of a trip is {0}".format(resp))


def main():
    n = int(stdin.readline())
    Mx = []
    for tc in range(n):
        num1, num2 = map(int, stdin.readline().split())
        for i in range(num1):
            line = stdin.readline().strip("\n")
            Mx.append(line)
        solve(Mx, num1, num2)
        Mx = []
main()

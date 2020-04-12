#UVA 10444 Multi-peg Towers of Hanoi

from sys import stdin

tab = None

def solve(N, P):
    global tab
    tab = [ [ 1 for _ in range(P+1) ] for _ in range(N+1) ]
    #Casos Base
    for i in range(N+1):
        tab[i][0] = tab[i][1] = tab[i][2] = 0
        for j in range(P+1):
            tab[0][j] = 0

    #Caso Inductivo
    n, p = 1, 3
    while n != N+1:
        if p == P+1:
            n, p = n+1, 3
        else:
            if n < p:
                tab[n][p] = 2 * n - 1
            elif p == 3:
                tab[n][p] = 2 * tab[n-1][p] + 1
            else:
                pos_min = float('inf')
                for k in range(1, n):
                    x = 2 * tab[k][p] + tab[n-k][p-1]
                    if x >= 0:
                        pos_min = min(pos_min, x)
                tab[n][p] = pos_min
            p += 1


def main():
    global tab
    cont = 1
    solve(200, 20)
    n, p = map(int, stdin.readline().split())
    while n != 0 or p != 0:
        print("Case {0}: {1}".format(cont, tab[n][p]))
        cont += 1
        n, p = map(int, stdin.readline().split())

main()

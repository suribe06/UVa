#UVA 10074 Take the Land

from sys import stdin

def solve(land, m, n):
    aux = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if land[j][i] == 1:
                aux[j][i] = aux[j-1][i] + 1

    max_area = 0
    for i in range(m):
        for j in range(n):
            acum = aux[i][j]
            for k in range(j+1, n):
                if aux[i][j] <= aux[i][k]:
                    acum += aux[i][j]
                else:
                    break
            for k in range(j-1, -1, -1):
                if aux[i][j] <= aux[i][k]:
                    acum += aux[i][j]
                else:
                    break

            max_area = max(acum, max_area)

    return max_area

def main():
    m, n = map(int, stdin.readline().split())
    while m != 0 and n != 0:
        land = []
        for _ in range(m):
            line = stdin.readline().split()
            for i in range(n):
                if line[i] == '1':
                    line[i] = 0
                else:
                    line[i] = 1
            land.append(line)

        print(solve(land, m, n))

        m, n = map(int, stdin.readline().split())

main()

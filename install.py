#UVA 1193 Radar Installation

from sys import stdin
import math

def solve(n, islands):
    ans, i = 0, 0
    while i != n:
        best, i, ans = i, i+1, ans+1
        while i != n and islands[i][0] < islands[best][1]:
            i+=1
    return ans

def main():
    cont = 1
    n, d = map(int, stdin.readline().split())
    while n != 0 and d != 0:
        islands = []
        check = True
        for i in range(n):
            x, y = map(int, stdin.readline().split())
            if d < y:
                check = False
            else:
                h = math.sqrt(d*d - y*y)
                islands.append((x - h, x + h))
        if check == False:
            print("Case {0}: -1".format(cont))
            cont += 1
            stdin.readline()
            n, d = map(int, stdin.readline().split())
        else:
            islands.sort(key=lambda x:x[1])
            ans = solve(n, islands)
            print("Case {0}: {1}".format(cont, ans))
            cont += 1
            stdin.readline()
            n, d = map(int, stdin.readline().split())

main()

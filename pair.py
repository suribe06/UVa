#UVA 10245 The Closest Pair Problem

from sys import stdin
import math

def distance(p1, p2):
    d = 0.0
    d = math.sqrt(pow((p1[0]-p2[0]),2) + pow((p1[1]-p2[1]),2))
    return d

def solve(points):
    ans = float('INF')
    points.sort(key=lambda x:x[0])
    for i in range(len(points)):
        j = i + 1
        flag = True
        while j < len(points) and flag == True:
            if points[i][0] + ans < points[j][0]:
                flag = False
            d = distance(points[i], points[j])
            if d < ans:
                ans = d
            j += 1
    return ans

def main():
    n = int(stdin.readline())
    while n!=0:
        points = list()
        for _ in range(n):
            tok = stdin.readline().split()
            points.append((float(tok[0]), float(tok[1])))
        ans = solve(points)
        if ans >= 10000:
            print("INFINITY")
        else:
            print('{0:.4f}'.format(ans))
        n = int(stdin.readline())

main()

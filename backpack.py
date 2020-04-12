#UVA 907 Winterim Backpacking Trip

from sys import stdin

def check_camp(x, n, k, dist):
    i, camps, sum = 0, 0, 0
    while camps <= k and i < n:
        if sum + dist[i] <= x:
            sum += dist[i]
            i += 1
        else:
            camps += 1
            sum = 0
    return camps <= k

def solve(n, k, dist):
    acum = 0
    for i in dist:
        acum += i

    low, hi = 0, acum
    while low + 1 != hi:
        mid = low + ((hi - low) >> 1)
        if check_camp(mid, n, k, dist):
            hi = mid
        else:
            low = mid

    return hi

def main():
    N,K,dist = None,None,None
    line = stdin.readline()
    while len(line)!=0:
        N,K = map(int, line.split())
        dist = [ int(stdin.readline()) for _ in range(N+1) ]
        print(solve(N+1, K, dist))
        line = stdin.readline()

main()

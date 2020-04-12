#UVA 12321 Gas Stations

from sys import stdin

def minimal_covering_with_failure_2(L, H, s):
    ans, low, n, ok = list(), L, 0, True
    N = len(s)
    while ok and low < H and n != N:
        ok = s[n][0] <= low
        best, n = n, n+1
        while ok and n != N and s[n][0] <= low:
            if s[n][1] > s[best][1]:
                best = n
            n+=1
        ans.append(best)
        low = s[best][1]
    ok = ok and low >= H
    if ok == False:
        ans = list()
    return ans, ok

def solve(road, gas_stations, G):
    ans = None
    l, ok = minimal_covering_with_failure_2(0, road, gas_stations)
    if ok == False:
        ans = -1
    else:
        N = len(l)
        ans = G - N
    return ans

def main():
    road, G = map(int, stdin.readline().split())
    while road != 0 and G != 0:
        gas_stations = []
        for i in range(G):
            x, r = map(int, stdin.readline().split())
            #gas_stations.append((max(x-r, 0), min(x+r, road)))
            gas_stations.append((x-r, x+r))
        gas_stations.sort(key=lambda x:x[0])
        print(solve(road, gas_stations, G))
        road, G = map(int, stdin.readline().split())

main()

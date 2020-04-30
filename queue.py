#UVA 10128 Queue

from sys import stdin

def solve(n, p, r):
    ans = 0
    if n == 1:
        if p == 1 and r == 1:
            ans = 1
    else:
        ans = solve(n-1, p, r)*(n-2) + solve(n-1, p, r-1) + solve(n-1, p-1, r)
    return ans

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        n, p, r = map(int, stdin.readline().split())
        ans = solve(n, p, r)
        print(ans)

main()

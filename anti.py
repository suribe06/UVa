# UVA 11240 Antimonotonicity

from sys import stdin

def solve(n, F):
    ans = 1
    for i in range(1, n):
        if ans%2 == 0 and F[i-1] < F[i]:
            ans += 1
        elif ans%2 == 1 and F[i-1] > F[i]:
            ans += 1
    return ans

def main():
    T = int(stdin.readline())
    for i in range(T):
        line = stdin.readline().split()
        n, F = int(line[0]), []
        for j in range(1, n+1):
            F.append(int(line[j]))
        ans = solve(n, F)
        print(ans)
main()

#UVA 12405 Scarecrow

from sys import stdin

def solve(field, N):
    ans, i = 0, 0
    while i < N:
        if field[i] == ".":
            ans += 1
            i += 3
        else:
            i += 1
    return ans

def main():
    T = int(stdin.readline())
    for i in range(T):
        N = int(stdin.readline())
        field = stdin.readline()
        ans = solve(field, N)
        print("Case {0}: {1}".format(i+1, ans))

main()

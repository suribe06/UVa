from sys import stdin

def solve(g, l):
    ans = None
    if l%g == 0:
        ans = 1
    else:
        ans = 0
    return ans

def main():
    T = int(stdin.readline())
    for i in range(T):
        g, l = map(int, stdin.readline().split())
        ans = solve(g, l)
        if ans == 1:
            print("{0} {1}".format(g, l))
        else:
            print("-1")

main()

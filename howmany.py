#UVA 986 How Many?

from sys import stdin

# d=0 bajada, d=1 subida

def hash(exp):
    ans = None
    if exp == True:
        ans = 1
    else:
        ans = 0
    return ans

def phi(n, k, x, y, r, d, memo):
    ans, key = None, (x, y, r, d)
    if key in memo: ans = memo[key]
    else:
        if x == 2*n:
            exp = (y==0 and r == 0 and d == 0)
            ans = hash(exp)
        else:
            if y == 0:
                ans = phi(n, k, x+1, y+1, r, 1, memo)
            elif y != 0 and (d == 0 or (d == 1 and y != k)):
                ans = phi(n, k, x+1, y+1, r, 1, memo) + phi(n, k, x+1, y-1, r, 0, memo)
            elif y != 0 and d == 1 and y == k and r == 0:
                ans = phi(n, k, x+1, y+1, r, 1, memo)
            elif y != 0 and d == 1 and y == k and r != 0:
                ans = phi(n, k, x+1, y+1, r, 1, memo) + phi(n, k, x+1, y-1, r-1, 0, memo)
        memo[key] = ans
    return ans

def main():
    inp = stdin
    for line in inp.readlines():
        memo = dict()
        num = [int(x) for x in line.strip().split()]
        print(phi(num[0], num[2], 0, 0, num[1], 1, memo))

main()

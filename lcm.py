from sys import stdin
import math

def mcd(a, b):
	ans = None
	if b == 0:
		ans = a
	else:
		ans = mcd(b, a%b)
	return ans

def mcm(a, b):
    ans = a*b // mcd(a, b)
    return ans

def get_divisors(n):
    divisors = {1}
    s = int(math.sqrt(n))
    for i in range(2, s+1):
        if n%i == 0:
            divisors.add(i)
            divisors.add(n//i)
    divisors.add(n)
    return list(divisors)

def solve(n):
    ans = 0
    divs = get_divisors(n)
    for i in range(len(divs)):
        for j in range(i, len(divs)):
            if mcm(divs[i], divs[j]) == n:
                ans += 1
    return ans

def main():
    n = int(stdin.readline())
    while n != 0:
        ans = solve(n)
        print(n, ans)
        n = int(stdin.readline())

main()

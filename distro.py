#UVA 10910 Marks Distribution

from sys import stdin

def binom(n, k, memo):
	assert 0 <= k <= n
	ans, key = None, (n, k)
	if key in memo: ans = memo[key]
	else:
		if k == 0 or k == n: ans = 1 #caso base
		else:
			if n < (k << 1): k = n - k
			ans = binom(n-1, k-1, memo) + binom(n-1, k, memo)
		memo[key] = ans
	return ans

def solve(num, memo):
    
    n, t, p = num[0], num[1], num[2]
    if n*p > t:
    	ans = 0
    else:
    	ans = binom(t-p*n+n-1, n-1, memo)
    return ans

def main():
    c = int(stdin.readline())
    while c > 0:
    	memo = dict()
    	for line in stdin.readlines():
    		num = [int(x) for x in line.strip().split()]
    		print(solve(num, memo))
    	c -= 1

main()

#UVA 11658 Best Coalitions

from sys import stdin

def knapsack(B, m, n, x, memo):
	ans, key = None, (n, m)
	if key in memo: ans = memo[key]
	else:
		if n == 0:
			if m >= 5001: ans = x/m
			else: ans = 0
		else:
			ans = knapsack(B, m, n-1, x, memo)
			ans = max(ans, knapsack(B, m + B[n-1], n-1, x, memo))
		memo[key] = ans
	return ans

def solve(percentages, x, memo):
	percentages.remove(x)
	n = len(percentages)
	ans = knapsack(percentages, x, n, x, memo)
	return round(ans*100, 2)

def main():
	n, m = map(int, stdin.readline().split())
	while n != 0 and m != 0:
		memo = dict()
		percentages = []
		for _ in range(n):
			f = float(stdin.readline().strip())
			f = int(f) * 100 + round(f % 1 * 100)
			percentages.append(f)
		x = percentages[m-1]
		ans = None
		if x > 5000:
			ans = 100.00
		else:
			ans = solve(percentages, x, memo)
		print('{0:.2f}'.format(ans))
		n, m = map(int, stdin.readline().split())

main()

from sys import stdin
import operator

MAX = 1000001
sieve = None
prime = None
differences = []

def build_sieve_opt():
    global sieve, prime, differences
    sieve = [True for _ in range(MAX)]
    sieve[0] = sieve[1] = False
    prime = [2]
    for j in range(4, MAX, 2):
        sieve[j] = False
    for i in range(3, MAX, 2):
        if sieve[i]:
            differences.append(i - prime[-1])
            prime.append(i)
            for j in range(i*i, MAX, i):
                sieve[j] = False

def right(x):
    global prime
    lo = 0
    hi = len(prime)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < prime[mid]: hi = mid
        else: lo = mid + 1
    return lo

def left(x):
    global prime
    lo = 0
    hi = len(prime)
    while lo < hi:
        mid = (lo + hi) // 2
        if prime[mid] < x: lo = mid + 1
        else: hi = mid
    return hi

build_sieve_opt()

def solve(l, u):
    global sieve, differences
    ans, aux = None, None
    if l != u:
        lo = right(l)
        if sieve[l]:
            lo = lo-1
        hi = left(u)
        if sieve[u]:
            hi = hi + 1
        aux = differences[lo:hi-1]
        d = dict()
        for x in aux:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        l = []
        for x in d:
            l.append((x, d[x]))
        if len(l) == 0:
            ans = 0
        elif len(l) == 1:
            ans = l[0][0]
        else:
            l.sort(key=lambda x: x[1], reverse=True)
            if l[0][1] == l[1][1]:
                ans = 0
            else:
                ans = l[0][0]
    else:
        ans = 0
    return ans

def main():
    T = int(stdin.readline())
    for i in range(T):
        l, u = map(int, stdin.readline().split())
        ans = solve(l, u)
        if ans == 0:
            print("No jumping champion")
        else:
            print("The jumping champion is {0}".format(ans))

main()

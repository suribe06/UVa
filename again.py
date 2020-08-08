from sys import stdin

MAX = 10001
sieve = None
prime = None
divis = None
ff = None
facm = [None for _ in range(MAX)]

def build_sieve_opt():
    global sieve, prime, divis
    sieve = [True for _ in range(MAX)]
    divis = [None for _ in range(MAX)]
    sieve[0] = sieve[1] = False
    prime = [2]
    divis[1] = 1; divis[2] = 2
    for j in range(4, MAX, 2):
        sieve[j] = False
        divis[j] = 2
    for i in range(3, MAX, 2):
        if sieve[i]:
            divis[i] = i
            prime.append(i)
            for j in range(i*i, MAX, i):
                sieve[j] = False
                divis[j] = i

def union_dictionaries(d1, d2):
    for x in d2:
        if x in d1:
            d1[x] += d2[x]
        else:
            d1[x] = d2[x]
    return d1

def factorial_factors():
    global ff
    ff = [None for _ in range(MAX)]
    ff[1] = dict({1:1})
    ff[2] = dict({2: 1})
    facm[2] = dict({2: 1})
    for i in range(3, MAX):
        d = factorout(i)
        facm[i] = d
        aux = dict(ff[i-1])
        r = union_dictionaries(aux, d)
        ff[i] = r

def factorout(n):
    global divis
    ans = dict()
    while n != 1:
        d, k = divis[n], 0
        while n%d == 0:
            n = n // d
            k += 1
        ans[d] = k
    return ans

build_sieve_opt()
factorial_factors()

def solve(m, n):
    ans, flag = 0, None
    fn = ff[n]
    fm = facm[m]
    Sn = set(fn.keys())
    Sm = set(fm.keys())
    flag = Sm.issubset(Sn)
    if flag == False:
        ans = 0
    else:
        ans = float('inf')
        for x in fm:
            aux = fn[x] // fm[x]
            ans = min(ans, aux)
    return ans

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        m, n = map(int, stdin.readline().split())
        ans = solve(m, n)
        print("Case {0}:".format(i+1))
        if ans == 0:
            print("Impossible to divide")
        else:
            print(ans)

main()

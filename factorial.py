from sys import stdin

MAX = 1000001
sieve = None
prime = None
divis = None
ff = None

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

def factorout(n):
    global divis
    ans = 0
    while n != 1:
        d, k = divis[n], 0
        while n%d == 0:
            n = n // d
            k += 1
        ans += k
    return ans

def factorial_factors():
    global ff
    ff = [None for _ in range(MAX)]
    ff[2] = 1
    for i in range(3, MAX):
        x = factorout(i)
        ff[i] = ff[i-1] + x

build_sieve_opt()
factorial_factors()

def main():
    global ff
    line = stdin.readline().strip()
    while len(line) != 0:
        n = int(line)
        ans = ff[n]
        print(ans)
        line = stdin.readline().strip()

main()

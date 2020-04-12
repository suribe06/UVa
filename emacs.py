#UVA 12785 Emacs Plugin

from sys import stdin

def failure(A):
    M = len(A)
    fail = [-1 for i in range(M)]
    i = 1
    if len(fail) != 1 : fail[1] = 0; i += 1
    while i < len(fail):
        j = 0
        k = True
        while fail[i-1]-j != -1 and k:
            if(A[fail[i-1]-j] == A[i-1]):
                k = False
                fail[i] = fail[i-1] + (1-j)
            j += 1
        if k: fail[i] = 0
        i += 1
    return fail

def kmp(T, P):
    global i
    N = len(T)
    M = len(P)
    fail = failure(P)
    flag = True
    j = 0
    while i < N and flag:
        if T[i] == P[j]:
            j += 1
            if j == M:
                flag = False
        else:
            while j >= 0 and P[j] != T[i]:
                j = fail[j]
            j+=1
        i+=1
    return not flag

def solve(T, P):
    global i
    P = P.split("*")
    ans = True
    i = 0
    w = 0
    while w < len(P):
        if len(P[w]) != 0:
            r = kmp(T, P[w])
            ans = ans and r
        w += 1
    return ans

def main():
    n = stdin.readline().strip()
    while n != "":
        n = int(n)
        t = stdin.readline().strip()
        for i in range(n):
            p = stdin.readline().strip()
            ans = solve(t, p)
            if ans:
                print("yes")
            else:
                print("no")
        n = stdin.readline().strip()
main()

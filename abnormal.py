#UVA 11888 Abnormal 89's

from sys import stdin

def failure(A):
    M = len(A)
    fail = [None for _ in range(M)]
    j = 0
    for i in range(1, M):
        fail[i] = j
        while  j > 0 and A[i] != A[j]:
            j = fail[j]
        j += 1
    return fail

def kmp(T, P):
    global i
    T = " " + T
    P = " " + P
    N = len(T)
    M = len(P)
    j = 1
    fail = failure(T)
    while i < M:
        while j > 0 and T[i] != P[j]:
            j = fail[j]
        if j == M - 1: #found it
            return True
        j += 1
        i += 1
    return False

def solve(words):
    return

def main():
    data = stdin.readline().strip()
    while data != "":
        n = int(data)
        words = []
        for i in range(n):
            w = stdin.readline().strip()
            words.append(w)
        solve(words)
        data = stdin.readline().strip()

main()

#UVA 10810 Ultra-QuickSort

from sys import stdin

swaps = 0

def merge(A,B):
    global swaps
    c = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            swaps += len(A) - i
            j += 1

    c += A[i:]
    c += B[j:]
    return c

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) >> 1
        a = mergesort(arr[:mid])
        b = mergesort(arr[mid:])
        return merge(a,b)

def solve(num):
    global swaps
    swaps = 0
    mergesort(num)
    return swaps

def main():
  n = int(stdin.readline().strip())
  while n!=0:
    num = [ int(stdin.readline()) for _ in range(n) ]
    print(solve(num))
    n = int(stdin.readline().strip())

main()

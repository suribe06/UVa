#UVA 10327 Flip Sort

from sys import stdin

inversiones = 0

def merge(A,B):
    c = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            global inversiones
            inversiones += len(A) - i
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

def solve(num, low, hi):
  global inversiones
  inversiones = 0
  mergesort(num)
  return inversiones

def main():
  inp = stdin
  s = inp.readline()
  lab = "Minimum exchange operations : {0}"
  while len(s)>0:
    n = int(s)
    num = [int(x) for x in inp.readline().strip().split()]
    print(lab.format(solve(num, 0, n)))
    s = inp.readline().strip()

main()

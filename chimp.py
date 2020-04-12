# UVA 10611 The Playboy Chimp

from sys import stdin

def left(ladies, x):
    mn = ''
    lo = 0
    hi = len(ladies)
    while lo < hi:
        mid = (lo + hi) // 2
        if ladies[mid] < x: lo = mid + 1
        else: hi = mid

    if lo == 0:
      mn = 'X'
    else:
      mn = str(ladies[lo - 1])
    return mn

def right(ladies, x):
    mx = ''
    lo = 0
    hi = len(ladies)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < ladies[mid]: hi = mid
        else: lo = mid + 1

    if lo >= len(ladies):
      mx = 'X'
    else:
      mx = ladies[lo]
    return mx

def solve(ladies, x):
    a = left(ladies, x)
    b = right(ladies, x)
    print(str(a) + " " + str(b))

def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries: solve(ladies, x)

main()

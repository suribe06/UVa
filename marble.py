#UVA 10474 Where Is the Marble?

from sys import stdin

marble,lenm,ans = None,None,-1

def binary_search (low, hi, x):
    global ans
    if low <= hi:
        mid = low + ((hi - low) >> 1)
        if marble[mid] == x:
            ans = mid
        if x <= marble[mid]:
            return binary_search(low, mid-1, x)
        else:
            return binary_search(mid + 1, hi, x)
    else:
        return None

def main():
  global marble,lenm,ans
  inp = stdin
  cas = 1
  lenm,lenq = [ int(x) for x in inp.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(inp.readline()) for i in range(lenm) ]
    marble.sort()
    print('CASE# {0}:'.format(cas))
    for q in range(lenq):
      ans = -1
      x = int(inp.readline())
      binary_search(0, len(marble)-1, x)
      if ans==-1:
          print('{0} not found'.format(x))
      else:
          print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in inp.readline().split() ]
    cas += 1

main()

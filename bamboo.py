#UVA 12032 The Monkey and the Oiled Bamboo

from sys import stdin

def solve(num, n):
  ans = 0
  k = 0
  for i in range(1, len(num)):
      diferencia = num[i] - num[i - 1]
      if diferencia > k:
          k = diferencia
  ans = k
  return ans

def main():
  tcnt = int(stdin.readline())
  for tc in range(1, tcnt+1):
    n = int(stdin.readline())
    num = [ int(x) for x in stdin.readline().split() ]
    print('Case {0}: {1}'.format(tc, solve(num, n)))

main()

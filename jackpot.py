#UVA 10684 The Jackpot

from sys import stdin

MAX = 10010
bet = [None for i in range(10010)]

def solve(low,hi):
  max, temp = 0, 0
  for i in range(0, hi):
      temp += int(bet[i])
      if temp > max:
          max = temp
      if temp < 0:
          temp = 0
  return max

def main():
  global bet
  inp = stdin
  n = int(inp.readline().strip())
  while n!=0:
    tok = inp.readline().strip().split()
    for i in range(n): bet[i] = int(tok[i])
    ans = solve(0,n)
    if ans<=0: print('Losing streak.')
    else: print('The maximum winning streak is {0}.'.format(ans))
    n = int(inp.readline().strip())
main()

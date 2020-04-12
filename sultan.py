#UVA 12582 Wedding of Sultan

from sys import stdin

def solve(cad):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    conts = [0 for _ in range(0, 26)]
    stack = []
    stack.append(cad[0])
    for i in range(1, len(cad)-1):
        if stack[-1] == cad[i]:
            stack.pop()
        else:
            conts[ord(cad[i]) - 65] += 1
            conts[ord(stack[-1]) - 65] += 1
            stack.append(cad[i])

    for i in range(0,26):
        if conts[i] != 0:
            print('{0} = {1}'.format(letters[i], conts[i]))
    if len(cad) == 2:
        print('{0} = {1}'.format(cad[0], 0))

def main():
  n = int(stdin.readline())
  for tc in range(1, n+1):
    cad = stdin.readline().strip("\n")
    print('Case {0}'.format(tc))
    solve(cad)

main()

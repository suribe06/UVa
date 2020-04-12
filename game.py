#UVA 12640 Largest Sum Game

from sys import stdin

def solve(num):
    r = 0
    max_sum = 0
    for i in num:
        r += i
        if r < 0:
            r = 0
        else:
            max_sum = max(r, max_sum)
        
    return max_sum

def main():
    inp = stdin
    for line in inp.readlines():
        num = [int(x) for x in line.strip().split()]
        print(solve(num))

main()

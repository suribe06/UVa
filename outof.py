#UVA 10344 23 out of 5

from sys import stdin
from collections import deque

def backtracking(numbers, n, x):
    global ans
    if n == 1:
        if numbers[0] == x:
            ans = True
            return
    else:
        i = 0
        while i < len(numbers):
            first = numbers[0]
            numbers.popleft()
            backtracking(numbers, n-1, x-first)
            backtracking(numbers, n-1, x+first)
            if x % first == 0:
                backtracking(numbers, n-1, x//first)
            numbers.append(first)
            i += 1

def solve(numbers):
    global ans
    ans = False
    backtracking(numbers, 5, 23)
    return ans

def main():
    line = stdin.readline().split()
    while line != ['0', '0', '0', '0', '0']:
        numbers = deque([int(x) for x in line])
        ans = solve(numbers)
        if ans:
            print("Possible")
        else:
            print("Impossible")
        line = stdin.readline().split()

main()

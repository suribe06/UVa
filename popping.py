#UVA 1261 String Popping

from sys import stdin

ans = False
def solve(string):
    global ans
    N = len(string)
    if N == 0:
        ans = True
    elif N == 1:
            ans = False
    elif N == 2:
        if string[0] != string[1]:
            ans = False
        else:
            ans = True
    else:
        i = 0
        while i < N and not(ans):
            j = i
            while j < N and string[i] == string[j]:
                j += 1
            if j - i >= 2:
                x = list(string)
                del x[i:j]
                solve(x)
            i = j-1
            i += 1

def main():
    global ans
    cases = int(stdin.readline())
    for i in range(cases):
        line = stdin.readline().strip()
        string = []
        for x in line:
            string.append(x)
        ans = False
        solve(string)
        if ans == True:
            print("1")
        else:
            print("0")

main()

#UVA 10950 Bad Code

from sys import stdin

def backtracking(psol, indexString):
    global string, all_sols, letters, A, X, cont
    if cont == 100:
        return
    else:
        if indexString == X:
            cont += 1
            all_sols.append(list(psol))
        else:
            indexString2 = indexString
            for k in range(len(letters)):
                l = letters[k]
                s = A[l]
                n = len(s)
                flag = True
                while indexString != X and flag:
                    if string[indexString] == '0':
                        indexString += 1
                    else:
                        flag = False

                if string[indexString:indexString+n] == s:
                    x = list(psol)
                    x.append(l)
                    backtracking(x, indexString+n)
                indexString = indexString2

def solve(N):
    global A, string, letters, all_sols, X, cont
    all_sols, X, cont = [], len(string), 0
    backtracking([], 0)
    for i in range(len(all_sols)):
        s = ""
        for x in all_sols[i]:
            s += x
        print(s)

def main():
    global A, string, letters
    N = int(stdin.readline())
    cases = 1
    while N != 0:
        A = dict()
        letters = []
        for i in range(N):
            x = stdin.readline().split()
            letters.append(x[0])
            A[x[0]] = x[1]
        letters.sort()
        string = stdin.readline().strip()
        print("Case #{0}".format(cases))
        solve(N)
        print()
        cases += 1
        N = int(stdin.readline())

main()

#UVA 10460 Find the Permuted String

from sys import stdin

factorials = [1, 1]
for i in range(2, 27):
    factorials.append(factorials[i-1]*i)

def p(string, i, aux, index):
    global ans, cont, factorials, f
    if len(aux) == len(string):
        cont += 1
        if cont == index:
            ans = aux
            return
    elif ans == "" and i < len(string):
        for j in range(len(aux) + 1):
            aux2 = aux[:j] + string[i] + aux[j:]
            val = f / factorials[len(aux2)] + cont
            if val >= index:
                p(string, i+1, aux2, index)
            else:
                cont = val

def solve(string, index):
    global ans, cont, factorials, f
    ans, cont, f = "", 0, factorials[len(string)]
    p(string, 0, "", index)
    return ans

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        string = stdin.readline().strip()
        index = int(stdin.readline())
        ans = solve(string, index)
        print(ans)

main()

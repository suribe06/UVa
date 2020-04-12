#UVA 10701 Pre, in and post

from sys import stdin

def solve(preOrder, startPre, endPre, inOrder, startIn, endIn):
    global ans
    if(startPre > endPre or startIn > endIn):
        return
    ind = inOrder.index(preOrder[startPre])
    solve(preOrder, startPre + 1, startPre + ind - startIn, inOrder, startIn, ind - 1)
    solve(preOrder, startPre + ind - startIn + 1, endPre, inOrder, ind + 1, endIn)
    ans += preOrder[startPre]


def main():
    global ans
    c = int(stdin.readline())
    while c > 0:
        s = stdin.readline().split()
        numNodes = int(s[0])
        preOrder = s[1]
        inOrder = s[2]
        ans = ""
        solve(preOrder, 0, numNodes-1, inOrder, 0, numNodes-1)
        print(ans)
        c -= 1

main()

#UVA 10308 Roads in the North

from sys import stdin
from collections import deque

def dfs(u, val):
	global tree, maxD, vis
	tmpmax = 0
	for v in tree[u]:
		if vis[v[0]] == 0:
			vis[v[0]] = 1
			tmp = dfs(v[0], v[1])
			maxD = max(maxD,tmpmax + tmp)
			tmpmax = max(tmpmax,tmp)

	return tmpmax + val


def makeTree(arr):
    tree = {}
    for i in range(len(arr)):
        nd1 = arr[i][0]
        nd2 = arr[i][1]
        dis = arr[i][2]

        if nd1 not in tree:
            tree[nd1] = []
            tree[nd1].append((nd2, dis))
        else:
            tree[nd1].append((nd2, dis))
        if nd2 not in tree:
            tree[nd2] = []
            tree[nd2].append((nd1, dis))
        else:
            tree[nd2].append((nd1, dis))

    return tree

def solve(aux):
    global tree, vis, maxD
    tree = makeTree(aux)
    vis = {u: 0 for u in tree}
    maxD = 0
    keys = list(tree.keys())
    node = keys[0]
    vis[node] = 1
    dfs(node, 0)

    return maxD


def main():
    aux = []
    line = stdin.readline()
    while len(line) != 0:
        if len(line) == 1:
            print(solve(aux))
            aux = []
        else:
            line = line.strip().split()
            line = list(map(int, line))

            aux.append(line)

        line = stdin.readline()
    if len(line) == 0:
        print(solve(aux))

main()

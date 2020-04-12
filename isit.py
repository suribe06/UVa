#UVA 615 Is It a Tree?

from sys import stdin

s = stdin.read()

def dfs(u):
    global visited, tree
    visited[u] = 1

    for v in tree[u]:
        if v not in tree:
            visited[v] = 1
        else:
            if visited[v] == 0:
                dfs(v)

def build_tree(E):
    global visited
    n = len(E)
    tree = {}
    indeg = {}
    visited = {}

    for i in range(n):
        if E[i][0] not in tree:
            tree[E[i][0]] = []
            tree[E[i][0]].append(E[i][1])
        else:
            tree[E[i][0]].append(E[i][1])

        if E[i][0] not in visited:
            visited[E[i][0]] = 0

        if E[i][1] not in visited:
            visited[E[i][1]] = 0

        if E[i][0] not in indeg:
            indeg[E[i][0]] = 0

        if E[i][1] not in indeg:
            indeg[E[i][1]] = 0

        indeg[E[i][1]] += 1

    return tree, indeg

def next_in():
    global i, s
    while not s[i].isdigit() and s[i] != '-':
        i += 1
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    ans = int(s[i:j])
    i = j
    return ans

i = 0

def solve(E):
    global visited, tree
    ans = "is a tree."
    t = build_tree(E)
    tree = t[0]
    indeg = t[1]

    num_root = 0
    flag_parent = True

    for key, value in indeg.items():
        if value == 0:
            num_root += 1
        if value > 1:
            flag_parent = False

    root = 0
    if num_root == 1:
        for key, value in indeg.items():
            if value == 0:
                root = key

    if flag_parent == True and num_root == 1:
        dfs(root)

    flag_path = True
    for key, value in visited.items():
        if value == 0:
            flag_path = False

    if num_root == 0 or num_root > 1 or flag_parent == False or flag_path == False:
        ans = "is not a tree."

    if len(tree) == 0:
        ans = "is a tree."

    return ans

def main():
    global i
    i = 0
    cont = 0
    a, b = next_in(), next_in()
    while a >= 0 or b >= 0:
        cont += 1
        E = []
        while a > 0 or b > 0:
            E.append((a, b))
            a, b = next_in(), next_in()
        a, b = next_in(), next_in()
        print("Case {0} {1}".format(cont, solve(E)))

main()

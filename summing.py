#UVA 112 Tree Summing

from sys import stdin

def next_int(dq):
    global i, s
    flagMinus = False
    while not s[i].isdigit() and s[i] != '-':
        if s[i] == '-':
            flagMinus = True
        i += 1
        my_pop(dq)
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
        my_pop(dq)
    if flagMinus:
        ans = int(s[i:j]) * -1
        flagMinus = False
    else:
        ans = int(s[i:j])
    i = j
    while s[i] != '(':
        i += 1
        my_pop(dq)
    return ans

i = 0

def next(dq):
    return dq[0]

def my_pop(dq):
    return dq.popleft()

def parse(dq):
    assert my_pop(dq) == '('
    PI = PD = 0
    num = next_int(dq)
    print(num)
    tree = []
    tree.append(num)
    while next(dq) != ')':
        x = parse(dq)
        tree.append(x)
    my_pop(dq)
    return tree

#if PI == PD:
    #solve(n, tree)

def solve(n, tree):
	stack = []
	stack.append((tree, tree[0]))
	flag = False
	while stack and flag == False:
		t, v = stack.pop()
		if len(t[1]) == 0 and len(t[2]) == 0 and v == n:
			flag = True
		else:
			if len(t[1]) != 0:
				stack.append((t[1], v + t[1][0]))
			if len(t[2]) != 0:
				stack.append((t[2], v + t[2][0]))

	return flag

tree = [5, [4, [11, [7, [], []], [2, [], []]], []], [8, [13, [], []], [1, [], []]]]

if len(tree) != 0:
    if solve(22, tree):
        print("yes")
    else:
        print("no")
else:
	print("no")

#def main():
    #return

#main()

#print(next_int(dq))
#print(parse(deque(s[i:])))

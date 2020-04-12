#UVA 668 Parliament

from sys import stdin
array = []
array.append(2)
for i in range(3, 10000):
    array.append(i+array[i-3])

def solve(N):
    global array
    ans, i, flag = [], 0, True
    while i < N and flag:
        ans.append(i+2)
        if array[i] >= N:
        	flag = False
        i += 1
    n = array[len(ans)-1]
    if n - 1 == N:
        ans.append(len(ans) + 2)
        del ans[len(ans)-2]
        del ans[0]
    elif n > N:
        x = array[len(ans)-1] - N
        ans.remove(x)
    else:
        pass
    return ans

def main():
    M = int(stdin.readline())
    while M != 0:
        stdin.readline()
        N = int(stdin.readline())
        ans = solve(N)
        print(*ans)
        if M > 1:
            print()
        M -= 1
main()

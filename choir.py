#UVA 12485 Perfect Choir

from sys import stdin

def solve(notes, sum, N):
    ans, i , average = 0, 0, int(sum/N)
    while i < N and notes[i] < average:
        ans = ans + average - notes[i]
        i += 1
    return ans + 1

def main():
    N = stdin.readline()
    while len(N) != 0:
        N = int(N)
        sum = 0
        notes = []
        line = stdin.readline().split()
        for x in line:
            sum += int(x)
            notes.append(int(x))
        if sum % N == 0:
            print(solve(notes, sum, N))
        else:
            print(-1)
        N = stdin.readline()

main()

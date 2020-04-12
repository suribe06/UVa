#UVA 12532 Interval Product

from sys import stdin

class SegmentTree:
    def __init__(self, A):
        n_hojas = 1
        while n_hojas < len(A):
            n_hojas *= 2

        self.tree = [0 for i in range(2 * n_hojas)]
        self.tree[0] = 'BASURA'
        for i in range(len(A)):
            self.tree[i + n_hojas] = A[i]

        for i in range(n_hojas - 1, 0, -1):
            self.tree[i] = self.tree[2*i] * self.tree[2*i+1]

        self.n_hojas = n_hojas
        return

    def suma(self, lo, hi, i=1):
        if lo == hi:
            ans = 1
        else:
            ans = self._suma(lo, hi, i=1, L=0, R=self.n_hojas)
        return ans

    def _suma(self, lo, hi, i, L, R):
        assert L <= lo < hi <= R
        M = (L + R) // 2
        if L == lo and R == hi:
            ans = self.tree[i]
        elif hi <= M: #Recurro sobre hijo izquierdo
            ans = self._suma(lo, hi, 2*i, L, M)
        elif lo >= M: #Recurro sobre hijo derecho
            ans = self._suma(lo, hi, 2*i+1, M, R)
        else:
            ans = self._suma(lo, M, 2*i, L, M)
            ans *= self._suma(M, hi, 2*i+1, M, R)

        return ans

    def set(self, i, val):
        i = i + self.n_hojas
        self.tree[i] = val
        while i != 1:
            pa = i // 2
            self.tree[pa] = self.tree[2*pa] * self.tree[2*pa+1]
            i = pa
        return

    def printTree(self):
        print(self.tree)
        return

def main():
    data = stdin.readline().strip()
    while data != "":
        n, k = map(int, data.split())
        sequence = stdin.readline().split()
        interval = []
        for i in range(len(sequence)):
            interval.append(int(sequence[i]))

        S = SegmentTree(interval)
        ans = ""
        for l in range(k):
            data2 = stdin.readline().split()
            command, i, j = data2[0], int(data2[1]), int(data2[2])
            if command == 'P':
                product = None
                product = S.suma(i - 1, j )

                if product > 0:
                    ans += "+"
                elif product == 0:
                    ans += "0"
                elif product < 0:
                    ans += "-"

            elif command == 'C':
                S.set(i-1, j)

        print(ans)
        data = stdin.readline().strip()

main()

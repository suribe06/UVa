#UVA 10034 Freckles

from sys import stdin
import math

#Se utiliza el codigo de kruskal de AGRA 2018-2

class dforest(object):
  """Disjoint-Union implementation with disjoint forests using path
  compression and ranking"""

  def __init__(self, size=100):
    """create an empty disjoint forest"""
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 0 for _ in range(size) ]

  def __str__(self):
    """return the string representation"""
    return str(self.__parent)

  def find(self, x):
    """return the representative of x"""
    if self.__parent[x]!=x: self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self, x, y):
    """perform the union of the collections where x and y belong"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      krx,kry = self.__rank[rx],self.__rank[ry]
      if krx>=kry:
        self.__parent[ry] = rx
        if krx==kry: self.__rank[rx] += 1
      else:
        self.__parent[rx] = ry

def kruskal(G, lenv):
  ans = list()
  G.sort(key=lambda x: x[2])
  df = dforest(lenv)
  sum = 0

  for u,v,w in G:
    if df.find(u)!=df.find(v):
      ans.append((u, v, w))
      df.union(u, v)
      sum += w
  return sum

def main():
    cases = int(stdin.readline())
    while cases > 0:
        stdin.readline()
        n = int(stdin.readline())
        G = []
        disX = [None for _ in range(n)]
        disY = [None for _ in range(n)]
        for i in range(n):
            x , y = map(float, stdin.readline().split())
            disX[i] = x
            disY[i] = y

        i = 0
        while i < n:
            j = i + 1
            while j < n:
                d = math.sqrt(pow(disY[j] - disY[i], 2) + pow(disX[j] - disX[i], 2))
                G.append((i, j, d))
                G.append((j, i, d))
                j += 1
            i += 1

        ans = kruskal(G, n)
        print('{0:.2f}'.format(ans))
        if cases != 1:
            print()

        cases -= 1;

main()

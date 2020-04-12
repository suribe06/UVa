#UVA 11747 Heavy Cycle Edges

from sys import stdin

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

  for u,v,w in G:
    if df.find(u)!=df.find(v):
      df.union(u, v)
    else:
        ans.append(w)

  return ans

def main():
    n , m = map(int, stdin.readline().split())
    while n != 0 or m != 0:
        G = []
        for i in range(m):
            u, v, d = map(int, stdin.readline().split())
            G.append((u, v, d))

        ans = kruskal(G, n)
        if len(ans) == 0:
            print("forest")
        else:
            for i in ans:
                print(i, end = " ")
                print()

        n , m = map(int, stdin.readline().split())

main()

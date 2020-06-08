import math
import string
import collections
from collections import Counter
from collections import deque
from decimal import Decimal
import sys
import fractions


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


def divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


# coordinates
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
n = int(input())
g = [None]*n
for i in range(n):
    g[i] = readints()
# print(g)
G = [None]*n
for i in range(n):
    G[i] = []
# print(G)
for i in range(n):
    if len(g[i]) >= 3:
        for j in range(2, len(g[i])):
            # print(g[i][j])
            G[i].append(g[i][j])
#print('G', G)
dist = [-1]*n
dist[0] = 0
d = deque()
d.append(0)
# print(d)
while(len(d) != 0):
    v = d.popleft()
    if G[v] != []:
        for nv in G[v]:
            if dist[nv-1] != -1:
                continue
            dist[nv-1] = dist[v]+1
            d.append(nv-1)
for i in range(n):
    print(i+1, dist[i])

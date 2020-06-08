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
R, C = map(int, input().split())  # R行C列
sy, sx = map(int, input().split())  # スタート地点の座標
gy, gx = map(int, input().split())  # ゴール地点の座標
c = [None]*R
# print(c)
for i in range(R):
    c[i] = input()
#print('c', c)
d = deque()
d.append((sy-1, sx-1))
# print(d)
dist = [-1]*R
# dist[i][j]には(0,0)から(i,j)までの距離が入る
# -1で初期化しておく
for i in range(R):
    dist[i] = [-1]*C
# print(dist)
dist[sy-1][sx-1] = 0
while(len(d) != 0):
    r, cc = d.popleft()  # 先頭から要素を1つ削除し,その要素を返す
    #print(r, cc)
    # print(c[r][cc])
    if c[r][cc] == '.':
        if r != 0 and dist[r-1][cc] == -1:  # 上
            dist[r-1][cc] = dist[r][cc]+1
            d.append((r-1, cc))
        if r != R-1 and dist[r+1][cc] == -1:  # 下
            dist[r+1][cc] = dist[r][cc]+1
            d.append((r+1, cc))
        if cc != 0 and dist[r][cc-1] == -1:  # 左
            dist[r][cc-1] = dist[r][cc]+1
            d.append((r, cc-1))
        if cc != C-1 and dist[r][cc+1] == -1:  # 右
            dist[r][cc+1] = dist[r][cc]+1
            d.append((r, cc+1))
    if r == gy-1 and cc == gx-1:
        print(dist[r][cc])
        break

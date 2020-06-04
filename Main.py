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
n, m = map(int, input().split())  # 頂点数と辺数
#print(n, m)
# グラフ入力受け取り（無効グラフを想定）
g = [[] for _ in range(n)]
# print(g)
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
#print('g', g)
dist = [-1]*n
# dist[i]はスタート頂点から頂点iまで何ステップで到達できるかを表す
# -1で初期化しておく
d = deque()  # その時点で発見済みだが未訪問な頂点を格納するキュー
dist[0] = 0  # 初期条件（頂点0を初期ノードとする）
d.append(0)  # 0は発見済みだが未訪問の頂点
# BFS開始（dが空っぽになるまで）
while(len(d) != 0):
    # print(d)
    v = d.popleft()  # キューから先頭頂点を取り出す
    # 指定した位置の要素を削除し,値を取得
    # vから辿れる頂点を全て調べる
    #print('v', v)
    #print('g[v]', g[v])
    for nv in g[v]:
        # print(nv)
        if (dist[nv] != -1):  # すでに発見済みの頂点は探索しない
            continue
        dist[nv] = dist[v]+1  # 新たな頂点nvについて距離情報を更新してキューに追加する
        d.append(nv)
# 各頂点の0からの距離
for i in range(n):
    print(i, ':', dist[i])

# 入力
# 9 13
# 0 1
# 0 4
# 0 2
# 1 4
# 1 3
# 1 8
# 2 5
# 3 8
# 4 8
# 5 8
# 5 6
# 3 7
# 6 7

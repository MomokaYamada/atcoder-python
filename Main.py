import math
import string


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


def complete_time(children, x):
    # ここに追記して再帰関数を実装する
    # ベースケース
    if len(children[x]) == 0:
        return 0  # 子組織がないような組織について,報告書が揃う時刻は0
    # 再帰ステップ
    max_receive_time = 0  # 受けとった時刻の最大値
    # x番の組織の子組織についてループ
    receive_time = 0
    for c in children[x]:
        # （子組織cのもとに揃った時刻+1）の時刻にcからの報告書を受け取る
        receive_time = complete_time(children, c)+1
        # 受け取った時刻の最大値=揃った時刻　なので最大値を求める
        max_receive_time = max(max_receive_time, receive_time)
    return max_receive_time


N = int(input())
p = readints()  # 各組織の親組織を示す配列
# print(p)
p.insert(0, -1)  # 0番目の親組織は存在しないので-1を入れておく
# print(p)
# 組織の関係から2次元配列を作る（理解しなくてもいい）
children = [[] for i in range(N)]  # ある組織の子組織の番号一覧
parent = 0
for i in range(1, N):
    parent = p[i]  # i番の親組織の番号
    children[parent].append(i)  # parentの子組織一覧にi番を追加
# print(children)
print(complete_time(children, 0))

# x番の組織について,子組織からの報告書が揃った時刻を返す
# childrenは組織の関係を表す2次元配列

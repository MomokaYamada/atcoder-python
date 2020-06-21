from copy import deepcopy
import math
import string
import collections
from collections import Counter
from collections import deque
from decimal import Decimal
import sys
import fractions
from operator import itemgetter
import itertools
import copy


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


def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a


# coordinates
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def binary_search(list, item):
    low = 0  # listの一番最初
    high = len(list)-1  # listの一番最後
    while(low <= high):  # 一つの要素に絞り込まれるまでの間は...
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None  # アイテムが存在しない


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))

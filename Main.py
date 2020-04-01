import math
import string
import collections
from collections import Counter


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

program = input()
memory = [0]*10000000
i = 0
j = 0
loop = [None]*(len(program))
tmp = []
cnt = 0
for i in range(len(program)):
    if program[i] == '[':
        tmp.append(i)
for i in reversed(range(len(program))):
    if program[i] == ']':
        loop[tmp[cnt]] = i
        loop[i] = tmp[cnt]
        cnt += 1


while(i < len(program)):
    if program[i] == '+':
        if memory[j] == 255:
            memory[j] = 0
        else:
            memory[j] += 1
    elif program[i] == '-':
        if memory[j] == 0:
            memory[j] = 255
        else:
            memory[j] -= 1
    elif program[i] == '>':
        j += 1
    elif program[i] == '<':
        j -= 1
    elif program[i] == '.':
        print(chr(memory[j]), end='')
    elif program[i] == '[':
        if memory[j] == 0:
            i = loop[i]
    elif program[i] == ']':
        i = loop[i]
        i -= 1
    i += 1
# print(memory)

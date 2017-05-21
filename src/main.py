"""main file."""
# coding=utf-8
import time
import random


def getk(x1, x2, y1, y2):
    """Get k."""
    if x1 == x2:
        k = 9999
    else:
        k = (y1 - y2) / (x1 - x2)
    return k


def gety(x, x1, x2, y1, y2):
    """Get y value."""
    y = ((y2-y1) * (x - x1) / (x2 - x1)) + y1
    return y


def gettag(n, T):
    """Get tags location."""
    a = [1] * n
    for i in range(n):
        a[i] = [random.randint(0, T), random.randint(0, T)]
        time.sleep(1)
        return a[i]


a1 = gettag(1, 50)
print("a1", a1)
# set follow
b = [0, 0]
bx = b[0]
# b_tmp = []
# n = 50
times = 0
k = 0.5
while times != 100:
    if k > 0:
        bx = bx + 1
    else:
        bx = bx - 1
    by = gety(bx, a1[0], a1[1], bx, b[0])
    print("b", bx, by)
    k = getk(bx, a1[0], by, a1[1])
    times += 1

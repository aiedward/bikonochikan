"""main file."""
# coding=utf-8
# import time
import random


def gettag(n, T):
    """Get tags location."""
    a = [1] * n
    for i in range(n):
        a[i] = [random.randint(0, T), random.randint(0, T)]
        # time.sleep(1)
        return a[i]


counts = 0
while counts != 10:
    a1 = gettag(1, 50)
    # set follow
    b = [0, 0]
    bx = b[0]
    by = b[1]
    # b_tmp = []
    # n = 50
    times = 0
    k = 0.5
    counts = int(1.3 * max(abs(a1[0] - bx), abs(a1[1] - by)))
    while times <= counts:
        if (a1[0] - bx) > 0:
            bx = bx + 1
        else:
            bx = bx - 1
        if (a1[1] - by) > 0:
            by = by + 1
        else:
            by = a1[1] - 1
        # by = gety(bx, a1[0], a1[1], bx, b[0])
        if max(abs(a1[0] - bx), abs(a1[1] - by)) < 1:
            break
        times += 1
    print("len", counts)
    print("b", bx, by)
    print("a1", a1)
    counts += 1

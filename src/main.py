"""main file."""
# coding=utf-8
# import time
import random


def getv(d, safe_d):
    """Calculate the speed."""
    v = 10 * (d / safe_d)  # 從循環的角度來看相當於變加速
    return v


def gettag(n, T):
    """Get tags location."""
    point = [1] * n
    for i in range(n):
        point[i] = [random.randint(0, T), random.randint(0, T)]
        # time.sleep(0.5)
        return point[i]


def follow(x1, y1, x2, y2, xv, yv):
    """Follow that point."""
    if (x1 - x2) > 0:
        x2 += xv  # v 爲追隨速度
    else:
        x2 -= xv
    if (y1 - y2) > 0:
        y2 += yv
    else:
        y2 -= yv
    return x2, y2


def keepaway(x1, y1, x2, y2, xv, yv):
    """Keep it away from other points."""
    if (x1 - x2) > 0:
        x2 -= xv  # v 爲逃逸速度
    else:
        x2 += xv
    if (y1 - y2) > 0:
        y2 -= yv
    else:
        y2 += yv
    return bx, by


def getd(x1, y1, x2, y2):
    """Get the distance."""
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return d


def line(x, k, b):
    """Get the trajectory of point A."""
    y = k * x + b
    return [x, y]


b = gettag(1, 50)  # b 點初始座標
c = gettag(1, 50)  # 固定障礙物

print("b:", b)

for i in range(20):
    a = line(i, 3, 5)
    c = line(i, 4, 10)
    for p in range(1):
        print("Point: ", p)
        # a = gettag(1, 50)
        # b = gettag(1, 50)
        # c = gettag(1, 50)  # 三體運動
        ax = a[0]
        ay = a[1]
        bx = b[0]
        by = b[1]
        cx = c[0]
        cy = c[1]
        ar = 1
        br = 2
        cr = 2
        safe_da = ar + br + 3  # 安全距離 = 半徑之和 + 調整距離
        safe_dc = cr + br + 3
        print("a: ", a, "c: ", c)
        q = 200
        for times in range(q):
            follow_d = getd(ax, ay, bx, by)
            keepaway_d = getd(cx, cy, bx, by)
            if follow_d < safe_da:
                if follow_d < (ar + br):
                    print("a loc error", "a:", ax, ay, "b:", bx, by)
                    break
                else:
                    # print("keep away from a", "a:", ax, ay, "b:", bx, by)
                    # delta_ax = abs(ax - bx)
                    # delta_ay = abs(ay - by)
                    # vx = getv(delta_ax, safe_da) * 10
                    # vy = getv(delta_ay, safe_da) * 10  # 加快減速
                    vx = vy = 5  # 調試
                    [bx, by] = keepaway(ax, ay, bx, by, vx, vy)
                    # print("keep away resutl", "bx:", bx,
                    #       "by:", by, "vx:", vx, "vy:", vy)
            if keepaway_d < (safe_dc):
                if keepaway_d < (cr + br):
                    print("c loc error", "c:", cx, cy, "b:", bx, by)
                    break
                else:
                    # print("keepaway from c", "c:", cx,
                    #       cy, "b:", bx, by, "a:", ax, ay)
                    # delta_cx = abs(cx - bx)
                    # delta_cy = abs(cy - by)
                    # vx = getv(delta_cx, safe_dc) * 10
                    # vy = getv(delta_cy, safe_dc) * 10  # 加快減速
                    vx = vy = 5  # 調試
                    [bx, by] = keepaway(cx, cy, bx, by, vx, vy)
                    # print("keep away resutl", "bx:", bx,
                    #       "by:", by, "vx:", vx, "vy:", vy)
            if safe_da < follow_d < (safe_da + 2):  # 跟隨成功的判定標準
                print("area: ", safe_da, "~", safe_da + 2)
                print("times: ", times)  # 輸出循環次數
                break
            else:
                # print("follow a")
                # delta_ax = abs(ax - bx)
                # delta_ay = abs(ay - by)
                if ax - bx == 0 or cx - bx == 0:
                    bx += 0.01  # 分母消零
                if abs((ay - by) / (ax - bx) - (cy - by) / (cx - bx)) <= 0.4:
                    # 對角線差速繞過s
                    vx = 0  # 調試
                    vy = 1  # 調試
                if abs(ay - by) < 1.5:
                    vx = 1
                    vy = 0  # 水平移動
                    # delta_ax = abs(ax - bx)
                    # delta_ay = abs(ay - by)
                    # vx = getv(delta_ax, safe_da) / 20  # 抑制加速
                    # vy = getv(delta_ay, safe_da) / 20
                else:
                    vx = vy = 1
                [bx, by] = follow(ax, ay, bx, by, vx, vy)
            # if times == 99:
            #     print("not enough times", times)
            #     times = 0
            #     q += 50
            #     if (q / 50) == 200:
            #         print("rebuild this code!")
            #         break
        print("bx: ", bx, "by: ", by)
        if times == q - 1:
            print("times out")
        print("------------------------------------")

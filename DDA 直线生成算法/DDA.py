import matplotlib.pyplot as plt
import numpy as np


def Round(x):
    """四舍五入取整函数，与python自带的取整函数round()不同

    Args:
        x (int): 一个点

    Returns:
        取整后的x  
    """
    if x >= 0:
        return int(x + 0.5)
    else:
        return int(x - 0.5)


def ShowPoint(x, y):
    """显示函数，用于显示点，并在对应位置标注(x,y)
    （因为调用次数多所以封装成一个函数

    Args:
        x (): 点
        y ([type]): [description]
    """
    plt.plot(x, y, 'r.')
    plt.text(x, y, '(' + str(x) + ',' + str(y) + ')', fontsize=14)
    return


def Input(x, y):
    x[0], y[0] = map(int, input("请输入起点: ").split())
    x[1], y[1] = map(int, input("请输入终点: ").split())
    return x, y


fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid(True)
x = [0, 0]
y = [0, 0]
x, y = Input(x, y)
if x[0] == x[1]:
    #斜率不存在时
    yi = min(y)
    for i in range(max(y) - min(y) + 1):
        ShowPoint(x[0], yi)
        yi = yi + 1
else:
    k = (y[1] - y[0]) / (x[1] - x[0])
    if abs(k) <= 1:
        # k的正负无所谓
        xi = min(x)
        yi = min(y) if k >= 0 else max(y)
        # 0 <= k <= 1时,直线递增,当x最小时,y最小
        # -1<= k<= 0时，直线递减,当x最小时, y最大
        for i in range(max(x) - min(x) + 1):
            ShowPoint(xi, Round(yi))
            xi = xi + 1  # x增1
            yi = yi + k  # y增k
    else:
        # abs(k)大于1的情况
        t = 1 / k
        yi = min(y)
        xi = min(x) if k > 0 else max(x)
        for i in range(max(y) - min(y) + 1):
            ShowPoint(Round(xi), yi)
            xi = xi + t
            yi = yi + 1
plt.show()

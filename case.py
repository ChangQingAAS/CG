from pylab import *
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

'''
1. 输入直线两端点 x0,y0 xn,yn
2. 计算初始值delta_x, delta_y,k=delta_y/delta_x,d=0, x=x0,y=y0
3. 绘制点x,y
4. d更新为d+k,若d>0.5,则x,y更新为x+1,y+1,d=d-1;否则x,y更新为x+1,y
5. 重复3,4直到直线画完
'''


def init(ax, width):
    # 设置长宽
    ax.axis([0, width, 0, width])

# 设置主刻度标签的位置,标签文本的格式
    majorLocator = MultipleLocator(1)
    minorLocator = MultipleLocator(0.5)
    ax.xaxis.set_major_locator(majorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    # ax.xaxis.set_minor_locator(minorLocator)
    # ax.yaxis.set_minor_locator(minorLocator)
    ax.grid(True)  # x坐标轴的网格使用主刻度


def add_pixel(x, y, ax, c):
    x = round(x)

    y = round(y)
    if c == 1:
        ax.add_patch(patches.Rectangle((x - 0.5, y - 0.5), 1, 1, color='b'))
        ax.plot(x, y, 'r.')
    else:
        ax.add_patch(patches.Rectangle((x - 0.5, y - 0.5), 1, 1))
        ax.plot(x, y, 'y.')


if __name__ == '__main__':

    # 将一行的字符串分割并转化为数字
    x0, y0, x1, y1, width = map(int, input("输入直线的两点和画布的边长: ").split(' '))
    if x0>x1:
        x0,x1=x1,x0
        y0,y1=y1,y0
    ax = subplot(121, aspect='equal',
            title='modified Bresenham')  # 改进的bresenham
    ax.plot([x0, x1], [y0, y1], '-k')
    bx = subplot(122, aspect='equal', title='DDA')  # DDA
    bx.plot([x0, x1], [y0, y1], '-k')
    # 图形初始化
    init(ax, width)
    init(bx, width)
    delta_x = x1 - x0
    delta_y = y1 - y0
    d = 0
    if delta_x == 0:
        k = 999999999
    else:
        k = delta_y / delta_x
    x = round(x0)
    y = round(y0)
    '''
    DDA算法
    '''
    if k > -1 and k < 1:
        # X 最大位移
        while True:
            if x > x1:
                break
            add_pixel(x, y, bx, 1)
            x = x+1
            y = y+k
    elif k >= 1:
        # Y 最大位移
        while True:
            if y > y1:
                break
            add_pixel(x, y, bx, 1)
            y = y+1
            x = x+1/k
    else:
        while True:
            if y < y1:
                break
            add_pixel(x, y, bx, 1)
            y = y-1
            x = x-1/k

    '''
    k的范围
    1.  (0,1)    x为最大位移，y正向增加
    2.  (1,+inf) y为最大位移，x正向增加
    3.  (0,-1)   x为最大位移，y负向增加
    4.  (-1,-inf)y为最大位移，y减小。x正向增加
    '''
    x = x0
    y = y0
    if k > 1:
        while True:
            if y > y1:
                break
            add_pixel(x, y, ax, 0)
            y = y + 1
            d = d + 1 / k
            if d > 0.5:
                x = x + 1
                d = d - 1
    elif k > 0:
        while True:
            if x > x1:
                break
            add_pixel(x, y, ax, 0)
            x = x + 1
            d = d + k
            if d > 0.5:
                y = y + 1
                d = d - 1
    elif k > -1:
        while True:
            if x > x1:
                break
            add_pixel(x, y, ax, 0)
            x = x + 1
            d = d - k
            if d > 0.5:
                y = y - 1
                d = d - 1
    else:
        while True:
            if y < y1:
                break
            add_pixel(x, y, ax, 0)
            y = y - 1
            d = d - 1 / k
            if d > 0.5:
                x = x + 1
                d = d - 1

    show()

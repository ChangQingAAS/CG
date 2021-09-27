import matplotlib.pyplot as plt
import numpy as np
import math


def draw_axis(cs):
    # 画出坐标轴
    plt.xlim(-cs, cs + 1)
    plt.ylim(-cs, cs + 1)
    ax = plt.gca()  # 获取整个框架
    ax.spines['right'].set_color('none')  # 可以隐藏两条边
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))

    x_ticks = np.arange(-cs, cs + 1, 1)
    y_ticks = np.arange(-cs, cs + 1, 1)
    plt.xticks(x_ticks, fontsize=8)
    plt.yticks(y_ticks, fontsize=8)
    plt.grid()  #生成网格


#使用极坐标画圆算法
def draw_circle(x0, y0, R):
    plt.scatter(x0, y0)
    list_x = []
    list_y = []
    angle = 360
    while (angle >= 0):
        #角度转弧度
        change = angle * math.pi / 180

        x = round(x0 + R * math.cos(change))
        y = round(y0 + R * math.sin(change))
        list_x.append(x)
        list_y.append(y)
        angle -= 2  # 步长设置为2

    for i in range(1, len(list_x)):
        plt.scatter(list_x[i], list_y[i])
        plt.plot([list_x[i - 1], list_x[i]], [list_y[i - 1], list_y[i]],
                 color='r')
        plt.pause(0.01)


if __name__ == '__main__':
    plt.figure(figsize=(6, 6))
    draw_axis(int(input('请输入坐标轴大小\n')))
    draw_circle(int(input('请输入圆心的x坐标\n')), int(input('请输入圆心的y坐标\n')),
                int(input('请输入圆的半径长度\n')))
    plt.show()

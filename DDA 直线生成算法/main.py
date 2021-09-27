import matplotlib.pyplot as plt
import numpy as np

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    steps = 0
    # 斜率判断
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    # 必有一个等于1，一个小于1
    delta_x = float(dx / steps)
    delta_y = float(dy / steps)
    # 四舍五入，保证x和y的增量小于等于1，让生成的直线尽量均匀
    x = x1 + 0.5
    y = y1 + 0.5
    for i in range(0, int(steps + 1)):
		# 绘制像素点
        plt.plot(int(x), int(y), color,'*')
        plt.text(x, y, '(' + str(x) + ',' + str(y) + ')', fontsize=14)
        x += delta_x
        y += delta_y
    
    plt.title("DDA")
    plt.xlabel("x - label")
    plt.ylabel("y - label")
    plt.gcf().set_facecolor(np.ones(3)* 240 / 255)   # 生成画布的大小
    plt.grid()  # 生成网格
    plt.show()


def main():
    x = 0
    y = 0
    xEnd = 10
    yEnd = 11
    color = "r."
    DDALine(x, y, xEnd, yEnd, color)


if __name__ == '__main__':
    main()

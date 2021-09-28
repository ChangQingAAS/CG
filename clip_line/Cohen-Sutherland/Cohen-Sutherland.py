import matplotlib.pyplot as plt
import numpy as np
import cv2

# 定义不同区域的编码
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# 窗口的边界值 (暂未初始化)
x_left_window = -1
x_right_window = -1
y_bottom_window = -1
y_top_window = -1

# 矩形的边界
ix, iy = -1, -1  # 左下角
px, py = -1, -1  # 右上角

# 线段的起点，终点
x_end, y_end = 0, 0
x_start, y_start = 0, 0

# 当前线段是否画完
is_line_drawn = 1

drawing = False  # 鼠标按下为真
notdone = True
img = []


def draw(event, x, y, flags, param):
    """响应鼠标事件, 用于画矩形，画线段的起点和终点，并进行线段的裁剪
    """

    # 定义全局变量
    global ix, iy, px, py
    global x_end, x_start, y_start, y_end
    global is_line_drawn, notdone, drawing
    global x_left_window, x_right_window, y_bottom_window, y_top_window

    # 鼠标左键画矩形
    if event == cv2.EVENT_LBUTTONDOWN and notdone == True:
        drawing = True
        ix, iy = x, y
    # 给矩形涂色
    elif event == cv2.EVENT_MOUSEMOVE and notdone == True:
        if drawing == True:
            # cv2.rectangle(img, (ix, iy), (px, py), (0, 0, 0), 0)  # 将刚刚拖拽的矩形涂黑
            # cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 0) 
            px, py = x, y
            
    # 结束画矩形，以开始画线
    elif event == cv2.EVENT_LBUTTONUP and notdone == True:
        drawing = False
        # 矩形颜色为绿色
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 0)
        px, py = x, y
        notdone = False

        # 获取窗口大小
        x_left_window, y_bottom_window = ix, iy
        x_right_window, y_top_window = x, y

    # 画线
    elif event == cv2.EVENT_MBUTTONDOWN:
        # 画线段端点颜色为蓝色
        cv2.circle(img, (x, y), 1, (255, 0, 0))

        if is_line_drawn % 2 == 1:
            x_start = x
            y_start = y
            is_line_drawn += 1
        else:
            x_end = x
            y_end = y
            is_line_drawn += 1
            print("需裁剪的线段： ", (x_start, y_start), (x_end, y_end))
            # 需裁减的线段颜色为黄色
            cv2.line(img, (x_start, y_start), (x_end, y_end), (0, 255, 255))
            # 窗口裁剪直线，并显示
            Cohen-Sutherland(x_start, y_start, x_end, y_end)


def encode(x, y):
    """给点(x,y) 进行编码
    """
    c = 0
    if x < x_left_window:
        c = c | LEFT
    if x > x_right_window:
        c = c | RIGHT
    if y < y_bottom_window:
        c = c | BOTTOM
    if y > y_top_window:
        c = c | TOP
    return c


def Cohen-Sutherland(x1, y1, x2, y2):
    """裁剪线段
    Args:
        (x1, y1) 线段起点
        (x2, y2) 线段终点
    """
    code1 = encode(x1, y1)
    code2 = encode(x2, y2)
    outcode = code1  # outcode是总在窗口外的那个端点
    x, y = 0, 0
    area = False  # 设置一个是否满足条件的区分标志
    while True:
        if (code2 | code1) == 0:
            area = True
            break
        if (code1 & code2) != 0:  # 简弃之
            break
        if code1 == 0:  # 开始求交点
            outcode = code2
        if (LEFT & outcode) != 0:  # 与窗口左边界相交
            x = x_left_window
            y = y1 + (y2 - y1) * (x_left_window - x1) / (x2 - x1)
        elif (RIGHT & outcode) != 0:
            x = x_right_window
            y = y1 + (y2 - y1) * (x_right_window - x1) / (x2 - x1)
        elif (BOTTOM & outcode) != 0:
            y = y_bottom_window
            x = x1 + (x2 - x1) * (y_bottom_window - y1) / (y2 - y1)
        elif (TOP & outcode) != 0:
            y = y_top_window
            x = x1 + (x2 - x1) * (y_top_window - y1) / (y2 - y1)
        x = int(x)  # 转换为整型
        y = int(y)
        if outcode == code1:
            x1 = x
            y1 = y
            code1 = encode(x, y)
        else:
            x2 = x
            y2 = y
            code2 = encode(x, y)
    if area == True:  # 若满足条件即可划线
        print("裁剪后的边是： ", (x1, y1), (x2, y2))
        # 裁剪后的边的颜色是黑色
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0))  
    return


def main():
    # 定义全局变量
    global img

    # 生成一张图片，相当于创建画布，颜色为白色
    img = np.full((512,512,3),255, np.uint8)

    # 直接显示窗口
    cv2.namedWindow('Cohen-Sutherland', cv2.WINDOW_NORMAL)

    # 处理事件，用于画矩形，画线段的起点和终点，并进行线段的裁剪
    cv2.setMouseCallback('Cohen-Sutherland', draw)

    while (1):
        # 显示图像
        cv2.imshow('Cohen-Sutherland', img)

        # 接收键盘按键，如果按‘Esc'键，则退出
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
        elif k == 27:
            break

    # 保存最后的图片
    cv2.imwrite('./clip_line/Cohen-Sutherland/out.jpg', img)

    # 清除窗口
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

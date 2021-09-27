'''
Cohen-Sutherland 裁剪算法

'''

import matplotlib.pyplot as plt
import numpy as np

LEFT=1        #0001 左
RIGHT=2       #0010 右
BOTTOM=4      #0100 下
TOP=8         #1000 上

XL=40
XR=100
YB=40
YT=100

def DDALine(image,x0, y0, x1, y1, color):
    # 保证x0<x1,否则调换起点和终点
    dx = x1 - x0
    dy = y1 - y0
    if dx != 0:
        k = dy / dx
    else:
        for i in range(y0, y0 + dy + 1):
            image[i][x0] = color
        else:
            for i in range(y1, y1 - dy + 1):
                image[i][x0] = color
        return
    if k>=0:
        if abs(k)<1:
            y = y0
            xmin = x0
            xmax = x1
            for i in range(xmin,xmax+1):
                image[int(y+0.5)][i] = color
                y = y+k
        else:
            x = x0
            if y0<y1:
                ymin = y0
                ymax = y1
            else:
                ymin = y1
                ymax = y0
            for i in range(ymin,ymax+1):
                image[i][int(x+0.5)] = color
                x = x + 1.0/k
    if k<0 :   #k<0
        if k>-1:
            y = y0
            xmin = x0
            xmax = x1
            for i in range(xmin,xmax+1):
                image[int(y+0.5)][i] = color
                y = y+k
        else:
            x = x1
            if y0<y1:
                ymin = y0
                ymax = y1
            else:
                ymin = y1
                ymax = y0
            for i in range(ymin,ymax+1):
                image[i][int(x+0.5)] = color
                x=x+1.0/k

def draw(image,graph,color):
    l = len(graph)
    for i in range(l):
        [x0, y0] = graph[i]
        [x1, y1] = graph[(i + 1 + l) % l]
        if x0 > x1:
            temp = x1
            x1 = x0
            x0 = temp
            temp = y1
            y1 = y0
            y0 = temp

        DDALine(image, x0, y0, x1, y1, color)


def encode(x,y):
    c=0
    if(x<XL):
        c=c|LEFT
    if(x>XR):
        c= c|RIGHT
    if(y<YB):
        c= c|BOTTOM
    if(y>YT):
        c=c|TOP
    return c


def CS_LineClip(polygon,image):
    image=image

    l = len(polygon)
    for i in range(l):
        [x1, y1] = polygon[i]
        [x2, y2] = polygon[(i + 1 + l) % l]
        print(x1)
        print(y1)
        print(x2)
        print(y2)
        print("\n")
        flag=0
        code1=encode(x1,y1)
        code2=encode(x2,y2)
        while(code1!=0 or code2!=0):        #同时为0,在内部，不用裁剪
            if(code1 & code2 !=0):
                flag=1
                break
            if(code1!=0):
                code=code1
            else:
                code=code2
            if(LEFT & code!=0):      #点在线左边
                 x=XL
                 if(x1==x2):
                     y=y1
                 else:
                     y=(int)(y1+(y2-y1)*(XL-x1)/(x2-x1))
            elif(RIGHT & code!=0):   #点在线右边
                x = XR
                if(x2==x1):
                    y=y1
                else:
                    y = (int)(y1 + (y2 - y1) * (XR - x1) / (x2 - x1))
            elif (BOTTOM & code != 0):     #点在线下边
                y = YB
                if(y2==y1):
                    x=x1
                else:
                    x = (int)(x1 + (x2 - x1) * (YB - y1) / (y2 - y1))
            elif (RIGHT & code != 0):     #点在线上边
                y = YT
                if(y2==y1):
                    x=x1
                else:
                    x = (int)(x1 + (x2 - x1) * (YT - y1) / (y2 - y1))
            if(code==code1):
                x1=x
                y1=y
                code1=encode(x,y)
            else:
                x2=x
                y2=y
                code2=encode(x,y)

        if(flag==1):
            pass
        else:
            if(x1 > x2):
                temp = x2
                x2 = x1
                x1 = temp
                temp = y2
                y2 = y1
                y1 = temp
            DDALine(image, x1, y1, x2, y2, False)


if __name__ == '__main__':
    image = np.ones([150, 150])
    plt.xlim(0, 150)
    plt.ylim(0, 150)

    window=[
        [40,40],
        [40,100],
        [100,100],
        [100,40]
    ]

    polygon = [
        [20, 20],
        [120, 20],
        [70, 100],
        [50, 80],
        [30, 120],
        [20, 50],
        [50, 50]
    ]
    draw(image,window,False)
    #draw(image,polygon,False)


    CS_LineClip(polygon,image)

    plt.imshow(image, plt.cm.gray)
    plt.show()

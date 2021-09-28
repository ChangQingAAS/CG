   
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 01:41:14 2021
@author: David Peña, Sebastián Matute & Alejandro Ponce
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# define region codes as constants
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# define diagonals points to define rectangle area
# of interest
xMax = 10.0
yMax = 8.0
xMin = 4.0
yMin = 4.0

# define function to compute region code to get
# a point(x,y)
def getPoint(x,y):
    code = INSIDE
    if x < xMin:
        code |= LEFT
    elif x > xMax:
        code |= RIGHT
    if y < yMin:
        code |= BOTTOM
    elif y > yMax:
        code |= TOP
    
    return code

# define function to display rectangle with its line
def display(x1, y1, x2, y2, accept):
    fig, ax = plt.subplots()
    ax.plot([x1,y1], [x2,y2], color="darkred")
    ax.add_patch(Rectangle((4,4), 10, 8, color="lightblue"))
    plt.xlabel('X AXIS')
    plt.ylabel('Y AXIS')
    if accept:
        subtitle = 'Line accepted from %.2f, %.2f to %.2f, %.2f' % (x1, y1, x2, y2)
        plt.title('Cohen-Sutherland Algorithm\n' + subtitle)
    else:
        subtitle = 'Line rejected - Completely outside the rectangle'
        plt.title('Cohen-Sutherland Algorithm\n' + subtitle)
    plt.show()
    
# now we implement the Cohen-Sutherland algorithm
# to clip a line from P1 to P2
def clipLine(x1, y1, x2, y2):
    # compute region codes for P1, P2
    codeA = getPoint(x1, y1)
    codeB = getPoint(x2, y2)
    isInside = False
    
    while True:
        # if both endpoints lie within rectangle
        if codeA == 0 and codeB == 0:
            isInside = True
            break
        
        # if both endpoints are outside rectangle
        elif (codeA & codeB) != 0:
            break
        
        # Some segment lies within the rectangle
        else:
            # line needs clipping because at least
            # one of the points is outside the rectangle
            x = 1.0
            y = 1.0
            # we find which of the points is outside
            if codeA != 0:
                codeOut = codeA
            else:
                codeOut = codeB
            
            # now we find the intersection point using
            # some formulas
            if codeOut & TOP:
                # point is above the clip rectangle
                x = x1 + (x2 - x1) * (yMax - y1) / (y2 - y1)
                y = yMax
            
            elif codeOut & BOTTOM:
                # point is below the clip rectangle
                x = x1 + (x2 - x1) * (yMin - y1) / (y2 - y1)
                y = yMin
                
            elif codeOut & RIGHT:
                # point is to the right of the clip rectangle
                y = y1 + (y2 - y1) * (xMax - x1) / (x2 - x1)
                x = xMax
                
            elif codeOut & LEFT:
                # point is to the left of the clip rectangle
                y = y1 + (y2 - y1) * (xMin - x1) / (x2 - x1)
                x = xMin
                
            # now we replace point outside rectangle by
            # intersection point
            if codeOut == codeA:
                x1 = x
                y1 = y
                codeA = getPoint(x1, y1)
            else:
                x2 = x
                y2 = y
                codeB = getPoint(x2, y2)
                
    if isInside:
        display(x1, y1, x2, y2, True)
    else:
        display(x1, y1, x2, y2, False)
            

# Test 1 - Line Segment - P1(5, 7), P2(5,7)
clipLine(5, 7, 5, 7)
# Test 2 - Line Segment - P1(7, 9), P2(11, 4)
clipLine(7, 9, 11, 4)
# Test 3 - Line Segment - P1(1, 5), P2(4, 1)
clipLine(1, 5, 4, 1)

print('Presented by: David Peña, Sebastián Matute & Alejandro Ponce')
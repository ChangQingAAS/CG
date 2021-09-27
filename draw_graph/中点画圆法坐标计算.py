import math

r = 8
x = [0] * r
y = [0] * r
p = [0] * r

p[0] = math.floor(5/4 - r)
y[0] = 8
x[0] = 0
if p[0] < 0:
    x[1] = x[0] + 1
    y[1] = y[0]
else:
    x[1] = x[0] + 1
    y[1] = y[0] + 1

for k in range(0, r):
    xx = x[k]
    yy = y[k]
    print("you should draw points :",(yy,xx),(xx,yy),(xx,-yy),(yy,-xx),(-yy,-xx),(-xx,-yy),(-xx,yy),(-yy,xx))

    p[k+1] = p[k] + 2 * (x[k] + 1) + (y[k+1] * y[k+1] - y[k] * y[k]) - (y[k+1] - y[k]) + 1

    if p[k + 1] < 0:
        x[k + 2] = x[k + 1] + 1
        y[k + 2] = y[k + 1]
    else:
        x[k + 2] = x[k + 1] + 1
        y[k + 2] = y[k + 1] - 1

    if (x[k + 1] >= y[k + 1]):
        print("x>= y")
        break

print(p)  
print(x)
print(y)

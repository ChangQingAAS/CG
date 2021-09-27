

**《计算机图形学》实验报告**





<center> <font color=black size=8>《线画图元生成算法实验》</font>  </center>















<center><font color=black size=5>姓名<u> _王红阳_</u></font></center>
<center><font color=black size=5>学号<u> _3019244233_</u></font></center>
<center><font color=black size=5>专业<u> _计算机科学与技术_</u></font></center>
<center><font color=black size=5>班级<u> _3班_</u></font></center>







<center><font color=black size=4>天津大学智能与计算学部</font></center>

<center><font color=black size=4>2021年 09月27 日 </font></center>

<div STYLE="page-break-after: always;"></div>

## 一、实验目的

- 

## 二、实验内容

- 内容：  
  - 实现 DDA 直线生成算法 
  - 实现 Bresenham 直线生成算法
-  要求： 
  - 自定义直线段起始点和终点坐标
  - 采用不同的彩色显示两种算法生成的直线结果
  - 为突出显示效果，采用网格表示像素，实现如下绘制效果。
  - ![image-20210927141553653](https://cdn.jsdelivr.net/gh/ChangQingAAS/for_picgo/img/20210927141553.png)
  
  - DDA算法
    DDA算法全称数值微分法（Digital Differential Analyzer）,是用数值方法解微分方程，即通过对x和y各增加一个小量，计算下一步的x、y值。实际上，应该令一个值增加1个单位，同时保证另一个值的增加量小于1个单位，这样才能绘制出更多的像素点，从而得到更准确的直线。因此，选择x增1还是y增1要看直线的斜率，
    不妨令直线的表达式为：$y = k x + b  $
  
    对于第i和第i+1个像素点，令x值分别为xi，xi+1，有
    $y_i = kx_i + b$ 
    $y_{i+1} = kx_{i+1} + b $ 
  
    以上两式作差，可以得到：
    $ \Delta y = y_{i+1}-y_i=k(x_{x+1}-x_i)=k\Delta x $
  
    由此可知，当x增加1个单位时，y增加k个单位；当y增加1个单位时，x增加 1/k 个单位。
    因为要保证令一个值增加1个单位的同时，另一个值的增加量小于1个单位，所以当直线斜率k<1时，令x增1，y增k；当k>1时，令y增1，x增加 1/k;(k = 1时，两种情况都可以，默认x增1）
  
    以下只考虑k<=1的情况。
    直线的起点坐标为（x0，y0），下一个像素点的坐标（x1，y1），因为k<=1,所以
    $ x_1 = x_0 + 1,y_1=y_0+k $
  
    因为像素点的坐标必须为整数，所以要对y1进行四舍五入处理，即Round（y1），Round（）函数为自定义的四舍五入函数，这样做的含义是选择最接近（x1，y1）的像素点。
    然后计算x2，y2，绘制（x2，Round（y2）），其中
    $x_2=x_1+1,y_2=y_1+k$ 
  
    依次计算x3，y3，x4，y4…直到终点xn，yn。像素点集合（xi，Round（yi））即为组成直线的像素点，其中0<=i<=n。
  
  - Bresenham 算法
  
    ![算法描述](https://cdn.jsdelivr.net/gh/ChangQingAAS/for_picgo/img/20210927174125.png)

## 三、实验结果

## 四、实验分析和总结

缺点：
在DDA算法中，x（或y）和k必须用浮点数表示，这不便于用硬件实现。

## 五、源代码
//代码要有详细的注释
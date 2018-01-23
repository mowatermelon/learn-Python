# -*- coding:utf-8 -*-  

# 基础案例 单平面坐标系曲线图
import matplotlib.pyplot as plt  
import numpy as np  
t = np.arange(0.0, 2.0, 0.01)#x轴上的点，0到2之间以0.01为间隔  
s = np.sin(2*np.pi*t)#y轴为正弦  
plt.plot(t, s)#画图  
  
plt.xlabel('time (s)')#x轴标签  
plt.ylabel('voltage (mV)')#y轴标签  
plt.title('About as simple as it gets, folks')#图的标签  
plt.grid(True)#产生网格  
plt.savefig("test.png")#保存图像  
plt.show()#显示图像  

# 基础案例 双平面坐标系曲线图
import matplotlib.pyplot as plt  
import numpy as np  
x1 = np.linspace(0.0, 5.0)#画图一  
x2 = np.linspace(0.0, 2.0)#画图二  
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)  
y2 = np.cos(2 * np.pi * x2)  
  
plt.subplot(2, 1, 1)#面板设置成2行1列，并取第一个（顺时针编号）  
plt.plot(x1, y1, 'yo-')#画图，染色  
plt.title('A tale of 2 subplots')  
plt.ylabel('Damped oscillation')  
  
plt.subplot(2, 1, 2)#面板设置成2行1列，并取第二个（顺时针编号）  
plt.plot(x2, y2, 'r.-')#画图，染色  
plt.xlabel('time (s)')  
plt.ylabel('Undamped')  
  
plt.show()  

# 圆饼案例
import matplotlib.pyplot as plt  
import numpy as np  
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'#设置标签  
sizes = [15, 30, 45, 10]#占比，和为100  
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']#颜色  
explode = (0, 0.1, 0, 0)  #展开第二个扇形，即Hogs，间距为0.1  
  
plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)#startangle控制饼状图的旋转方向  
plt.axis('equal')#保证饼状图是正圆，否则会有一点角度偏斜  
  
fig = plt.figure()  
ax = fig.gca()  
  
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90, radius=0.25, center=(0, 0), frame=True)  
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, radius=0.25, center=(1, 1), frame=True)  
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, radius=0.25, center=(0, 1), frame=True)  
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90,radius=0.25, center=(1, 0), frame=True)  
  
ax.set_xticks([0, 1])#设置位置  
ax.set_yticks([0, 1])  
ax.set_xticklabels(["Sunny", "Cloudy"])#设置标签  
ax.set_yticklabels(["Dry", "Rainy"])  
ax.set_xlim((-0.5, 1.5))  
ax.set_ylim((-0.5, 1.5))  
  
ax.set_aspect('equal')  
plt.show()  

# 双曲线案例

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
 
x = np.arange(-5.0, 5.0, 0.02)
y1 = np.sin(x)
 
plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)
 
plt.subplot(212)
#设置x轴范围
xlim(-2.5, 2.5)
#设置y轴范围
ylim(-1, 1)
plt.plot(x, y1)

plt.show()


#直方图案例
import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
  
mu = 100  # 正态分布的均值  
sigma = 15  # 标准差  
x = mu + sigma * np.random.randn(10000)#在均值周围产生符合正态分布的x值  
  
num_bins = 50  
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)  
#直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象  
y = mlab.normpdf(bins, mu, sigma)#画一条逼近的曲线  
plt.plot(bins, y, 'r--')  
plt.xlabel('Smarts')  
plt.ylabel('Probability')  
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')#中文标题 u'xxx'  
  
plt.subplots_adjust(left=0.15)#左边距  
plt.show()  


# 3D散点图
import matplotlib.pyplot as plt  
import numpy as np  
from mpl_toolkits.mplot3d import Axes3D  
  
x_list = [[3,3,2],[4,3,1],[1,2,3],[1,1,2],[2,1,2]]  
fig = plt.figure()  
ax = fig.gca(projection='3d')  
for x in x_list:  
    ax.scatter(x[0],x[1],x[2],c='r')  
plt.show()

#空间平面
from mpl_toolkits.mplot3d.axes3d import Axes3D  
from matplotlib import cm  
import matplotlib.pyplot as plt  
import numpy as np  
    
fig = plt.figure()  
ax = fig.add_subplot(1, 1, 1, projection='3d')  
X=np.arange(1,10,1)  
Y=np.arange(1,10,1)  
X, Y = np.meshgrid(X, Y)  
Z = 3*X+2*Y+30  
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap=cm.jet,linewidth=0, antialiased=True)  
ax.set_zlim3d(0,100)  
fig.colorbar(surf, shrink=0.5, aspect=5)  
plt.show()   

#空间曲面
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm  
from matplotlib.ticker import LinearLocator, FormatStrFormatter  
import matplotlib.pyplot as plt  
import numpy as np  
  
fig = plt.figure()  
ax = fig.gca(projection='3d')  
X = np.arange(-5, 5, 0.1)  
Y = np.arange(-5, 5, 0.1)  
X, Y = np.meshgrid(X, Y)  
R = np.sqrt(X**2 + Y**2)  
Z = np.sin(R)  
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)  
#画表面,x,y,z坐标， 横向步长，纵向步长，颜色，线宽，是否渐变  
ax.set_zlim(-1.01, 1.01)#坐标系的下边界和上边界  
  
ax.zaxis.set_major_locator(LinearLocator(10))#设置Z轴标度  
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))#Z轴精度  
fig.colorbar(surf, shrink=0.5, aspect=5)#shrink颜色条伸缩比例（0-1），aspect颜色条宽度（反比例，数值越大宽度越窄）  
  
plt.show()  
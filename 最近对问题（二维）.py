import random
import time

n=int(input('请输入点的个数：'))
abscissa=[]
ordinate=[]
for x in range(n):
    x=random.randint(-1000,1000)
    abscissa.append(x)
abscissa=sorted(abscissa)
for y in range(n):
    y = random.randint(-1000, 1000)
    ordinate.append(y)
coordinates=[]
for i in range(n):
    coordinate=[]
    coordinate.append(abscissa[i])
    coordinate.append(ordinate[i])
    coordinates.append(coordinate)
print(f"随机生成的点对为：{coordinates}")

def calculate_distance(x1,y1,x2,y2):
    distance=((x2-x1)**2+(y2-y1)**2)**0.5
    return distance

#蛮力法
start1=time.time()
mindistance=20000*2**0.5
for i in range(n):
    for j in range(i+1,n):
        distance=calculate_distance(coordinates[i][0],coordinates[i][1],coordinates[j][0],coordinates[j][1])
        if distance<mindistance:
            mindistance=distance
end1=time.time()
print(f"蛮力法结果：{mindistance}")
print(f"蛮力法用时：{end1-start1}s")

#分治法
start2=time.time()
def find_nearest_points(list,n,xmin,xmax):  #从1开始计数
    if n==2:
        dis=calculate_distance(coordinates[xmin-1][0],coordinates[xmin-1][1],coordinates[xmax-1][0],coordinates[xmax-1][1])
        return dis
    else:
        leftmin=find_nearest_points(list,n//2+1,xmin,(xmin+xmax-1)//2+1)
        rightmin=find_nearest_points(list,n-n//2,(xmin+xmax-1)//2+1,xmax)
        d=20000*2**0.5
        if leftmin<d:
            d=leftmin
        if rightmin<leftmin:
            d=rightmin
        print(d)
    return d

d=find_nearest_points(coordinates,100,1,100)

print(d)

leftpoints = []

for i in range(n):
    if -d <= list[i][0] <= d and -d <= list[i][1] <= d:
        leftpoints.append(list[i])

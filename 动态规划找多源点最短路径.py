#以求点1到点0最短距离为例
inf=float('-inf')
dist=[
[0,  1  ,inf, 4 ],
[inf,0  ,9  ,2  ],
[3  ,5  ,0  ,8  ],
[inf,inf,6  ,0  ]
]

way1=[0,0,0,0]

for x in range(2,4): #从上三角矩阵向右下走
    i=x
    j=x
    temlist = [] #将该点所有可能的数据存入，最后找最小
    for y in range(x-1):#从0向上找（所有可能），再向左找
        i = i - 1
        j = x
        num = 0
        if dist[i][j]>0:
            num += dist[i][j]
            num+=way1[i]
            temlist.append(num)
            way1[x]=min(temlist)
    if temlist==[]:
        way1[x]=-inf


print(way1)

for x in range(4):#将矩阵转置
    for y in range(x):
        dist[x][y],dist[y][x]=dist[y][x],dist[x][y]

way2=[0,0,0,0]
for x in range(1,4): #从下三角矩阵向左上走（相当于将矩阵转置向右下走）
    i=x
    j=x
    temlist = [] #将该点所有可能的数据存入，最后找最小
    for y in range(x):#从0向上找（所有可能），再向左找
        i = i - 1
        j = x
        num = 0
        if dist[i][j]>0:
            num += dist[i][j]
            num+=way2[i]
            temlist.append(num)
            way2[x]=min(temlist)
    if temlist==[]:
        way2[x]=-inf

print(way2)

way=[0,0,0,0]
for i in range(4):
    way[i]=way1[i]+way2[i]
print(way)
print(min(way[1:]))
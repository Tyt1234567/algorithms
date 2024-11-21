inf=float('-inf')
dist=[
[0,  4  ,2  , 3 ,inf,inf,inf,inf,inf,inf],
[inf,0  ,inf,inf,9  ,8  ,inf,inf,inf,inf],
[inf,inf,0  ,inf,6  ,7  ,8  ,inf,inf,inf],
[inf,inf,inf,0  ,inf,4  ,7  ,inf,inf,inf],
[inf,inf,inf,inf,0  ,inf,inf,5  ,6  ,inf],
[inf,inf,inf,inf,inf,0  ,inf,8  ,6  ,inf],
[inf,inf,inf,inf,inf,inf,0  ,6  ,5  ,inf],
[inf,inf,inf,inf,inf,inf,inf,0  ,inf,7  ],
[inf,inf,inf,inf,inf,inf,inf,inf,0  ,3  ],
[inf,inf,inf,inf,inf,inf,inf,inf,inf,0  ],
]

way=[0,0,0,0,0,0,0,0,0,0]
for x in range(1,10):
    i=x
    j=x
    temlist = [] #将该点所有可能的数据存入，最后找最小
    for y in range(x):#从0向上找（所有可能），再向左找
        i = i - 1
        j = x
        num = 0
        if dist[i][j]>0:
            num += dist[i][j]
            num+=way[i]
            temlist.append(num)
            way[x]=min(temlist)
    if temlist==[]:
        way[x]=inf

print(way)
if way[9]==-inf:
    print("path doesn't exist")
else:
    print(f"最短距离为{way[9]}")


way2=[]
j=9
while j>0:
    for k in range(j):
        if dist[k][j]>=0:
            num2=dist[k][j]
            if way[k]+num2==way[j]:
                way2.insert(0,num2)
                j=k
print(way2)

'''
for i in range(len(dis)):
    for j in range(i):
        if dis[0][i] > dis[0][j]+dis[j][i]:
            dis[0][i] = dis[0][j]+dis[j][i]
print(dis[0])
'''












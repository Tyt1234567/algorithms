inf=float('inf')
dist=[
[inf,3  ,6 , 7 ],
[5  ,inf,2  ,3  ],
[6  ,4  ,inf,2  ],
[3  ,7  ,5  ,inf]
]

n=4

lst=[]
for x in range(n):
    lst2={}
    lst.append(lst2)

#以零点出发和回到为例：

for i in range(n):#共有n个城市，本例中有4个
    if dist[i][0]!=inf:

        lst[0][f"{i}-0"]=dist[i][0]#分别代表从三个点回到0点的距离


for i in range(1,n):
    for j in range(1,n):
        if i!=j:
            lst[1][f"{i}-{j}-0"]=dist[i][j]+lst[0][f"{j}-0"]


for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if i!=j and j<k and i!=k:
                lst[2][f"{i}-{j}-{k}-0"]=min(dist[i][j]+lst[1][f"{j}-{k}-0"],dist[i][k]+lst[1][f"{k}-{j}-0"])
                lst[3][f"0-{i}-{j}-{k}-0"]=lst[2][f"{i}-{j}-{k}-0"]+dist[0][i]


for row in lst:
    print(row)





result=[]
for i in (lst[3].values()):
    result.append(i)
print(result)
print(min(result))


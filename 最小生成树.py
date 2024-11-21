#prim算法
inf=float('inf')

tree=[
[inf, 8, 8, 32, 32],
[8, inf, 16, 24, 24],
[8, 16, inf, 40, 40],
[32, 24, 40, inf, 16],
[32, 24, 40, 16, inf]
]

way_gone=[]
#从顶点0构造最小生成树
i=0
mindis=0
for x in range(len(tree)-1):
    way_gone.append(i)
    dist=min(tree[i])
    j=tree[i].index(dist)

    temdist=[]
    for way in way_gone:
        temdist.append(tree[j][way])

    #检查是否为以走点之间的最小路径，并连接最小路径
    if dist != min(temdist):
        i=tree[j].index(min(temdist))
        mindis+=tree[i][j]
        print(f"{i}-{j},distance={tree[i][j]}")
        for y in way_gone:
            tree[y][j] = inf
            tree[j][y]=inf
        i=j

    else:
        mindis += tree[i][j]
        print(f"{i}-{j},distance={tree[i][j]}")
        #防止原路返回
        for y in way_gone:
            tree[y][j] = inf
            tree[j][y]=inf

        i=j

print(mindis)





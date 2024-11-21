#输入矩阵，0表示相连，1表示不连

pic=[
[1,1,1,0,1,0,1,0],
[1,1,0,1,0,1,0,1],
[1,0,1,1,1,0,1,0],
[0,1,1,1,0,1,0,1],
[1,0,1,0,1,1,1,0],
[0,1,0,1,1,1,0,1],
[1,0,1,0,1,0,1,1],
[0,1,0,1,0,1,1,1]
]

color=[]
for x in range(len(pic)):
    color.append(x+1)


print_color=[]
for x in range(len(pic)):
    print_color.append('?')

i=0

for x in range(len(pic)):
    print(print_color)
    for y in range(x,len(pic)):#遍历每个点，如果没有着色且不相邻，则着色
        if pic[x][y]==1 and print_color[y]=='?':
            print_color[y] = color[i]
            for j in range(y):
                if print_color[j]==color[i] and pic[j][y]==0:#如果已经着色的有相邻点，则改为未着色
                    print_color[y] ='?'

    i+=1
    print(print_color)

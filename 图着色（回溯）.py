max=int(input('你能接受的最大颜色数是？'))

#1为相连，0为不连
tree=[
    [0,1,1,0,0],
    [1,0,1,1,1],
    [1,1,0,0,1],
    [0,1,0,0,1],
    [0,1,1,1,0]
]

color=[1,0,0,0,0]
def ok(k):
    for i in range(5):
        if tree[k][i]==1:
            if color[k]==color[i]:
                return False
    return True

k=1#从第二个点开始图
while k>=0:
    color[k]+=1
    while color[k]<max:
        if ok(k)==True:
            break

        else:
            color[k] += 1


    if color[k]==max and ok(k)==False:#回溯
        color[k]=0
        k-=1

        continue

    if k==4 and ok(k)==True:
        print(color)
        break

    elif k<4 and color[k]<=max:
        k+=1

    else:
        color[k]=0
        k-=1

    if color[0]>1:
        print('此问题无解')
        break





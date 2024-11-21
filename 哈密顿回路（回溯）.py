#1为通，0为不通
way=[
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,1,0,1,1],
    [1,0,1,0,1],
    [0,1,1,1,0]
]

route=[0,0,0,0,0]#从城市0出发
def ok(k):#检查第k步是否可以
    for i in range(k):#检查是否重复
        if route[k]==route[i]:
            return False
    if way[route[k-1]][route[k]]==0:#检查上一步到这一步是否通
        return False
    if k==len(way)-1:#最后一步与起点是否通
        if way[route[k]][0]==0:
            return False
    return True

k=1
while k>=1:
    route[k]+=1
    while route[k]<len(way)-1:
        if ok(k)==True:
            break
        else:
            route[k]+=1

    #如果到试探到最后一个城市仍不行则回溯
    if route[k]==len(way)-1 and ok(k)==False:
        route[k]=0

        k-=1
        continue

    if k==len(way)-1 and ok(len(way)-1)==True:#满足条件，结束
        break
    elif k<len(way)-1 and route[k]<=len(way):#填写下一个位置
        k+=1
    else:#回溯(若下一个数无法填，则这个数会加1，直到超过n，再回溯)
        route[k]=0
        k -= 1

print(route)



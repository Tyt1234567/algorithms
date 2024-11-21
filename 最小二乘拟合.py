points=[[-3, 7], [-1, 1], [2, 2], [5, -1]]
def multiply(a,b):
    result=[[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j]+=a[i][k]*b[k][j]
    return result

a=[]
for i in range(len(points)):
    point=[1,points[i][0]]
    a.append(point)


at=[]
row=[]
col=[]
b=[]
for i in range(len(points)):
    row.append(1)
    col.append(points[i][0])
    b.append([points[i][1]])
at.append(row)
at.append(col)


c=multiply(at,b)
d=multiply(at,a)  #d为2×2矩阵,且奇异


#接下来求d的逆
detd=d[0][0]*d[1][1]-d[0][1]*d[1][0]
dinverse=[[d[1][1]/detd,-d[0][1]/detd],[-d[1][0]/detd,d[0][0]/detd]]


e=multiply(dinverse,c)

intercept=e[0][0]
slope=e[1][0]

print(intercept)
print(slope)
def caldis(k,b,x,y):
    return(abs((k*x-y+b))/((k*k+1)**0.5))

totaldis=0
for i in range(len(points)):
    totaldis+=caldis(slope,intercept,points[i][0],points[i][1])
print(totaldis)



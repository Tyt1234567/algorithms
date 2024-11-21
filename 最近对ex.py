points=[[1, 5], [8, 4], [4, 4], [10, 7], [4, 1]]
sortedpoints=sorted(points,key=lambda point: point[0])


def calculate_distance(x1,y1,x2,y2):
    distance=((x2-x1)**2+(y2-y1)**2)**0.5
    return distance
def find_nearest_points(points,xstart,xend,n):#此时points为按横坐标排序好的二位列表，start,end均从1开始数,n为剩余点的个数
    if n==2:
        dis=calculate_distance(points[xstart-1][0],points[xstart-1][1],points[xend-1][0],points[xend-1][1])
        return dis
    else:
        leftmin=find_nearest_points(points,xstart,(xstart+xend-1)//2+1,n//2+1)
        rightmin = find_nearest_points(points,(xstart+xend-1)//2+1,xend,n-n//2)
        d=leftmin

        if rightmin<leftmin:
            d=rightmin


        uncertain=[]
        for i in range((xstart+xend-1)//2-5,(xstart+xend-1)//2+5):
            try:
                points[i]
            except IndexError:
                continue
            else:
                if d>=points[i][0]>=-d:
                    uncertain.append(points[i])

        for i in range(len(uncertain)):
            for j in range(i + 1, len(uncertain)):
                distance = calculate_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0],coordinates[j][1])
                if distance < d:
                    d=distance
    return d
d=find_nearest_points(sortedpoints,1,5,5)
import decimal
decimal.getcontext().rounding="ROUND_HALF_UP"
print(decimal.Decimal(d).quantize(decimal.Decimal("0.0000")))

import copy
inf = float('inf')
dis=[
    [inf,3  ,1  ,5  ,8  ],
    [3  ,inf,6  ,7  ,9  ],
    [1  ,6  ,inf,4  ,2  ],
    [5  ,7  ,4  ,inf,3  ],
    [8  ,9  ,2  ,3  ,inf]
]

#贪心求上界（0点出发）
city_left=[0,1,2,3,4]
i=0
max_dist=0
while len(city_left)>1:
    tem=[]
    for city in city_left[1:]:
        tem.append(dis[i][city])

    j=dis[i].index(min(tem))
    max_dist+=dis[i][j]
    i = j
    city_left.remove(j)

max_dist+=dis[j][0]

def cal_min_dist(routes): #routes为已经走过的路线，以二维列表存储，如[[0,2],[2,3]]
    dis_copy=copy.deepcopy(dis)
    min_dist = 0

    for route in routes:
        min_dist += dis_copy[route[0]][route[1]]*2
        dis_copy[route[0]][route[1]] = 0
        dis_copy[route[1]][route[0]] = 0

    for i in range(len(dis_copy)):
        min_dist += sum(sorted(dis_copy[i])[0:2])
    min_dist = min_dist / 2
    return min_dist









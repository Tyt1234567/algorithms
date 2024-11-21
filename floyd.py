inf=float('inf')
dist=[
[0,  1  ,inf, 4 ],
[inf,0  ,9  ,2  ],
[3  ,5  ,0  ,8  ],
[inf,inf,6  ,0  ]
]

for k in range(len(dist)):
    for i in range(len(dist)):
        for j in range(len(dist)):
            if dist[i][k]+dist[k][j]<dist[i][j]:
                dist[i][j]=dist[i][k]+dist[k][j]
print(dist)
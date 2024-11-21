inf=float('inf')
dist=[
[inf,3  ,3  ,2  ,6  ],
[3  ,inf,7  ,3  ,2  ],
[3  ,7  ,inf,2  ,5  ],
[2  ,3  ,2  ,inf,3  ],
[6  ,2,  5,  3  ,inf]
]

#1点到1点为例
#法一

rows=[0,1,2,3,4]
i=0

while len(rows)>1:
    tem=[]
    for row in rows[1:]:
        tem.append(dist[i][row])

    j = dist[i].index(min(tem))
    print(f"i-j:{i}-{j},distance={dist[i][j]}")
    i = j
    rows.remove(j)

print(f"i-j:{j}-{0},distance={dist[j][0]}")

a=0
b=a
b+=1
print(b)
print(a)
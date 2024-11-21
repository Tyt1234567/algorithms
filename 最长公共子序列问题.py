str1='abcbdb'
str2='acbbabdbb'

#初始化列表
table=[]
for x in range(len(str1)+1):
    row=[]
    for y in range(len(str2)+1):
        row.append(0)
    table.append(row)

i=0
j=0
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if str1[i]==str2[j]:
            table[i+1][j+1]=table[i][j]+1
        else:
            table[i + 1][j + 1] = max(table[i+1][j],table[i][j+1])
for row in table:
    print(row)

i=len(str1)
j=len(str2)
sameword=[]
while i>=1 and j>=1:
    if table[i][j] == table[i][j-1]:
        j-=1
    if table[i][j] != table[i][j-1]:
        sameword.append([i,j])
        i-=1

index=[x[1]-1 for x in sameword]
index=set(index)

word=[]
for x in index:
    word.append(str2[x])
print(word)
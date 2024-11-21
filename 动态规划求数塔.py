number=[
[6],
[3,9],
[7,1,2],
[2,5,0,9],
[8,4,13,1,6]]
line=5


for i in range(line - 1):
    for j in range(line - i-1):
        if number[line - 2 - i][j] + number[line - i-1][j] >= number[line - 2 - i][j] + number[line - i-1][j + 1]:
            number[line - 2 - i][j] = number[line - 2 - i][j] + number[line - i-1][j]

        else:
            number[line - 2 - i][j] = number[line - 2 - i][j] + number[line - i-1][j + 1]

print(number[0][0])
for line in number:
    print(line)
print("\n")




way=[0,0,0,0,0]
line=5
j=0
i=1
while i<=line-1:
    if number[i][j]>number[i][j+1]:
        way[i]=j
    else:
        way[i]=j+1
        j+=1
    i+=1

print(way)


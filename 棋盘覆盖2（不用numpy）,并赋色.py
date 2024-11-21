import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as lsc
import matplotlib.colors as mc
size = int(input(""))

matrix = []
for x in range(size):
    row = []
    for x in range(size):
        row.append(-1)
    matrix.append(row)


a = input().split()
location = [int(x) for x in a]
a = location[0]-1
b = location[1]-1
matrix[a] [b] = 0

n=1
def chessboard(matrix,size,a,b,startrow=0,startcol=0,number=0):
    def countnumber():
        global n
        m=n
        n+=1
        return m
    if size==1:
        return matrix
    else:
        if a >= startrow+size // 2 and b >= startcol+size // 2:  #右下
            number=countnumber()
            matrix[startrow+size // 2 - 1][startcol+size // 2 - 1] = number
            matrix[startrow+size // 2][startcol+size // 2 - 1] = number
            matrix[startrow+size // 2 - 1][startcol+size // 2] = number
            chessboard(matrix,size//2,size//2-1+startrow,size//2-1+startcol,startrow,startcol,number)
            chessboard(matrix,size//2,size//2-1+startrow,size//2+startcol,startrow,startcol+size//2,number)
            chessboard(matrix,size//2,size//2+startrow,size//2-1+startcol,startrow+size//2,startcol,number)
            chessboard(matrix,size//2,a,b,startrow+size//2,startcol+size//2,number)
        if a >= startrow+size // 2 and b < startcol+size // 2:  #左下
            number=countnumber()
            matrix[startrow+size // 2 - 1][startcol+size // 2 - 1] = number
            matrix[startrow+size // 2 - 1][startcol+size // 2] = number
            matrix[startrow+size // 2][startcol+size // 2] = number
            chessboard(matrix,size//2,size//2-1+startrow,size//2-1+startcol,startrow,startcol,number)
            chessboard(matrix,size//2,size//2-1+startrow,size//2+startcol,startrow,startcol+size//2,number)
            chessboard(matrix,size//2,a,b,startrow+size//2,startcol,number)
            chessboard(matrix,size//2,size//2+startrow,size//2+startcol,startrow+size//2,startcol+size//2,number)
        if a < startrow+size // 2 and b >= startcol+size // 2:  #右上
            number=countnumber()
            matrix[startrow+size // 2 - 1][startcol+size // 2 - 1] = number
            matrix[startrow+size // 2][startcol+size // 2 - 1] = number
            matrix[startrow+size // 2][startcol+size // 2] = number
            chessboard(matrix,size//2,size//2-1+startrow,size//2-1+startcol,startrow,startcol,number)
            chessboard(matrix,size//2,a,b,startrow,startcol+size//2,number)
            chessboard(matrix,size//2,size//2+startrow,size//2-1+startcol,startrow+size//2,startcol,number)
            chessboard(matrix,size//2,size//2+startrow,size//2+startcol,startrow+size//2,startcol+size//2,number)
        if a < startrow+size // 2 and b < startcol+size // 2:  #左上
            number=countnumber()
            matrix[startrow+size // 2][startcol+size // 2] = number
            matrix[startrow+size // 2][startcol+size // 2 - 1] = number
            matrix[startrow+size // 2 - 1][startcol+size // 2] = number
            chessboard(matrix,size//2,a,b,startrow,startcol,number)
            chessboard(matrix,size//2,size//2-1+startrow,size//2+startcol,startrow,startcol+size//2,number)
            chessboard(matrix,size//2,size//2+startrow,size//2-1+startcol,startrow+size//2,startcol,number)
            chessboard(matrix,size//2,size//2+startrow,size//2+startcol,startrow+size//2,startcol+size//2,number)
    return matrix
c=chessboard(matrix,size,a,b)
for row in c:
    for number in row:
        print(f'{number:<4}',end=' ')
    print('')

max_value=np.max(c)

cmap_colors=[(1,0,0)]
cmap_colors.extend([(1-i/max_value,1-i/max_value,1) for i in range(max_value+1)])
cmap=lsc.from_list('custom_cmap',cmap_colors,N=(max_value*2+1))
plt.imshow(c,cmap=cmap)
plt.colorbar()
plt.show()
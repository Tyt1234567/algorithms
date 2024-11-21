import numpy as np
import random
import matplotlib.pyplot as plt

n=int(input('请输入矩阵规模（必须为2的次方数）：'))
matrix=np.zeros((n,n))
a=random.randint(0,n-1)
b=random.randint(0,n-1)
matrix[a][b]=1

def chessboard(matrix,n,a,b,number=2): #n为方阵行数，a、b为1所在位置（从0开始数）
    if n ==2 :
        for col in range(2):
            for row in range(2):
                if matrix[row][col] == 0:
                    matrix[row][col] = number

    else:
        if a>=n//2 and b>=n//2:
            matrix[n//2-1][n//2-1] = number
            matrix[n//2][n//2-1] = number
            matrix[n//2-1][n//2] = number
            chessboard(matrix[n//2:n,n//2:n],n//2,a-n//2,b-n//2,number+1)
            chessboard(matrix[0:n//2,0:n//2],n//2,n//2-1,n//2-1,number+2)
            chessboard(matrix[0:n//2,n//2:n],n//2,n//2-1,0,number+3)
            chessboard(matrix[n//2:n,0:n//2],n//2,0,n//2-1,number+4)
        if a>=n//2 and b<n//2:
            matrix[n//2-1][n//2-1]=number
            matrix[n//2][n//2] = number
            matrix[n//2-1][n//2] = number
            chessboard(matrix[n//2:n,0:n//2], n//2, a-n//2,b,number+1)
            chessboard(matrix[0:n//2,0:n//2], n//2, n//2-1, n//2-1, number+2)
            chessboard(matrix[0:n//2,n//2:n], n//2, n//2-1,0, number+3)
            chessboard(matrix[n//2:n,n//2:n], n//2, 0,0, number+4)
        if a<n//2 and b>=n//2:
            matrix[n//2-1][n//2-1] = number
            matrix[n//2][n//2] = number
            matrix[n//2][n//2-1] = number
            chessboard(matrix[0:n//2,n//2:n], n//2, a, b-n//2,number+1)
            chessboard(matrix[0:n//2,0:n//2], n//2, n//2-1, n//2-1, number+2)
            chessboard(matrix[n//2:n,0:n//2], n//2, 0, n//2-1, number+3)
            chessboard(matrix[n//2:n,n//2:n], n//2, 0, 0, number+4)
        if a<n//2 and b<n//2:
            matrix[n//2][n//2-1]=number
            matrix[n//2][n//2] = number
            matrix[n//2-1][n//2] = number
            chessboard(matrix[0:n//2,0:n//2], n//2, a, b,number+1)
            chessboard(matrix[n//2:n,0:n//2], n//2, 0, n//2-1, number+2)
            chessboard(matrix[n//2:n,n//2:n], n//2, 0, 0, number+3)
            chessboard(matrix[0:n//2,n//2:n], n//2, n//2-1, 0, number+4)
    return matrix

a=chessboard(matrix,n,a,b)
print(a)
plt.imshow(a,cmap=plt.cm.Blues)
plt.show()


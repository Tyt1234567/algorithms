import numpy as np
import matplotlib.pyplot as plt
n=int(input('请输入矩阵规模：'))

matrix=np.zeros((n,n))
def rotation(matrix,n,number=1):
    if n==1:
        matrix[0][0] = number
        return matrix
    if n==2:
        matrix[0][0]=number
        matrix[1][0]=number+1
        matrix[1][1]=number+2
        matrix[0][1]=number+3
        return matrix
    else:
        for a in range(n-1):
            matrix[a][0]=number
            number += 1
        for b in range(n-1):
            matrix[-1][b]=number
            number+=1
        for c in range(n-1):
            matrix[n-c-1][-1]=number
            number+=1
        for d in range(n-1):
            matrix[0][n-d-1] = number
            number += 1
        rotation(matrix[1:n-1,1:n-1], n-2, number)
        return matrix


matrix=rotation(matrix,n)
print(matrix)
plt.imshow(matrix,cmap=plt.cm.Blues)
plt.show()
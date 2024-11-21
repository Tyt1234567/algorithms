n=20
def is_prime(a):#检查整数是否为素数
    if a <2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i ==0:
            return False
    return True

def check(k):#判断位置k是否满足条件

    for i in range(k):#检查是否重复
        if a[i]==a[k]:
            return False

    if k==n-1:    #检查最后一个数与第一个数是否为素数
        if is_prime(a[k]+a[0]) == False:
            return False

    if is_prime(a[k]+a[k-1])==True:#检查与前一个数和是否为素数
        return True
    else:
        return False

k=1
a=[1]
for i in range(n-1):
    a.append(0)

while k>=1:
    a[k]+=1
    while a[k]<=n-1:
        if check(k) == True: #位置k可以填a[k]
            break
        else:
            a[k]=a[k]+1 #试探下一个数

    if a[k]==n and check(k)==False: #如果填到上限仍不满足则回溯
        a[k] = 0
        k -= 1
        continue

    if k==n-1 and check(n-1)==True:#满足条件，结束
        break
    elif k<n-1 and a[k]<=n:#填写下一个位置
        k+=1
    else:#回溯(若下一个数无法填，回溯后前一个数会加1，如果前一个数加1后超过了上限，再回溯)
        a[k]=0
        k -= 1
print(a)

async def


















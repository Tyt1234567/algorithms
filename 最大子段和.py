import random
import time
randomlist = []
for x in range(1000):
    x = random.randint(-10, 10)
    randomlist.append(x)


#蛮力法
st1=time.time()
maxsum=0
for i in range(1000):
    for j in range(i,1000):
        sum=0
        for number in randomlist[i:j+1]:
            sum+=number
            if sum>maxsum:
                maxsum=sum
en1=time.time()
print(f"蛮力法结果:{maxsum}")
print(f"蛮力法用时:{en1-st1}s")

#分治法
st2=time.time()
def maxsum(list,start,end):
    sum=0
    if start==end:
        if list[start-1]>=0:
            sum=list[start-1]
        else:
            sum=0
        return sum
    else:
        middle=(start+end)//2
        leftsum=maxsum(list,start,middle)
        rightsum=maxsum(list,middle+1,end)
        leftmaxsum = 0
        a = 0
        for x in range(middle - start + 1):
            a += list[middle - 1 - x]
            if a >= leftmaxsum:
                leftmaxsum = a
        rightmaxsum = 0
        b = 0
        for y in range(end - middle):
            b += list[middle + y]
            if b >= rightmaxsum:
                rightmaxsum = b

        sum = leftmaxsum + rightmaxsum

        if sum < leftsum:
            sum = leftsum
        if sum < rightsum:
            sum = rightsum
    return sum

sum=maxsum(randomlist,1,1000)
print(f"分治法结果:{sum}")
en2=time.time()
print(f"分治法用时：{en2-st2}s")
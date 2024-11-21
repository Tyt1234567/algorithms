'''
牛牛坤有n只手镯，他们按顺序摆放在摊位上，每只都价值不菲，但他决定一次性卖掉其中的一部分，并且牛牛坤只想卖掉位置连续的手镯。牛牛坤是个善良的人，每卖出一只手镯就会捐出K元。请你帮牛牛坤计算他的最大收益。
输入格式:
输入的第一行为给出两个数字n(1 < n < 10)和k(1<< 10)，分别表示牛坤的手数量和牛牛每卖出一只手镯的捐款数额。
输入的第二行为以空格分隔的n个数字，第i个数字表示第识手镯的价格，每个数的范围都在1到10°之间。
输出格式:
输出一个数字，表示牛牛坤的最大收益。
输入样例:
5 10
5 8 12 9 13
输出样例:
4
'''

line1 = input().split()
line1=[int(x) for x in line1]
num = line1[0]
donation = line1[1]

line2 = input().split()
objects=[int(x)-donation for x in line2]

def maxsum(list,start,end):
    sum=0
    if start==end:
        if list[start-1]>=0:
            sum=list[start-1]
#        else:
 #           sum=0
 #       return sum
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
sum=maxsum(objects,1,num)
print(sum)
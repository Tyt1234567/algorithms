'''
小鸭同学和小华同学感觉大四生活大无聊了，他们闲的玩起了一个游戏。起初，每个人都会选定一个周定的正整数目在整局游戏中都不会更改，假定小鹏同学选定了数字a，
小华同学选定了数字6。另外他们有 个小球轮流被双方拿走，涉戏每轮他们各自行动一次，从小鹏同学开始。每次行动他们拿走小球的数量等干他们选定的数字和当前剩余
小球数量的最大公约数。当一方无法再按照规则拿取到所需的小球时(即剩余的小球数量少于需要拿取的数量) 他就输了。

你的任务是在给定上述游戏中的a，b和n后判断谁会赢得游戏。[最大公约数]两个非负整数a和b的最大公约数k是这样的最大非负整数: 和b均可被整除无余数。
例如gcd(6,9) = 3。规定gcd(0,x) = t。

输入格式:
3 5 9
输入只有一行，是三个用空格间隔的正整数a.b,n(1 < bn < 100)分别代表上述游戏中小鹏同学和小华同学选定的数字以及游戏开始时小球的数量。

输出格式:
xiao peng win
输出只有一行。如果小鹏同学赢得了比赛输出xiao peng win!，否则输出 xiao hua win!。
'''

#最大公因数
def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

line = input().split()
line = [int(x) for x in line]
peng = line[0]
hua = line[1]
total = line[2]
while True:
    if gcd(peng,total)<=total:
        total-=gcd(peng,total)
    else:
        print('xiao hua win')
        break
    if gcd(hua,total)<=total:
        total-=gcd(hua,total)
    else:
        print('xiao peng win')
        break
















#最小公倍数
def lcm(a,b):
    return abs(a*b) // gcd(a,b) if a and b else 0



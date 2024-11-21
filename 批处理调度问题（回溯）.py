machine1_time = [2, 5, 4]
machine2_time = [3, 2, 1]
arranged_work=[0,-1,-1]
besttime=float('inf')
time=5
def checkwork(i):
    global time
    global besttime
    global arranged_work
    for work in arranged_work[:i]:
        if work == arranged_work[i]:
            return False
    if time > besttime:
        return False
    if i == 2 and time <= besttime:
        besttime = time
        return True
    return True
k=1
while k >= 1:
    arranged_work[k] +=1
    while arranged_work[k] <= 1:
        if checkwork(k) == True:#可以安排作业i
            time = max(time-machine2_time[k-1]+machine1_time[k]+machine2_time[k],time+machine2_time[k])
            break
        else:#安排下个
            arranged_work[k] +=1
    if k == 2 and checkwork(k) == False:#不能安排作业i,则重新安排作业i-1(超过先前的最好时长)
        time = min(time + machine2_time[k - 1] - machine1_time[k] - machine2_time[k], time - machine2_time[k])
        arranged_work[k] == -1
        k-=1
        continue
    if k == 2 and checkwork(k) == True:
        time = max(time - machine2_time[k - 1] + machine1_time[k] + machine2_time[k], time + machine2_time[k])
        print(f'最短时间是{time},安排为{arranged_work}')
        break
        time = min(time + machine2_time[k - 1] - machine1_time[k] - machine2_time[k], time - machine2_time[k])
        arranged_work[k] = -1
        k -= 1
        continue

    if k < 2 and arranged_work[k] <= 2:#填写下一个位置
        k+=1

    if k==2 and arranged_work[k]>2:
        time = min(time + machine2_time[k - 1] - machine1_time[k] - machine2_time[k], time - machine2_time[k])
        arranged_work[k]=-1
        k-=1





































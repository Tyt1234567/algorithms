#先按结束时间排序
activities=[[1,4],[3,5],[0,6],[5,7],[3,8],[5,9],[6,10],[8,11],[8,12],[2,13],[12,14]]
activities=sorted(activities, key=lambda x:x[1])
starttime=[]
endtime=[]
for activity in activities:
    starttime.append(activity[0])
    endtime.append(activity[1])

starttime=[1,9,10,14,11]
endtime=[10,11,12,16,20]
activities=[[1,10],[9,11],[10,12],[14,16],[15,17]]
i=0
while i<len(activities)-1:

    print(f"安排活动{i+1}")
    time=activities[i][1]
    i+=1
    while activities[i][0]<time and i<=len(activities)-2 :
        i+=1


if time<=activities[i][0]:
    print(f"安排活动{i + 1}")








N,D =map(int,input().split())
num=list(map(int,input().split()))

num.sort()
list=[]

for i in range(N-1):
    if i==0:
        if num[1]-num[0]:
            list.append(1)
            
    elif i==(N-1):
        if num[i+1]-num[i]:
            list.append(N)
            break
    elif (num[i+2]-num[i+1]>=D) and (num[i+1]-num[i]>=D):
        list.append(i+1)

print(*list[0])
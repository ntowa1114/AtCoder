n=int(input())
t_pre=0
x_pre=0
y_pre=0
for i in range(n):
    t,x,y=map(int,input().split())
    dt=t-t_pre
    dx=abs(x-x_pre)
    dy=abs(y-y_pre)
    if dt>=dx+dy and (dt - dx-dy) %2==0:
        t_pre=t
        x_pre=x
        y_pre=y
    else:        
        print("No")
        exit()
print("Yes")

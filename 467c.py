n,m = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=n
for s in (0,1):
    x=s
    count=0
    for i in range(n):
        count += (a[i] !=x)
        if i<n-1:
            x^=b[i]
    ans=min(ans,count)    
print(ans)
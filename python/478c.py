n,k=map(int,input().split())
a=list(map(int,input().split()))


imax=n-k+1
ans="No"

for i in range(1,imax+1):
    ac=a.copy()
    b=ac[i-1:i-1+k]
    bs=sorted(b)
    ac[i-1:i-1+k]=bs
    if(ac==sorted(ac)):
        ans="Yes"

print(ans)
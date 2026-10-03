n=int(input())
x=list(map(int,input().split()))
ans="Yes"
for i in x:
    if i>=0:
        ans="No"
        break
print(ans)
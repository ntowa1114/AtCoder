N,V=map(int,input().split())
price=list(map(int,input().split()))
max=0
ans=[]*3
for i in range(1,N+1):
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            if (i+j+k<=V):
                if(max<price[i-1]+price[j-1]+price[k-1]):
                    max=price[i-1]+price[j-1]+price[k-1]

print(max)


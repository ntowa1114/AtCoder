N,M =map(int,input().split())

grape=[0]*N

count=0

for i in range(M):
    grape[i%N]+=1

for i in grape[0:]:
    print(i)


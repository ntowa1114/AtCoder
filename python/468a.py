n=int(input())
num_lst = list(map(int, input().split()))
count=0

for i in range(1,n-1):
    if(num_lst[i-1]<num_lst[i] and num_lst[i+1]<num_lst[i]):
        
        count=count+1

print(count)

n=int(input())

num_lst = list(map(int, input().split()))
count=0

while all(n%2==0 for n in num_lst):

    num_lst = [x/2 for x in num_lst]
    count+=1

print(count)
n=int(input())
num_list = []
for i in range(n):
    num_list.append(input())
num_list = list(set(num_list))
print(len(num_list))

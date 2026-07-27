n = int(input())
ans=0
for i in range(n):
    a_str, b_str, s = input().split()
    a = int(a_str)
    b = int(b_str)
    if s=="keep":
        ans=ans+(b-a)

print(ans)
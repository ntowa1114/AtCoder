n,m = map(int,input().split())
balls=[-1]*m
for i in range(n):
    c,s= map(int,input().split())
    

    if(balls[c-1]<s):
        balls[c-1]=s

print(" ".join(map(str, balls)))
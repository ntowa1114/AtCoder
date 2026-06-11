n=int(input())
card_lst = list(map(int, input().split()))
total=0
for i in range(n):
    selCard = max(card_lst)
    if(i%2==0):
        total = total + selCard
    else:
        total = total - selCard
    card_lst.remove(selCard)
print(abs(total))

"""
模範解答

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

print(sum(a[::2]) - sum(a[1::2]))
"""
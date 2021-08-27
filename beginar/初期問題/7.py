N = int(input())

a = list(map(int,input().split()))

ans=0
n=1

for n in N:
    if n%2!=0:
        ans+= max(a)
        a.remove(max(a))
    else:
        ans-= max(a)
        a.remove(max(a))
    n+=1

print(ans)

N = int(input())
a = list(map(int, input().split()))

ans = 0
while True:
    for i in range(N):
        if i%2 !=0:
            break
        a[i] = a[i]//2
    ans+=1 
    
print(ans)



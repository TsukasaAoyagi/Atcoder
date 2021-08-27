n, a, b = map(int, input().split())


ans = 0
for i in range(n+1):
    m = sum(list(map(int, str(i))))
    if a<=m<=b:
        ans+= i

print(ans)




n,a,x,y = map(int,input().split())

if n>a:
    ans = a*x + (n-a)*y
    print(ans)

else:
    ans = n*x
    print(ans)

    


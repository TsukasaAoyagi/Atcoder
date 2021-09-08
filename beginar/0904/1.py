s,t = input().split()

ans = []

ans.append(s)
ans.append(t)

ans=sorted(ans)

if ans[0]== t:
    print("Yes")

else:
    print("No")
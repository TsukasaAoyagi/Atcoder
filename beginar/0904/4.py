Q = int(input())

query = []

ans = []






for i in range(Q):
    q=list(map(int,input().split()))
    query.append(q)


for j in range(Q):
    r = query[j][0]

    if r == 1:
        ans.append(query[j][1])

    elif r == 2:
        print(ans[0])
        ans.pop(0)

    else:
        ans = sorted(ans)









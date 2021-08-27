n = int(input())
a = list(map(int,input().split()))
mp = {}
# 要素毎にカウントする
for i in range(n):
    if a[i] in mp.keys():
        mp[a[i]] += 1
    else:
        mp[a[i]] = 1


key = list(mp.keys())
print(mp)
# ソートしておくことで key[i] < key[j] とできる
key.sort()
print(key)
ans = 0
for i in range(len(key)):
    for j in range(i+1,len(key)):
        if i!=j:
            # 2要素の差の2乗に要素数の積をかけ
            ans += (key[j]-key[i])**2*(mp[key[i]]*mp[key[j]])
print(ans)


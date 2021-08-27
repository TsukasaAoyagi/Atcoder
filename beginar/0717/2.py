n = int(input())

s = input()

for i in range(n):
    if s[i]=="1":
        ans = i
        break

if ans%2==0:
    print("Takahashi")

else:
    print("Aoki")


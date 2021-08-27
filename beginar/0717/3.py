n,k = map(int,input().split())

c = list(map(int,input().split()))

color = {}

for i in range(n):
    color.setdefault(c[i], 0)

print(color)
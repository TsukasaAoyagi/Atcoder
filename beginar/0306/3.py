import itertools

n = int(input())

s = list(map(int, input().split()))

ans = 0

for pair in itertools.combinations(s, 2):
    a = (pair[0]-pair[1])**2
    ans+= a


print(ans)


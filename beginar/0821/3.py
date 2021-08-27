import itertools

s,k = input().split()

S=list(s)
K = int(k)

t = list(itertools.permutations(S))

t=list(set(t))

t = sorted(t)



T = t[K-1]



T ="".join(T)

print(T)






N=int(input())
A=list(map(int,input().split()))
v=[]

for i in range(N):
	v.append((A[i],i+1))

v.sort()
v.reverse()
print(v[1][1])


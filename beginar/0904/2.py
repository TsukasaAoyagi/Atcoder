a = input()
b = input()
c = input()

s = []

s.append(a)
s.append(b)
s.append(c)

ans = ["ABC","ARC","AGC","AHC"]

y = list(set(ans)-set(s))

print(y[0])




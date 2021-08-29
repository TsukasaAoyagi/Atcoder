n = input()
n = n.rstrip("0")

print(("No","Yes")[n==n[::-1]])




""" import random

n = int(input())



list =[0,1]


while n>0:
    Box = 0
    ans = []
    while Box<n:
        k = random.choice(list)
        if k == 0:  
            Box+=1
            ans.append("A")
        else:
            Box*=2
            ans.append("B")
    if Box==n and len(ans)<=120:
        break


    
ans = "".join(ans)
print(ans)
print(Box) """

n = int(input())

ans=""

while n!=0:
    if n%2==0:
        ans+="B"
        n=n//2
    else:
        n-=1
        ans+="A"

print(ans[::-1])






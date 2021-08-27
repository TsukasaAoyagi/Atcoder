X = int(input())

flag = True

if X[0]==X[1] and X[1]==X[2] and X[2]==X[3]:
    flag = False

for i in range(3):
    if int(X[i]) >= 0 and int(X[i]) <=8 and int(X[i]) == int(X[i-1]) -1:
        continue
    elif int(X[i]) == 9 and int(X[i+1]) == 0:
        continue
    else:
        break

else:
    flag = False

if flag:
    print("Strong")

else:
    print("Weak")


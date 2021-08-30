n = int(input())


def has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)


list = []

for i in range(n):
    list.append(input().split())

if has_duplicates2(list)==False:
    print("No")

else:
    print("Yes")





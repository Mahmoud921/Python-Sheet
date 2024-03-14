lst1 =list(map(int,input().split()))
lst2 = list(map(int,input().split()))
for i in lst1:
    for j in lst2:
        if i == j:
            print(i,end=" ")
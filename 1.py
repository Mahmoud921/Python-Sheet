# Generate Arry from length and filled with integer numbers increased by on from start
def fun(length,start):
    arr=[]
    for i in range(length):
        start +=i
        arr.append(start)
    return arr
length,start = map(int,input().split())
print(fun(length,start))

    
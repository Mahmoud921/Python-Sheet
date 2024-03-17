Keys = ['ten','twenty','thirty']
Values = [10, 20, 30]
dec = {}
for val in range(len(Keys)):
    if Keys[val] in dec:
        dec[Keys[val]].append(Values[val])
    else:
        dec[Keys[val]] = Values[val]
print(dec)
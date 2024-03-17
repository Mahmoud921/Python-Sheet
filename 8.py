list_froute = list(input().split())
dic={}
for st in list_froute:
    dic_key=st[0]
    if dic_key in dic:
        dic[dic_key].append(st)
    else:
        dic[dic_key] = [st]
print(dic)
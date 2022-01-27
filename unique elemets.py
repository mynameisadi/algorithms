arr=[int(x) for x in input().split()]
d=dict()
for x in arr:
    d[x]=d.get(x,0)+1
flag=True
for i in d:
    if d[i]>=2:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")

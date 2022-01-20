arr=[int(x) for x in input().split()]
i=0
while(i<len(arr)):
    sum1=0
    flag=False
    j=i-1
    while(j>=0):
        if arr[i]<arr[j]:
            flag=True
            sum1=j
        j=j-1    
    if (flag):
        arr[i],arr[sum1]=arr[sum1],arr[i]
        i=sum1+1
    else:
        i=i+1
print(arr)



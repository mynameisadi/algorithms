arr=[int(x) for x in input().split()]
for i in range(len(arr)):
    sum1=i
    for j in range(i+1,len(arr)):  
        if arr[j]<arr[sum1]: 
            sum1=j
    arr[i],arr[sum1]=arr[sum1],arr[i] 
print(arr)
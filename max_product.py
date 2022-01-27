arr=[int(x) for x in input().split()] 
sum1=0 
a=0 
b=0 
for i in range(len(arr)):  
    for j in range(i+1,len(arr)):
        if arr[i]*arr[j]>sum1:
            sum1=arr[i]*arr[j]
            a=i
            b=j
print(sum1)
print(a,b)
            


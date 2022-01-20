import math
arr=[int(x) for x in input().split()]
buckets=round(math.sqrt(len(arr)))

sum1=arr[0]
for x in arr:
    if x>sum1:
        sum1=x
arr1=[]
for i in range(len(arr)):
    arr1.append([])

for j in arr:
    which_bucket=math.ceil((j*buckets)/sum1)
    arr1[which_bucket-1].append(j)

for k in range(buckets):
    arr2=arr1[k]
    i=0
    while(i<len(arr2)):
        sum1=0
        flag=False
        j=i-1
        while(j>=0):
            if arr2[i]<arr2[j]:
                flag=True
                sum1=j
            j=j-1    
        if (flag):
            arr2[i],arr2[sum1]=arr2[sum1],arr2[i]
            i=sum1+1
        else:
            i=i+1
    arr1[k]=arr2
sum2=[]
for z in arr1:
    sum2=sum2+z
print(sum2)
    
    


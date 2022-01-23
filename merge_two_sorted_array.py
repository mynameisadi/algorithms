#give input in sorted order
arr1=[int(x) for x in input().split()]
arr2=[int(y) for y in input().split()]
arr3=[]
i=0
j=0
while(i<len(arr1) and j<len(arr2)):
    if arr1[i]<arr2[j]:
        arr3.append(arr1[i])
        i=i+1
    if arr1[i]>arr2[j]:
        arr3.append(arr2[j])
        j=j+1
    else:
        arr3.append(arr1[i])
        arr3.append(arr2[j])
        i=i+1
        j=j+1

while(i<=len(arr1)-1):
    arr3.append(arr1[i])
    i=i+1
while(j<=len(arr2)-1):
    arr3.append(arr2[j])
    j=j+1
print(arr3)



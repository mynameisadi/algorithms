#given start,mid and high index
'''arr=[int(x) for x in input().split()]
l=0
h=len(arr)-1
mid=int(input())
i=0
j=mid+1
arr1=[]
while(i<=mid and j<=h):
    if arr[i]<arr[j]:
        arr1.append(arr[i])
        i=i+1
    if arr[j]<arr[i]:
        arr1.append(arr[j])
        j=j+1
    else:
        arr1.append(arr[i])
        arr1.append(arr[j])
        i=i+1
        j=j+1
while(i<=mid):
    arr1.append(arr[i])
    i=i+1
while(j<=h):
    arr1.append(arr[j])
    j=j+1
print(arr1)'''

# without extra space
arr=[int(x) for x in input().split()]
l=0
h=len(arr)-1
mid=int(input())
i=0
j=mid+1
arr1=[]
while(i<=mid and j<=h):
    if arr[i]<arr[j]:
        i=i+1
    if arr[j]<arr[i]:
        arr[j],arr[i]=arr[i],arr[j]
    else:
        i=i+1
print(arr)

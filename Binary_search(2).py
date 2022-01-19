arr=[int(x) for x in input().split()]
k=int(input())  
front=0
end=len(arr)-1  
mid=0
flag=False
while(front<=end):
    mid=(front+end)//2
    if arr[mid]==k:
        flag=True
        print(mid)  
        break
    elif arr[mid]>k:
        end=mid-1
    elif arr[mid]<k:
        front=mid+1
if flag==False:
    print("Number not found")

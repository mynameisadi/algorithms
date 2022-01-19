arr=[int(x) for x in input().split()]
k=int(input())
flag=True
for i in range(0,len(arr)):
    if arr[i]==k:
        flag=False
        print(i)
if flag==True:
    print("number not found")
    

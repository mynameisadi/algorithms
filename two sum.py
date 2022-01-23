arr=[int(a) for a in input().split()]
k=int(input())
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            continue
        elif arr[i]+arr[j]==k:
            print(i,j)



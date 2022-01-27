arr1=[int(x) for x in input().split()]
arr2=[int(y) for y in input().split()]

if len(arr1)!=len(arr2):
    print("False") 
else:
    arr1.sort()
    arr2.sort()
    if arr1==arr2:
        print("True")
    else:
        print("False")
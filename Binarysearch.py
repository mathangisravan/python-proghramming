def Binarysearch(list1,key):
    low = 0
    high = len(list1) -1
    value = 0
    while low<= high and value == 0:
        mid = (low + high) //2
        if key == list1[mid]:
            value =1
        elif( key > list1[mid]):
         low = mid +1
        elif( key < list1[mid]):
            high = mid-1
    if value == 1 :
        print("Key found at "+str(mid))
    else :
        print("Not found")

    
key = int(input("Enter the key value"))
num = int(input("Enter the values in a list"))
list1 = [int(input()) for i in range(num)]
list1.sort()
print(list1)
Binarysearch(list1,key)

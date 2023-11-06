def Bubblesort(list1):
    i =len(list1)
    temp = 0
    while i>=0:
        for j in range(0,i,1):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
        i-=1
    print(list1)
list1 = [3,2,1,4,5,9,5,3]
Bubblesort(list1)


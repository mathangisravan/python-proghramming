
list1 = [1,2,1,2,3,4,5,3,4,2]
count =0
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j]:
            count+=1
print(count)
        

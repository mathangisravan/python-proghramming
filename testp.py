tup = (1,2,4,3,5,6,7,1,2,4,5,6,1,1,1,2,4,4,5)
count = 0
for i in range(len(tup)):
    for j in range(i,len(tup)):
        if tup[i] == tup[j]:
            count +=1
    print(count)


def integer(N):
    count = 0
    num = ''
    for  i in range(1,N+1):
        num = str(i)
        if len(num) %2 != 0:
            count+=1    
    print(count)       
N = int(input("Enter the value of N"))
integer(N)

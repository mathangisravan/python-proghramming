def fact(n):
    
    if n ==0:
        print('Zero factorial if "1"')
    elif n<0:
        print('Not valid')
    else:
        a =1
        for i in range(1,n+1):
          a = a*i
        print(a)
    
fact(8)

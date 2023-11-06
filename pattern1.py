def righttriangle(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end =" ")
        for k in range(i+1):
            print('*',end=" ")
        print()
    print()

def lefttriangle(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,n):
            print("*", end = " ")
        print()

righttriangle(4)
lefttriangle(5)
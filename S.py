def prints(n):

    for i in range(n):
        print("*", end =" ")
    print()
    for i  in range(n-1):
        print("*")
    for i in range(n):
         print("*", end =" ")
    print()
    for i in range(n-1):
        for j in range(n-1):
            print(" ", end = " ")
        for j in range(1):
            print("*", end = "")
        print()
    for i in range(n):
        print("*", end =" ")
prints(2)
    

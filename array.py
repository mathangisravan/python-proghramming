def feb(n):
    a= 0
    b = 1
    if n <0:
        print("Enter a valid number")
    elif n ==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
feb(-1)
# hello
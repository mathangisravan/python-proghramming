def recursicemethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursicemethod(n-1)
        print(n)

recursicemethod(4)
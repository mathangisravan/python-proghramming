class patterns :
    def __init__(self,n):
        self.n =n
    
    def pattern1(self,m):
        
        for i in range(1,m+1):
         for j in range(1,i+1):
             print("*", end = " ")
         print()

    def pattern2(self,m):
        
        for i in range(1,m+1):
         for j in range(1,i+1):
             print("*", end = " ")
         print()

    def dimondpattern(self,m):
        for i in range(1,m+1):
            for j in range(i,m+1):
                print(" ", end = " ")
            for j in range(i):
                print("*", end = " ")
            for j in range(i):
                print("*", end = " ")
            print()
        for i in range(1,m+1):
            for j in range(i):
                print(" ", end = " ")
            for j in range(i,m+1):
                print("*", end = " ")
            for j in range(i,m+1):
                print("*", end = " ")
            print()
        

m = int(input("Enter the value "))
value = patterns(m)
value.dimondpattern(m)

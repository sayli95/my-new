def cal(p1,p2):

    def add():
        return p1+p2

    def sub():
        return p1-p2
    
    def mul():
        return p1*p2
    
    def div():
        return p1/p2

    print(f"Addition = {add()}")
    print(f"Subtraction = {sub()}")
    print(f"Multiplication = {mul()}")
    print(f"Division = {div()}")
    

cal(25,5)



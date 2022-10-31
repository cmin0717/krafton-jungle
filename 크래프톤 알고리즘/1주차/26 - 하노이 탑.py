def test():
    n = int(input())
    def hanoi(n,x,y,z):
        if n == 1:
            print(x,z)
            return
        else:
            hanoi(n-1,x,z,y)
            print(x,z)
            hanoi(n-1,y,x,z)
    if n > 20 :
        print((2**n)-1)
    else:
        print((2**n)-1)
        hanoi(n,1,2,3)
    return

test()

while True:
    def isEvenOdd(n):
        if(n ^ 1 ==n+1):
            # then 0 num is even
            return True;
        else:
            # then 1 num is odd
            return False;

    number = int(input("Enter you number"))
    if isEvenOdd(number):
        print(number,"is even")

    else:
        print(number, "is odd")
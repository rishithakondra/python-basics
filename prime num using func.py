def check_prime():
    num=int(input("enter:"))
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                print(num,"is not a prime:")
                break
        else:
            print(num,"is a prime")
    else:
        print(num,"is not prime")
check_prime()
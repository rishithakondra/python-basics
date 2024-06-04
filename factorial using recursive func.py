def recursive_factorial(n):
    if n<=1 :
        return n
    else:
        return n*recursive_factorial(n-1)
num=6
if num < 0:
    print("Invalid input ! please enter a postive number.")
elif num==0:
    print("factorial of number 0 is 1" )
else:
    print("factorial of number",num, "=",recursive_factorial(num))
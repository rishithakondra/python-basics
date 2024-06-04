import operator
d={}
n=int(input("no of elements:"))
for i in range(n):
    k=input("enter key for first dict:")
    v=input("enter its value:")
    d[k]=v
key=input()
if key in d:
    print("yes")
else:
    print("no")
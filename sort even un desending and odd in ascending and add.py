l=list(map(int,input().split()))
b=[]
l.sort
for i in l:
    if i%2==0:
        b.insert(0,i)
    else:
        b.append(i)
print(b)

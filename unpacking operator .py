def my_sum(*integers):
    result=0
    for x in integers:
        result+=x
    return result
print(my_sum(1,2,3))
## is used for kwargs
#used for keyword arguments
def concatenate(**kwargs):
    result=""
    for arg in kwargs.values():
        result+=arg
    return result
print(concatenate(a="real",b="python",c="is",d="great",e="!"))


#kwargs are keyword arguments
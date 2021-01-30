def outer(a,b):
    def inner(n,n2):
        res=a+b
        return( res)
    return inner(2,4)
print(outer(3,3))
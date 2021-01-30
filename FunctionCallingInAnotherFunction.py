def square(x):
    y = x * x
    return( y)

def sum_of_squares(x, y, z,k):
    a = square(x)
    b = square(y)
    c = square(z)
    d = square(k)

    return(a * b * c*d)

a = 1
b = 2
c = 3
d=4
result = sum_of_squares(a, b, c,d)
print(result)
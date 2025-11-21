def factorial(n):
    rst=1
    for i in range(1, n+1):
        rst*=i
    return rst
print(factorial(5))  
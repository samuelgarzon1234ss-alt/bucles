import math
def numP(n):
    if n<2:
        return False
    limite=int(math.sqrt(n))  
    for i in range(2, limite+1):
        if n%i==0:
            return False
    return True
print(numP(7))   
print(numP(12))  
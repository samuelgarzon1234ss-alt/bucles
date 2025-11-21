def mcd(a, b):
    while b!=0:
        a, b=b, a%b
    return abs(a)
def mcm(a, b):
    return abs(a * b)//mcd(a, b)
print(mcd(48, 18))   
print(mcm(48, 18))   
print(mcd(12, 20))  
print(mcm(12, 20))   
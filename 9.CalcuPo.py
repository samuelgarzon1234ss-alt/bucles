def potencia(base, exp):
    resul=1
    for i in range(exp):
        resul*=base
    return resul
print(potencia(2, 5))  
print(potencia(3, 3))  
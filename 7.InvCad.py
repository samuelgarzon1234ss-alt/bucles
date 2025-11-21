def invertir(cadena):
    if len(cadena)<=1:
        return cadena
    return cadena[-1]+invertir(cadena[:-1])
print(invertir("hola"))  
print(invertir("python"))  
print(invertir("Estiven"))
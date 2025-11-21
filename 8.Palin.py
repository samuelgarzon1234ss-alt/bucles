def invertir(cadena):
    if len(cadena)<=1:
        return cadena
    return cadena[-1]+invertir(cadena[:-1])
def plm(cadena):
    return cadena==invertir(cadena)
print(plm("Niconiconi"))   
print(plm("Malcon")) 
print(plm("MR Money"))
def sumar(a, b):
    return a+b
def restar(a, b):
    return a-b
def multiplicar(a, b):
    return a*b
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a/b
def pedirNumero(prompt):
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Entrada inválida. Ingresa un número (p.ej. 3.5 o 2).")
def pedirOpcion():
    while True:
        try:
            opcion = int(input("Elige una opción (1-4) o 0 para salir: "))
            if opcion in (0, 1, 2, 3, 4):
                return opcion
            print("Opción no válida. Elige 0, 1, 2, 3 o 4.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero (p.ej. 1).")
def calculadora():
    print("Calculadora")
    print("0. Salir")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    while True:
        opcion = pedirOpcion()
        if opcion == 0:
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        a = pedirNumero("Ingresa el primer número: ")
        b = pedirNumero("Ingresa el segundo número: ")
        try:
            if opcion == 1:
                resultado = sumar(a, b)
                op_name = "Suma"
            elif opcion == 2:
                resultado = restar(a, b)
                op_name = "Resta"
            elif opcion == 3:
                resultado = multiplicar(a, b)
                op_name = "Multiplicación"
            elif opcion == 4:
                resultado = dividir(a, b)
                op_name = "División"
            print(f"{op_name} => {resultado}")
        except ZeroDivisionError as e:
            print("Error:", e)
        print() 
if __name__ == "__main__":
    calculadora()
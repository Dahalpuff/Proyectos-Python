# Calculadora básica en Python

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir entre cero"

def multiplicar(a, b):
    return a * b

def potencia(a,b):
    return a ** b

# Bucle infinito hasta que el usuario decida salir
while True:
    print("\n**** Calculadora básica ****")
    print("Listado de operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Potencia")
    print("6. Salir")
    
    opcion = input("Elige una operación (1-5) o pulsa 6 para salir: ")

    if opcion == "6":
        print("¡Hasta luego!")
        break  # Rompe el ciclo y termina el programa

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", sumar(num1, num2))
    elif opcion == "2":
        print("Resultado:", restar(num1, num2))
    elif opcion == "3":
        print("Resultado:", dividir(num1, num2))
    elif opcion == "4":
        print("Resultado:", multiplicar(num1, num2))
    elif opcion =="5":
        print("Resultado: ", potencia(num1, num2))
    else:
        print("Opción inválida")

def obtener_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Debe ingresar números válidos.")
            continue

def multiplicar(num1, num2):
    return num1 * num2

def main():
    while True:
        try:
            num1, num2 = obtener_numeros()
            resultado = multiplicar(num1, num2)
            print("El resultado de la multiplicación es:", resultado)
            break
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
            continue

if __name__ == "__main__":
    main()

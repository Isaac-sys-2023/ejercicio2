from multiplicacion import obtener_numeros


def sumar(num1, num2):
    return num1 + num2


def main():
    num1, num2 = obtener_numeros()
    resultado = sumar(num1, num2)
    print("El resultado de la suma es:", resultado)


if __name__ == "__main__":
    main()

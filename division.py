def dividir():
    dividendo = input("Inserte el numero que se va a dividir... ")
    dividendo = float(dividendo)
    divisor = input("Inserte el numero que va a dividir al anterior numero... ")
    divisor = float(divisor)
    resultado = dividendo / divisor
    print(f"El resultado es {resultado}")

dividir()
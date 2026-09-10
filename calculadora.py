from suma import suma
from resta import resta


def calculadora(a, b, operacion):
    if operacion == "suma":
        return suma(a, b)
    elif operacion == "resta":
        return resta(a, b)
    else:
        return "Operacion no valida"


def entrada_usuario():
    try:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        operacion = input("Ingrese la operacion (suma/resta): ").lower()
        resultado = calculadora(a, b, operacion)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Debe ingresar un numero valido.")


if __name__ == "__main__":
    entrada_usuario()
def calculadora(a, b, operacion):
    if operacion == "suma":
        return suma(a, b)
    elif operacion == "resta":
        return resta(a, b)
    else:
        return "Operacion no valida"
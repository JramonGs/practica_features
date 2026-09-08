def calculadora(a, b, operacion):
    if operacion == "suma":
        return suma(a, b)
    elif operacion == "resta":
        return resta(a, b)
    else:
        return "Operacion no valida"
    
    print(calculadora(5, 3, "suma"))  # Output: 8
    print(calculadora(5, 3, "resta"))  # Output: 2
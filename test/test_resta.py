# Importamos la funcion que queremos testear.
import resta

# Funcion para probar.
def test_resta():
    
    # Probamos que la resta de 5 y 3 sea igual a 2 (este es el resultado esperado).
    assert resta.resta(5, 3) == 2

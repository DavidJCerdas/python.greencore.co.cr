name = input("Cual es su nombre?: ")

ERROR1 = "tiene espacios"
ERROR2 = "solo la primera letra debe ir in mayuscula"

ERRORS = [0,ERROR1, ERROR2]

def alrevez(palabra):
    word = list(palabra)
    word.reverse()
    return "".join(word)

def control_errores(palabra):
    if " " in name:
        return 1
    if name != name.capitalize():
        return 2
    return 0

imprimo = control_errores(name)
if imprimo == 0:
    print("Hola, {0}".format(alrevez(name).capitalize()))
if imprimo > 0:
    print("No tiene el formato correcto, {0}".format(ERRORS[imprimo]))

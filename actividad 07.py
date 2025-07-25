def ingresar_numeros():
    n = int(input("¿Cuántos números desea ingresar?: "))
    numeros = []
    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(num)
    return numeros

def analizarLalista(numeros):
    suma = sum(numeros)
    promedios = suma / len(numeros) if numeros else 0
    positivos = sum(1 for x in numeros if x > 0)
    negativos = sum(1 for x in numeros if x < 0)
    cerosencalificaciones = sum(1 for x in numeros if x == 0)
    multiplosdel3 = sum(1 for x in numeros if x % 3 == 0)
    return suma, promedios, positivos, negativos, cerosencalificaciones, multiplosdel3
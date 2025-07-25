def ingresar_numeros():
    n = int(input("¿Cuántos números desea ingresar?: "))
    numeros = []
    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(num)
    return numeros

def analizarLalista(numeros):
    suma = sum(numeros)
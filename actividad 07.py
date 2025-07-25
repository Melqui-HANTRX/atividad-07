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

def areaDerectangulo(base, altura):
    return base * altura

def perimetroDelrectangulo(base, altura):
    return 2 * (base + altura)

def esunNumeroprimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def promedioDelascalificaciones():
    n = int(input("¿Cuántas calificaciones desea ingresar?: "))
    calificaciones = []
    for i in range(n):
        cal = float(input(f"Ingrese la calificación {i + 1}: "))
        calificaciones.append(cal)

    promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0
    mayoresa85 = sum(1 for x in calificaciones if x >= 85)
    perdercurso = sum(1 for x in calificaciones if x < 60)
    return promedio, mayoresa85, perdercurso

def mayorOmenorYrepetidos():
    n = int(input("¿Cuántos números desea ingresar?: "))
    numeros = []
    for i in range(n):
        num = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(num)

    mayor = max(numeros)
    menor = min(numeros)

    frecuenciarepetidas = {}
    for num in numeros:
        if num in frecuenciarepetidas:
            frecuenciarepetidas[num] += 1
        else:
            frecuenciarepetidas[num] = 1

    repetidos = {}
    for rep2 in frecuenciarepetidas:
        if frecuenciarepetidas[rep2] > 1:
            repetidos[rep2] = frecuenciarepetidas[rep2]

    return mayor, menor, repetidos

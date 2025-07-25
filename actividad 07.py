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

def calculadora():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Operaciones disponibles: +  -  *  /")
    operaciones = input("Seleccione la operación: ")

    if operaciones == "+":
        return num1 + num2
    elif operaciones == "-":
        return num1 - num2
    elif operaciones == "*":
        return num1 * num2
    elif operaciones == "/":
        if num2 == 0:
            return "Error: división por cero"
        return num1 / num2
    else:
        return "Operación inválida"

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Analizar lista de números reales")
        print("2. Calcular área y perímetro de un rectángulo")
        print("3. Verificar si un número es primo")
        print("4. Promedio de calificaciones y análisis")
        print("5. Análisis de lista de números enteros")
        print("6. Calculadora básica")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")
        match opcion:
            case "1":
                numeros = ingresar_numeros()
                suma, prom, pos, neg, ceros, mult3 = analizarLalista(numeros)
                print(f"Suma total: {suma}")
                print(f"Promedio: {prom:.2f}")
                print(f"Positivos: {pos}, Negativos: {neg}, Ceros: {ceros}")
                print(f"Multiplos de 3: {mult3}")
            case "2":
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                area = areaDerectangulo(base, altura)
                perimetro = perimetroDelrectangulo(base, altura)
                print(f"Área: {area}")
                print(f"Perímetro: {perimetro}")
            case "3":
                num = int(input("Ingrese un número entero: "))
                if esunNumeroprimo(num):
                    print("El número es primo.")
                else:
                    print("El número NO es primo.")
            case "4":
                promedio, buenos, riesgo = promedioDelascalificaciones()
                print(f"Promedio: {promedio:.2f}")
                print(f"Mayor o igual a ≥85: {buenos}, Es menor o igual que (<60): {riesgo}")
            case "5":
                mayor, menor, repes = mayorOmenorYrepetidos()
                print(f"Mayor: {mayor}, Menor: {menor}")
                print("Repetidos y frecuencia:")
                for numerosrep in repes:
                    print(f"{numerosrep} → {repes[numerosrep]} veces")
                return mayor, menor, repes
            case "6":
                resultado = calculadora()
                print(f"Resultado: {resultado}")
            case "7":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
menu()


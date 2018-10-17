# Autor: Carlos Alberto Reyes Ortiz
# Matricula: A01376349

# Este programa muestra el menu que te da a elejir entre calcular una divisón (1),
# encontrar el numero mayor entre de los números que quieras (2) y Salir del programa (3).




def dividr(): # Esta función calcula una división entre dos números dados por el usuario,
              # dando como resultado el cociente y el residuo.

    print("Calculando divisiones")
    divisor = int(input("Divisor: "))
    dividendo = int(input("Dividendo: "))
    acumulador = dividendo
    cociente = 0
    while acumulador <= divisor:
        acumulador += dividendo
        cociente += 1

    if acumulador != (divisor + dividendo):
        residuo = divisor - (dividendo * cociente)
    else: residuo = 0


    print(divisor, "/", dividendo, "=", cociente,  "sobra", residuo  )




def encontrarMayor():# Esta función encuentra el número mayor entre la cantidad de números que el usuario lo desee.

    numeroMayor = -1
    print("Teclea una serie de números para encontrar el mayor. ")
    numero = int(input("Teclea un número [-1 para salir]: "))

    while numero != -1:
        if numero > numeroMayor:
            numeroMayor = numero
        numero = int(input("Teclea un número [-1 para salir]: "))

    if numeroMayor == -1 :
        print("No hay valor mayor")
    else: print("El mayor es: " ,numeroMayor)




def leerOpcionesMenu(): # Esta función imprime las opciones que el usuario tiene para hacer.
    print()
    print()
    print("Misión 07. Ciclos while")
    print("Autor: Carlos Alberto Reyes Ortiz")
    print("Matricula: A01376349")
    print("1. Calcula divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    print()
    return opcion




def main(): # Función principal: Es un menu que junta todas las funciones para hacer el programa más amigable
            # para el usuario.

    opcion = leerOpcionesMenu()
    while opcion != 3:
        if opcion == 1:
            dividr()
            opcion = leerOpcionesMenu()
        elif opcion == 2:
            encontrarMayor()
            opcion = leerOpcionesMenu()
        elif opcion < 1 or opcion > 3:
            print("ERROR, teclea 1, 2 o 3")
            opcion = leerOpcionesMenu()

    print()
    print("Gracias por usar este programa, regresa pronto.")



main()



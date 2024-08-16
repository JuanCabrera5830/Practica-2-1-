def main():
    N = 8  # Definimos el tama�o del arreglo
    numeros = []  # Creamos una lista vac�a para almacenar los n�meros

    # Solicitamos al usuario que ingrese 8 n�meros
    print("Ingrese 8 numeros enteros:")
    for i in range(N):
        numero = int(input(f"Numero {i + 1}: "))
        numeros.append(numero)

    # Imprimimos los valores almacenados en el arreglo
    print("\nLos valores ingresados en el arreglo son:")
    for i, numero in enumerate(numeros):
        print(f"numeros[{i}] = {numero}")

    # Calculamos la suma de los n�meros
    suma = sum(numeros)
    print(f"\nLa suma de los numeros es: {suma}")

if __name__ == "__main__":
    main()
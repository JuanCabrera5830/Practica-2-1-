def main():
    N = 8  # Definimos el tamaño del arreglo
    numeros = []  # Creamos una lista vacía para almacenar los números

    # Solicitamos al usuario que ingrese 8 números
    print("Ingrese 8 numeros enteros:")
    for i in range(N):
        numero = int(input(f"Numero {i + 1}: "))
        numeros.append(numero)

    # Imprimimos los valores almacenados en el arreglo
    print("\nLos valores ingresados en el arreglo son:")
    for i, numero in enumerate(numeros):
        print(f"numeros[{i}] = {numero}")

    # Calculamos la suma de los números
    suma = sum(numeros)
    print(f"\nLa suma de los numeros es: {suma}")

if __name__ == "__main__":
    main()
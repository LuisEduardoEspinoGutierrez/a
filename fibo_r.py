def fibonacci_rec(numero):
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci_rec(numero-1) + fibonacci_rec(numero-2)

numero = int(input("Ingresa el número de índice para calcular el número de Fibonacci: "))
resultado = fibonacci_rec(numero)
print("El número de Fibonacci en el índice",numero,"es: ",resultado)
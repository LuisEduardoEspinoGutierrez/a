
def factorial(numero):
    if(numero > 1):
        return numero*factorial(numero-1)
    else:
        return numero
    
numero = int(input("Ingrese el numero: "))   
resultado = factorial(numero)
print("el factorial de ",numero," es: ",resultado)

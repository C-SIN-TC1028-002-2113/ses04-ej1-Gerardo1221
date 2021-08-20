def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    if edad<=0 or edad>120: 
        print("Respuesta incorrecta")
    elif edad<18:
        print("No cumples requisitos")
    elif edad>=18:
        Id = input("¿Tienes identificación oficial? (s/n): ") 
        if Id== "s":
            print("Trámite de licencia concedido")
        elif Id== "n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    
if __name__ == '__main__':
    main()

def main():
    #escribe tu código abajo de esta línea
    #escribe tu código abajo de esta línea
    #Modifica el programa para que haga lo siguiente: Realiza un programa que reciba las coordenadas de dos puntos y que calcule la pendiente de la recta que une esos dos puntos. La fórmula para calcular la pendiente es:
    # m = (y2 - y1) / (x2 - x1)
    #Autora:Renata Arriaga
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    pendiente = float((y2 - y1) / (x2 - x1))
    print("Pendiente:",pendiente)




if __name__ == '__main__':
    main()

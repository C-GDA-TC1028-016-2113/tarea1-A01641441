def main():
    #escribe tu código abajo de esta línea
    #escribe tu código abajo de esta línea
    #Modifica el programa para que haga lo siguiente: A inicio de año, las personas están preocupadas por su peso por lo que acuden a nutriólogos, gimnasios y cualquier otra cosa que les ayude en el proceso. Realiza un programa que ayude a las personas a indicar cuántos kilos debe bajar por mes, dados el peso inicial, el peso final y el número de meses que una persona estará en un programa integral para bajar de peso.
    #Autora:Renaa Arriaga
    pesoinicial = float(input("Dame el peso inicial: "))
    pesofinal = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    pesoperder = float(pesoinicial- pesofinal)
    bajarmes = float(pesoperder/meses)
    print ("Lo que debes bajar por mes es:",bajarmes)




if __name__ == '__main__':
    main()

def main():
    #escribe tu código abajo de esta línea
    #Modifica el programa para que realice lo siguiente: En una universidad cada estudiante cursa 4 materias en el semestre. Desarrolla un programa que reciba la calificación de cada materia (tipo float), calcula el promedio de las 4 materias y lo despliega.
    #Autora:Renata Arriaga
    calificacion1 = float(input("Calificación de la materia: "))
    calificacion2 = float(input("Calificación de la materia: "))
    calificacion3 = float(input("Calificación de la materia: "))
    calificacion4 = float(input("Calificación de la materia: "))
    promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4)/4
    print("El promedio es:",promedio)


if __name__ == '__main__':
    main()

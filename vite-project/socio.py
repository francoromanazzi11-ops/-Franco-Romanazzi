class examen:
    def __init__(self, nombre, edad, examen_final_aprobado):
        self.nombre = nombre
        self.edad = edad
        self.examen_final_aprobado = examen_final_aprobado

    def mostrar_estado(self):
        if self.examen_final_aprobado:
            print(f"{self.nombre} usted ha pasado de año.")
        else:
            print(f"{self.nombre} usted debe recursar.")

alumno1 = examen("Emiliano", 13, True)
alumno2 = examen("Cruz", 14, False)

alumno1.mostrar_estado()
alumno2.mostrar_estado()
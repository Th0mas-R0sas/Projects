aprobados = 0
reprobados = 0
promedio = 0
for estudiante in range(1,31):
    nota_estudiante = float(input(f"Ingrese nota estudiante {estudiante}:"))
    suma_nota += nota_estudiante #suma_nota = suma_nota + nota_estudiante
    if nota_estudiante >= 4.0:
        aprobados += 1
        print(f"Estudiante {estudiante} esta aprobado con una nota {nota_estudiante}")
    else:
        reprobados += 1
        print(f"Estudiante {estudiante} esta reprobado con una nota {nota_estudiante}")
print("Informacion del curso")
print(f"Cantidad de estudiantes aprobados: {aprobados}")
print(f"Cantidad de estudiantes reprobados: {reprobados}")
print(f"El promedio del curso es: {suma_nota / estudiante}")
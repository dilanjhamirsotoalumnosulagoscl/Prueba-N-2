notas = []
nota = input("Ingrese una nota (o 0 para finalizar): ")
while nota == "0":
    print("Debe ingresar al menos una nota")
    nota = input("Ingrese una nota (o 0 para finalizar): ")
notas.append(int(nota))

while True:
    nota = input("Ingrese una nota (o 0 para finalizar): ")
    if nota == "0":
        break
    notas.append(int(nota))

print("Cantidad de notas:", len(notas))
print("Promedio de notas:", sum(notas) / len(notas))

notas_bajo_4 = 0
notas_mayor_igual_4 = 0
i = 0
while i < len(notas):
    if notas[i] < 4:
        notas_bajo_4 = notas_bajo_4 + 1
    else:
        notas_mayor_igual_4 = notas_mayor_igual_4 + 1
    i += 1

print("Cantidad de notas bajo 4.0:", notas_bajo_4)
print("Cantidad de notas igual o mayor que 4.0:", notas_mayor_igual_4)
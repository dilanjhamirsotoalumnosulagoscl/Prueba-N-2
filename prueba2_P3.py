capitales_paises = {}

for i in range(5):
    capital = input("Ingrese la capital " + str(i+1) + ": ")
    pais = input("Ingrese el país correspondiente a " + capital + ": ")
    capitales_paises[capital] = pais

nombre_turista = input("Ingrese el nombre del turista: ")
capital_procedencia = input("Ingrese la capital de procedencia del turista: ")

if capital_procedencia in capitales_paises:
    pais_procedencia = capitales_paises[capital_procedencia]
    print("El turista con el nombre " + nombre_turista + " viene de la capital " + capital_procedencia + " y su país es " + pais_procedencia)
else:
    print("La capital de procedencia no se encuentra en la lista")
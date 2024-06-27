tasa_cambio = 950

precios_clp = []

for x in range(10):
    precio_clp = input("Ingrese el precio del producto " + str(x+1) + " en CLP: ")
    precios_clp.append(int(precio_clp))

precios_usd = []
for precio_clp in precios_clp:
    precio_usd = precio_clp / tasa_cambio
    precios_usd.append(str(precio_usd))

print("Precios en USD:")
for x in range(10):
    print("Producto " + str(x+1) + ": USD " + precios_usd[x])
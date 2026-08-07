nombres_rios = ["Douro", "Ebro", "Tajo", "Duero", "Guadiana", "Turia", "Cádiz", "Llobregat", "Aránjuez", "Zúrich"]

# Usando sort()
print("Después de usar sort():")
nombres_rios.sort()
for rio in nombres_rios:
    print(rio)

# Usando sorted()
print("\nDespués de usar sorted():")
sorted_nombres = sorted(nombres_rios)
for rio in sorted_nombres:
    print(rio)

# Usando reverse()
print("\nDespués de usar reverse():")
sorted_nombres.reverse()
for rio in sorted_nombres:
    print(rio)

# Usando len()
print(f"\nEl número total de ríos en la lista es: {len(nombres_rios)}")
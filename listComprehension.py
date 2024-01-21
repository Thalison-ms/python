numeros = list(range(1, 100))

for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)

# Usando list comprehension, usa-se chaves []
pares_div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
print(pares_div4)

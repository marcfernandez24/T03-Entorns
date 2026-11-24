# Creem la llista.
llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Demanem un enter positiu.
numero = int(input("Introdueix un número enter positiu: "))
while numero <= 0:
    numero = int(input("Introdueix un número enter positiu: "))

# Sumem el número a cada element de la mateixa llista.
for i in range(len(llista)):
    llista[i] = llista[i] + numero

print(llista)

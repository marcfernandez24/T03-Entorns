import random

# Generem 1000 enters entre -5000 i 5000.
llista = []
for i in range(1000):
    llista.append(random.randint(-5000, 5000))

print("Versió amb bucle:")
# Calculem el més gran, el més petit i la suma amb un bucle.
mes_gran = llista[0]
mes_petit = llista[0]
suma = 0
for numero in llista:
    if numero > mes_gran:
        mes_gran = numero
    if numero < mes_petit:
        mes_petit = numero
    suma = suma + numero

# Dividim la suma pel nombre d'elements per obtenir la mitjana.
mitjana = suma / len(llista)

print("El nombre més gran és:", mes_gran)
print("El nombre més petit és:", mes_petit)
print("La mitjana és:", mitjana)

print("Versió amb funcions:")
# Fem els càlculs amb les funcions bàsiques de Python.
mes_gran = max(llista)
mes_petit = min(llista)
mitjana = sum(llista) / len(llista)

print("El nombre més gran és:", mes_gran)
print("El nombre més petit és:", mes_petit)
print("La mitjana és:", mitjana)

llista = []

# Demanem una longitud entre 2 i 10.
entrada = input("Longitud de la llista (entre 2 i 10): ")
while entrada not in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
    entrada = input("Longitud de la llista (entre 2 i 10): ")
quantitat = int(entrada)

# Comprovem cada número abans d'afegir-lo a la llista.
for i in range(quantitat):
    correcte = False
    while not correcte:
        entrada = input("Introdueix un número: ")

        # Comprovem els dígits sense el signe ni el punt decimal.
        digits = entrada
        if digits != "" and digits[0] in "+-":
            digits = digits[1:]
        digits = digits.replace(".", "", 1)
        correcte = digits != ""
        for caracter in digits:
            if caracter not in "0123456789":
                correcte = False

        if not correcte:
            print("Escriu un número; per als decimals, fes servir el punt.")

    numero = float(entrada)
    llista.append(numero)

print("La llista és:", llista)

# Calculem la suma i la multiplicació amb un for.
suma = 0
multiplicacio = 1
for numero in llista:
    suma = suma + numero
    multiplicacio = multiplicacio * numero

print("La suma és:", suma)
print("La multiplicació és:", multiplicacio)

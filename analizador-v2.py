# Práctica de diseño de un analizador Léxico, que cumpla con los siguientes requisitos:

# Utiliza el lenguaje de su elección, NO FRAMEWORK
# Desarrolle un programa que simule un analizador Léxico.
# Debe permitir una entrada de texto (char), símbolos y números (intenger) a la vez
# El programa debe devolver:
#   Una cadena sin espacios, uniendo solo texto y números, eliminando todo tipo de simbolos.
#   También debe devolver la cantidad de de cada tipo de carácter que existe en la cadena.
#   Debe devolver la cadena ordenada de los caracteres ingresados (mayúsculas, minúsculas, números, símbolos eliminados)


contador = {}  # para salvar el numero de tipo de caracteres
letras = []  # para salvar los numeros y letras sin espacios ni simbolos
numeros = []

entrada = ""
caracteres = []


def contar(k):
    if contador.get(k) == None:
        contador[k] = 1
    else:
        c = contador.get(k)
        contador[k] = c + 1


print("------------< DEMO DE ANALIZADOR LEXICO >-----------------")
entrada = input()

# volcar la cadena a una lista para su analisis
caracteres[:] = entrada

# recorrer la lista, quitar espacios, simbolos y contar
for x in caracteres:
    if not x.isspace():
        # validar valor alfabetico
        if x.isalpha():
            letras.append(x)

            if x.isupper():
                contar("Mayusculas")

            if x.islower():
                contar("Minusculas")

        # validar valor numerico
        if x.isnumeric():
            numeros.append(x)
            contar("Numeros")

print("-> CADENA DE ENTRADA: " + entrada)
print("-> CADENA SIN ESPACIOS NI SÍMBOLOS: " +
      str().join(letras) + str().join(numeros))

# ahora ordenar letras
n = len(letras)
for x in range(n):

    if letras[x].isupper():
        mayus = letras[x]  # salvar mayuscula
        for i in range(n):
            if letras[i].islower():
                minus = letras[i]  # salvar minuscula
                letras[i] = mayus
                letras[x] = minus
                break

print("CANTIDAD DE CARACTÉRES:")
for k in contador.keys():
    print("* " + k + " : " + str(contador[k]))

print("CADENA FINAL: " + str().join(letras) + str().join(numeros))
print("---------------------------------------------------------")

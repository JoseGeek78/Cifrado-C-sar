def cifrado_cesar(texto, desplazamiento):
    """
    Aplica el cifrado César a un texto con un desplazamiento dado.
    :param texto: Texto a cifrar.
    :param desplazamiento: Número de posiciones a desplazar en el alfabeto.
    :return: Texto cifrado.
    """
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():  # Solo ciframos letras
            base = ord('A') if caracter.isupper() else ord('a')
            # Cifra el carácter aplicando el desplazamiento y respetando el rango
            nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo_caracter
        else:
            # No ciframos caracteres no alfabéticos
            resultado += caracter
    return resultado


# Solicitar entrada al usuario
palabra = input("Introduce la palabra a cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento (entero): "))

# Cifrar la palabra e imprimir el resultado
cifrado = cifrado_cesar(palabra, desplazamiento)
print(f"Palabra cifrada: {cifrado}")

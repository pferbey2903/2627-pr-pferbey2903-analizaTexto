
vocales: str = "aeiouáéíóúü"

def analizar_texto(frase: str) -> tuple[int, int]:

    num_vocales: int = 0

    for caracter in frase.lower():
        if caracter in vocales:
            num_vocales += 1

    num_palabras: int = len(frase.split())

    return (num_vocales, num_palabras)


def main():
    """Función principal"""

    frase: str = str(input("Escribe una frase: "))
    conversion: tuple[int, int] = analizar_texto(frase)
    print (f"Vocales: {conversion[0]} Palabras: {conversion[1]}")

if __name__ == "__main__":
    main()
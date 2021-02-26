def alfabeto(letra):
    lista = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
             'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
             'Z': 26}
    return lista[letra.upper()]

def converte_palavra(palavra):
    array = []
    conversao = []
    for letra in str(palavra):
        array.append(letra)

    for posicao in array:
        conversao.append(alfabeto(posicao))

    return conversao


if __name__ == '__main__':
    frase_1 = input("Digite a primeira palavra:\n")
    frase_2 = input("Digite a segunda palavra:\n")

    print(f"'{converte_palavra(frase_1)}'")
    print(f"'{converte_palavra(frase_2)}'")

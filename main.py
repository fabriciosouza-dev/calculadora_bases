def alfabeto(letra):
    lista = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
             'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
             'Z': 25}
    return lista[letra.upper()]

def converte_palavra(palavra):
    array = []
    conversao = []
    for letra in str(palavra):
        array.append(letra)

    for posicao in array:
        conversao.append(alfabeto(posicao))

    return conversao

def multiplica(frase_1,frase_2):
    vetor_1 = converte_palavra(frase_1)
    vetor_2 = converte_palavra(frase_2)

    # index = 0
    # while index < len(vetor_1):
    #     print(index, items[index])
    #     index += 1



if __name__ == '__main__':
    frase_1 = input("Digite a primeira palavra:\n")
    frase_2 = input("Digite a segunda palavra:\n")

    print(f"'{converte_palavra(frase_1)}'")
    print(f"'{converte_palavra(frase_2)}'")

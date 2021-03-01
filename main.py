def alfabeto(letra):
    lista = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
             'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
             'Z': 25}
    return lista[letra.upper()]


def alfabeto_invertido(numero):
    lista = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J',
             '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S',
             '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z'}
    return lista[str(numero)]


def converte_palavra(palavra):
    array = []
    conversao = []
    for letra in str(palavra):
        array.append(letra)

    for posicao in array:
        conversao.append(alfabeto(posicao))

    return conversao


def multiplica(frase_1, frase_2):
    if len(frase_1) <= len(frase_2):
        frase_menor = frase_1
        frase_maior = frase_2
    else:
        frase_menor = frase_2
        frase_maior = frase_1
    vetor_1 = converte_palavra(frase_menor)
    vetor_2 = converte_palavra(frase_maior)
    vetor_1.reverse()
    vetor_2.reverse()
    hash = {}

    index_1 = 0
    while index_1 < len(vetor_1):
        index_2 = 0
        hash[f"produto_{index_1}"] = []
        for x in range(index_1):
            hash[f"produto_{index_1}"].append(0)
        while index_2 < len(vetor_2):
            result = vetor_2[index_2] * vetor_1[index_1]
            if result >= 26:
                resto = result % 26
                quociente = int(result / 26)
                if len(hash[f"produto_{index_1}"]) - 1 - index_1 == index_2 and index_2 != 0:
                    hash[f"produto_{index_1}"][index_2 + index_1] += resto
                else:
                    hash[f"produto_{index_1}"].append(resto)
                hash[f"produto_{index_1}"].append(quociente)
            else:
                if len(hash[f"produto_{index_1}"]) - 1 == index_2:
                    hash[f"produto_{index_1}"][index_2 + index_1] += result
                else:
                    hash[f"produto_{index_1}"].append(result)
            index_2 += 1
        index_1 += 1
    return hash


def verifica_converte_array(array):
    index = 0
    new_array = array
    while index < len(new_array):
        if new_array[index] >= 26:
            quociente = int(new_array[index] / 26)
            new_array[index] = new_array[index] % 26
            try:
                new_array[index + 1] += quociente
            except:
                new_array.append(quociente)
        index += 1
    return new_array


def soma_vetores(hash):
    index = 0
    existe = True
    array = []
    while existe:
        try:
            hash[f"produto_{index}"]
            index += 1
        except:
            existe = False
    for x in range(index):
        array.append(hash[f"produto_{x}"])
    ml = max(map(len, array))
    return [sum(x) for x in zip(*map(lambda x: x + [0] * ml if len(x) < ml else x, array))]


def criptografa(frase_1, frase_2):
    hash = multiplica(frase_1, frase_2)
    vetor_somado = soma_vetores(hash)
    vetor_final = verifica_converte_array(vetor_somado)
    vetor_final.reverse()
    str = ''

    for x in vetor_final:
        str += alfabeto_invertido(x)
    return str


if __name__ == '__main__':
    frase_1 = input("Digite a primeira palavra:\n")
    frase_2 = input("Digite a segunda palavra:\n")
    print(f"\nA multiplicação das duas palavras é: '{criptografa(frase_1, frase_2)}'")
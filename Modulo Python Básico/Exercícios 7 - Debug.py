## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    tamanho = 1
    soma = 0.0
    for i, valor in enumerate(valores):
        soma += valor
        i += 1
    media = soma / tamanho

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = false

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))


# def calcular_media(valores):
#     tamanho = len(valores)  # Corrigido para obter o tamanho real da lista
#     soma = 0.0
#     for valor in valores:  # Não é necessário usar enumerate neste caso
#         soma += valor
#     media = soma / tamanho
#     return media  # Adicionado retorno à função

# continuar = True
# valores = []
# while continuar:
#     valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
#     if valor.lower() == 'ok':
#         continuar = False  # Corrigido para False com a primeira letra maiúscula
#     else:
#         valores.append(float(valor))  # Adiciona o valor à lista de valores como float

# media = calcular_media(valores)
# print('A média calculada para os valores {} foi de {}'.format(valores, media))

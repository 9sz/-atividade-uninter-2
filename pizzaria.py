print('Bem vindo à pizzaria do Matheus Felipe da Silva Marciano')
print('================|à la carte|================')
print('Código | Descrição  | Pizza M   | Pizza G')
print('-------------------------------------------')
print('  21   | Napolitana | R$ 20,00  | R$ 26,00 ')
print('  22   | Margherita | R$ 20,00  | R$ 26,00')
print('  23   | Calabresa  | R$ 25,00  | R$ 32,50')
print('  24   | Toscana    | R$ 30,00  | R$ 39,00')
print('  25   | Portuguesa | R$ 30,00  | R$ 39,00')
print('-------------------------------------------')
soma = 0
while True:
    codpizza = input('Qual o código da pizza?')
    tamanho = input('Qual o tamanho da pizza?')
    # valores pizzas M
    if tamanho == 'm' and codpizza == '21':
        soma = soma + 20
    elif tamanho == 'm' and codpizza == '22':
        soma = soma + 20
    elif tamanho == 'm' and codpizza == '23':
        soma = soma + 25
    elif tamanho == 'm' and codpizza == '24':
        soma = soma + 30
    elif tamanho == 'm' and codpizza == '25':
        soma = soma + 30
    # valores pizzas G
    elif tamanho == 'g' and codpizza == '21':
        soma = soma + 26
    elif tamanho == 'g' and codpizza == '22':
        soma = soma + 26
    elif tamanho == 'g' and codpizza == '23':
        soma = soma + 32.50
    elif tamanho == 'g' and codpizza == '24':
        soma = soma + 39
    elif tamanho == 'g' and codpizza == '25':
        soma = soma + 39

    else:
        print('Opção inválida! Lembre de usar letras minúsculas e o código correto!')
        continue

    pedir = input('Deseja mais algum item? (s/n)')

    if pedir == 's':
        continue
    else:
        print('O valor final da conta é {}R$' .format(soma))
        break

def mensagem():
    print('''Bem vindo ao meu primeiro programa''')
def calculadora():
    nome = str(input('Digite seu nome: '))
    n1 = int(input('Olá {} digite o primeiro número: '.format(nome)))
    operacao = input('''
Por favor selecione a operação matemática desejada para completar a operação:
+ para adição
- para subtração
* para multiplicação
/ para divisão
** para potência''')
    n2 = int(input('Agora que selecionou a operação {} digite o segundo número: '.format(operacao)))

    if operacao == '+':
        print('{} + {} = '.format(n1, n2), end=' ')
        print(n1 + n2)

    elif operacao == '-':
        print('{} - {} = '.format(n1, n2), end=' ')
        print(n1 - n2)

    elif operacao == '*':
        print('{} * {} = '.format(n1, n2), end=' ')
        print(n1 * n2)

    elif operacao == '/':
        print('{} / {} = '.format(n1, n2), end=' ')
        print(n1 / n2)

    elif operacao == '**':
        print('{} ** {} = '.format(n1, n2, ), end=' ')
        print(n1 ** n2)
    else:
        print('Você não digitou uma operação valida, por favor tente de novo')

    repetir()


def repetir():
    calc_repetir = input('''Deseja realizar uma nova operação? Por favor aperte S para SIM ou N para NÃO.''')
    if calc_repetir.upper() == 'S':
        calculadora()
    elif calc_repetir.upper() == 'N':
        print('Até a proxima.')
    else:
        repetir()

mensagem()
calculadora()

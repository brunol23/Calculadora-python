
nome = str(input('Digite seu nome: '))
num = int(input('Olá {}, digite o número para ver sua tabuada: '.format(nome)))
operacao = input('''Agora digite a operação desejada: 
+ ADIÇÃO
- SUBTRAÇÃO
* MULTIPLICAÇÃO
/ DIVISÃO''')

if operacao == '+':
    print('{} + {:2} = {}'.format(num, 0, num + 0))
    print('{} + {:2} = {}'.format(num, 1, num + 1))
    print('{} + {:2} = {}'.format(num, 2, num + 2))
    print('{} + {:2} = {}'.format(num, 3, num + 3))
    print('{} + {:2} = {}'.format(num, 4, num + 4))
    print('{} + {:2} = {}'.format(num, 5, num + 5))
    print('{} + {:2} = {}'.format(num, 6, num + 6))
    print('{} + {:2} = {}'.format(num, 7, num + 7))
    print('{} + {:2} = {}'.format(num, 8, num + 8))
    print('{} + {:2} = {}'.format(num, 9, num + 9))
    print('{} + {:2} = {}'.format(num, 10, num + 10))
elif operacao == '-':
    print('{} - {:2} = {}'.format(num, 0, num - 0))
    print('{} - {:2} = {}'.format(num, 1, num - 1))
    print('{} - {:2} = {}'.format(num, 2, num - 2))
    print('{} - {:2} = {}'.format(num, 3, num - 3))
    print('{} - {:2} = {}'.format(num, 4, num - 4))
    print('{} - {:2} = {}'.format(num, 5, num - 5))
    print('{} - {:2} = {}'.format(num, 6, num - 6))
    print('{} - {:2} = {}'.format(num, 7, num - 7))
    print('{} - {:2} = {}'.format(num, 8, num - 8))
    print('{} - {:2} = {}'.format(num, 9, num - 9))
    print('{} - {:2} = {}'.format(num, 10, num - 10))
elif operacao == '*':
    print('{} x {:2} = {}'.format(num, 0, num * 0))
    print('{} x {:2} = {}'.format(num, 1, num * 1))
    print('{} x {:2} = {}'.format(num, 2, num * 2))
    print('{} x {:2} = {}'.format(num, 3, num * 3))
    print('{} x {:2} = {}'.format(num, 4, num * 4))
    print('{} x {:2} = {}'.format(num, 5, num * 5))
    print('{} x {:2} = {}'.format(num, 6, num * 6))
    print('{} x {:2} = {}'.format(num, 7, num * 7))
    print('{} x {:2} = {}'.format(num, 8, num * 8))
    print('{} x {:2} = {}'.format(num, 9, num * 9))
    print('{} x {:2} = {}'.format(num, 10, num * 10))
elif operacao == '/':
    print('{} / {:2} = {}'.format(num, 0, num / 0))
    print('{} / {:2} = {}'.format(num, 1, num / 1))
    print('{} / {:2} = {}'.format(num, 2, num / 2))
    print('{} / {:2} = {}'.format(num, 3, num / 3))
    print('{} / {:2} = {}'.format(num, 4, num / 4))
    print('{} / {:2} = {}'.format(num, 5, num / 5))
    print('{} / {:2} = {}'.format(num, 6, num / 6))
    print('{} / {:2} = {}'.format(num, 7, num / 7))
    print('{} / {:2} = {}'.format(num, 8, num / 8))
    print('{} / {:2} = {}'.format(num, 9, num / 9))
    print('{} / {:2} = {}'.format(num, 10, num / 10))
else:
    print('Digite uma operação válida!!!')


num = int (input('Digite um valor qualquer: '))
opc = int (input('''Qual sera a base de conversão
[1] Para Binario
[2] para Octal
[3] para Hexadecimal: 
Sua opção: '''))
if opc == 1:
    print('Base escolhida Binario')
    print('''numero original {}.
Conversão para binario é igual a {}'''.format(num, bin(num)[2:]))

elif opc == 2:
    print('Base escolida Octal')
    print('''numero original {}.
Conversão para Octal é igual a {}'''.format(num, oct(num)[2:]))
elif opc == 3:
    print('base escolhida hexadecimal')
    print('''numero original {}.
Conversão para Hexadecimal é igual a {}'''.format(num, hex(num)[2:]))
else:
    print('Opção invalida favor adicionar uma possivel.')
nome = str (input('QUal o seu nome?:'))
valorCasa = float(input('{}, Qual o valor da casa?: '.format(nome)))
salario = float(input('{}, Qual o seu salario?: '.format(nome)))
prestacao = valorCasa/ (anos*12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {}'.format(valorCasa, anos), end='')
print('A prestação sera de R${:.2f}'. format(prestacao))

if prestacao <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo negado!')

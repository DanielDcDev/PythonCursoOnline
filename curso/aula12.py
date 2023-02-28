nome = str(input('QUal o seu nome ?: '))

if nome == 'Daniel':
    print('Que nome bonito!')
elif nome in ' Ana Claudia Jessica Juliana Maria':
    print('Belo nome senhora')
elif nome in ' Caio Matheus Alexandre Marcio João':
    print('Belo nome Cara')
else:
    print('Seu nome até que é normal hein!!')
print('tenha um bom dia {}' .format(nome))
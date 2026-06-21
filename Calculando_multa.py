vel=float(input('Qual a velocidade do carro?'))
if vel>80:
    valor = (vel - 80) * 7.00
    print('Você foi multado. Sua multa esta no valor de R${:.2f}.'.format(valor))
else:
    print('Você esta dentro da velocidade permitida!')

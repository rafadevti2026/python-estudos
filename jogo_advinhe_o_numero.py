from random import randint
computador=randint(0,5) 
print('---'*20)
print('Tente adivinhar em que número eu pensei...')
print('---'*20)
jogador=int(input('Em que número eu pensei?'))
print('Pensei no numero {}'.format(computador))
if computador==jogador:
    print('-----------Parabéns você acertou!!!!-------------')
else:
    print('--------------Que pena você errou!---------------')

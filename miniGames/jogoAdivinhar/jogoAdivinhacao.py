from random import randint
from time import sleep
print('\033[34m-=-\033[m' * 10)
print('\033[33m     Jogo da adivinhação\033[m')
print('\033[34m-=-\033[m' * 10)
print('\033[36mDigite um número de 1 ao 10\033[m')
jog = int(input('\033[35mNúmero: \033[m'))
pc = randint(1, 10)
print('\033[1mAguarde...\033[m')
sleep(3)
print('\033[34m-=-\033[m' * 10)
if jog == pc:
    print('\033[1;32mParabéns, você acertou o número!!!\033[m')
else:
    print('\033[31mVocê errou, tente novamente\033[m')
print('\033[34m-=-\033[m' * 10)
print('\033[36mNúmero escolhido pela máquina:\033[m \033[32m{}\033[m'.format(pc))
print('\033[34m-=-\033[m' * 10)

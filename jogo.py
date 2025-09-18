import random # MÓDULO que serve para gerar números aleatórios

print("Bem-vindo ao Advinhe o número!")
print("As regras são simples, Vou pensar em um número e você tentará advinhá-lo.")
numero = random.randint(1, 10)
isGuessRight = False
while isGuessRight != True:
    advinha = input("Digite um número de 1 a 10: ")
    if int(advinha) == numero:
        print("Você advinhou {}. O número está correto! Você ganhou!".format(advinha))
        isGuessRight - True
    else:
        print("Você digitou o número {}. Desculpe, não é isso. Tente novamente.".format(advinha))

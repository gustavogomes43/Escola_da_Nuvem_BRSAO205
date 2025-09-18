"""myString = "Isso é um string"
print(myString)
print(type(myString))
print(myString + " é do tipo de dado " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)"""

name = input(" Qual é o seu nome? ") # name é uma variável input pede uma entrada para o usuário
color = input(" Qual sua cor favorita? ")
animal = input(" Qual seu animal favorito? ")
print("(), voce gosta da cor () e do animal ()! ".format(name, color, animal))

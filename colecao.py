# LISTA
listaFrutas = ["abacate", "uva", "abacaxi"]
print("Minha lista de frutas original: ", listaFrutas)
print(type(listaFrutas))
print(listaFrutas[0])
print(listaFrutas[1])
print(listaFrutas[2])
listaFrutas[0] = "MAÇA"
print("Minha lista de frutas alterada: ", listaFrutas)

# TUPLA
tuplaFrutas = ("abacate", "uva", "abacaxi")
print("A minha TUPLA de frutas é: ", tuplaFrutas)
print("O tipo de dados da minah TUPLA é: ", type(tuplaFrutas))
print(tuplaFrutas[0])
print(tuplaFrutas[1])
print(tuplaFrutas[2])

# DICIONARIO
dicioFrutas = {
    "Ricardo": "Limão",
    "Gustavo": "Uva",
    "Taciara": "Tangerina",
    "Carol": "Manga"
}
print("Meu dicionario de Pessoas e frutas preferidas é: ", dicioFrutas)
print(type(dicioFrutas))
print("A Carol gosta de", dicioFrutas["Carol"])
print(dicioFrutas["Gustavo"])
print(dicioFrutas["Ricardo"])
print(dicioFrutas["Taciara"])

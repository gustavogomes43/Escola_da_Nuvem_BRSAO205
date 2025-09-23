def num_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) +1):
        if numero % i == 0:
            return False
    return True
numeros_primos = []
for n in range(1, 251):
    if num_primo(n):
        numeros_primos.append(n) 
print("Números primos entre 1 e 250:")
print(numeros_primos)
with open("resultado.txt", "w") as arquivo:
    arquivo.write("Números primos de 1 a 250:\n")
    for primo in numeros_primos:
        arquivo.write(str(primo) + "\n")
print("Arquivos salvos com sucesso!")


# Explicação linha a linha
def num_primo(numero):
1. Define uma função chamada num_primo que recebe um parâmetro numero. 
Em Python def cria a função; numero é o valor que a função vai testar se é primo.

    if numero < 2:
        return False
2. Verifica se o número é menor que 
2. Por definição, números primos são inteiros maiores ou iguais a 
2. Se numero for 0, 1 ou negativo, a função já retorna False (não é primo).

    for i in range(2, int(numero ** 0.5) +1):
3. Inicia um laço for com i variando de 2 até int(numero ** 0.5) + 1 (o limite de range é exclusivo).

numero ** 0.5 calcula a raiz quadrada do número (como float).

int(...) converte para inteiro (arredonda para baixo).

+1 garante que a raiz seja incluída quando for exata.
Por que testar só até a raiz? Se numero tem um divisor d maior que a raiz, então existe outro divisor e = numero / d menor que a raiz. 
Assim basta procurar divisores até a raiz — economiza verificações.

        if numero % i == 0:
            return False
4. Dentro do laço, usa o operador % (resto da divisão). 
Se numero % i == 0 significa que i divide numero exatamente — então numero é composto, não primo, e retornamos False imediatamente (podemos sair cedo).

        return True
5. Se o laço terminou sem encontrar nenhum divisor, nenhum i dividiu o número → o número é primo. Retorna True.

Próxima parte do código — coleta os primos entre 1 e 250:

numeros_primos = []
6. Cria uma lista vazia chamada numeros_primos para armazenar os primos encontrados.

for n in range(1, 251):
7. Percorre n de 1 até 250 (em range, o limite superior é exclusivo, então usamos 251 para incluir 250).

    if num_primo(n):
        numeros_primos.append(n)
8. Para cada n, chama num_primo(n). Se a função retornar True (é primo), n é adicionado (append) à lista numeros_primos.

    print("Números primos entre 1 e 250:")
print(numeros_primos)
9. Imprime uma mensagem explicativa e depois imprime a lista com todos os primos encontrados.

# Resultado (o que seu programa vai mostrar)
O código encontrou 53 números primos entre 1 e 250. A lista é:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241

# Melhorias simples (mais eficiente e robusta)
1. Evitar testar pares depois de checar o 2 (poupança ~ metade das iterações):

import math

def num_primo_melhor(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    limite = math.isqrt(numero)      # inteiro exato da raiz
    for i in range(3, limite + 1, 2): # testa só ímpares
        if numero % i == 0:
            return False
    return True

2. Para gerar muitos primos rapidamente (até grandes limites), usar Crivo de Eratóstenes (Sieve) é muito mais rápido: complexidade aproximadamente 
𝑂(𝑛loglog𝑛).




                                                                                                                                    

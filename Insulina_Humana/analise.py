# Variável que armazena insulina humana
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
print("Sequência pré-pró-insulina:")
print(preproInsulin)
print("Comprimento da sequência:", len(preproInsulin), "caracteres\n")

lsInsulina = "malwmrllpllallalwgpdpaaa"
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulina = "giveqcctsicslyqlenycn"
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulina = bInsulina + aInsulina
print("Sequência LS:", lsInsulina, "tamanho", len(lsInsulina))
print("Sequência A:", aInsulina, "tamanho", len(aInsulina))
print("Sequência B:", bInsulina, "tamanho", len(bInsulina))
print("Sequência C:", cInsulina, "tamanho", len(cInsulina), "\n")
print("Sequência da insulina (B + A):")
print(insulina)
print("Comprimento da insulina:", len(insulina), "caracteres\n")



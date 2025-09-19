# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulina = "malwmrllpllallalwgpdpaaa"  
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulina = "giveqcctsicslyqlenycn"  
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulina = bInsulina + aInsulina

pKR = {
    'y':10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25,
}
print("\nDicionário pKR.")
print(pKR)
print("\nContando o Y:")
print("quantidade de Y: ", float(insulina.count("y")))
seqContar = {x: float(insulina.count(x)) for x in ['y','c','k','h','r','d','e']}
print("\n")
print(seqContar)
print("\n")

pH = 0
while (pH <= 14):
    cargaLiquida = (
        +(sum({x: ((seqContar[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqContar[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
    print("pH:", '{0:2f}'.format(pH), "Carga liquida: ", cargaLiquida)
    pH += 1
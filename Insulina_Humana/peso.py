# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulina = "giveqcctsicslyqlenycn"
insulina = bInsulina + aInsulina

aaPesos = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaContarInsulina = ({x: float(insulina.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
pesoMolecularInsulina = sum({x: (aaContarInsulina[x]*aaPesos[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("O peso molecular aproximado da insulina é: " +
str(pesoMolecularInsulina))

pesoMolecularInsulinaReal = 5807.63
print("Porcentagem de erro: " + str(((pesoMolecularInsulina - 
pesoMolecularInsulinaReal)/pesoMolecularInsulinaReal)*100))




'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 
'''

# Faturamento por estado em forma de dicionário
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# SOma os valores do dicionário
faturamento_total = sum(faturamento_estados.values())

# Calcula o percentual e cria outro dicionário, onde percentual é 100*valor/faturamento_total
percentuais = {estado: 100*(valor / faturamento_total) for estado, valor in faturamento_estados.items()}

print(f"Faturamento total: R${faturamento_total:.2f}\n")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}% de representação")

'''
Faturamento total: R$180759.98

SP: 37.53% de representação
RJ: 20.29% de representação
MG: 16.17% de representação
ES: 15.03% de representação
Outros: 10.98% de representação
'''
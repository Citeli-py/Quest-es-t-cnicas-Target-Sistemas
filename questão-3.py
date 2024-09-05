'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json

def calcular_faturamento(dados):
    # Filtra os dias com faturamento, final de semana faturamento == 0.0
    faturamentos_validos = [dia['valor'] for dia in dados if dia['valor'] > 0]

    # Calcula menor e maior
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)

    # Calcula a média mensal 
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

    # Coloca 1 nos dias com faturamento acima da média e soma tudo
    dias_acima_da_media = sum([1 for valor in faturamentos_validos if valor > media_mensal]) 

    return menor_faturamento, maior_faturamento, dias_acima_da_media

dados_faturamento = json.load(open("dados.json", 'r'))
menor_fat, maior_fat, dias_acima_media = calcular_faturamento(dados_faturamento)

print(f"Menor valor de faturamento: R${menor_fat:.2f}")
print(f"Maior valor de faturamento: R${maior_fat:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")


'''
Menor valor de faturamento: R$373.78
Maior valor de faturamento: R$48924.24
Número de dias com faturamento acima da média: 10
'''
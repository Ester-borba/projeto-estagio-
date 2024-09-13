import json

# Exemplo de dados em JSON
dados = '''
[
    {"dia": 1, "faturamento": 1000},
    {"dia": 2, "faturamento": 1500},
    {"dia": 3, "faturamento": 0},
    {"dia": 4, "faturamento": 2000},
    {"dia": 5, "faturamento": 0},
    {"dia": 6, "faturamento": 3000}
]
'''

faturamento = json.loads(dados)

valores = [dia["faturamento"] for dia in faturamento if dia["faturamento"] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

import json

#abertura do arquivo JSON
with open('faturamento.json', 'r') as file:
    data = json.load(file)

#leitura do faturamento em json com valores acima de 0
faturamentoDiario = [dia["valor"] for dia in data ["faturamentoDiario"] if dia["valor"] > 0]

#menor e maior valor de faturamento
menorFaturamento = min(faturamentoDiario)
maiorFaturamento = max(faturamentoDiario)

print(f"Menor valor de faturamento: R$ {menorFaturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maiorFaturamento:.2f}")

#média do faturamento
mediaFaturamento = sum(faturamentoDiario) / len(faturamentoDiario)
print(f"Média de faturamento: R${mediaFaturamento:.2f}")

#dias com faturamento acima da média
diasAcimaDaMedia = sum(1 for valor in faturamentoDiario if valor > mediaFaturamento)
print(f"Dias com faturamento acima da média: {diasAcimaDaMedia}")



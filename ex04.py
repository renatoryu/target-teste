faturamentoSp = 67836.43
faturamentoRj = 36678.66
faturamentoMg = 29229.88
faturamentoEs = 27165.48
faturamentoOutros = 19849.53

faturamentoTotal = faturamentoSp+faturamentoRj+faturamentoMg+faturamentoEs+faturamentoOutros

percentualSp = (faturamentoSp / faturamentoTotal) * 100
percentualRj = (faturamentoRj / faturamentoTotal) * 100
percentualMg = (faturamentoMg / faturamentoTotal) * 100
percentualEs = (faturamentoEs / faturamentoTotal) * 100
percentualOutros = (faturamentoOutros / faturamentoTotal) * 100

print(f"Percentual de representação de SP: {percentualSp:.2f}%")
print(f"Percentual de representação de RJ: {percentualRj:.2f}%")
print(f"Percentual de representação de MG: {percentualMg:.2f}%")
print(f"Percentual de representação de ES: {percentualEs:.2f}%")
print(f"Percentual de representação de Outros: {percentualOutros:.2f}%")



# Exercício 4: Análise de Margem de Lucro (Financeiro)
# Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

faturamento = 15000
custos_fixos = 5000
percentual_imposto = 0.15

#cálculo do imposto
imposto = faturamento * percentual_imposto

#lucro líquido
lucro_liquido = faturamento - custos_fixos - imposto

#margem de lucro
margem_lucro = lucro_liquido / faturamento


meta_atingida = margem_lucro > 0.3
print(f'Sua empresa teve um lucro líquido de R$ {lucro_liquido:.2f}, com a margem de lucro de {margem_lucro:.1f}%')
print(f'Significa que a meta de 0.3 foi atingida? {meta_atingida}')





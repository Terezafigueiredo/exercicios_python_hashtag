# Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total 
# para a equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento 
# final da empresa após subtrair esse bônus.
# ●	Faturamento inicial: 50.000
# ●	Percentual de bônus: 0.10 significa 10 por cento

faturamento_inicial = 50000
bonus = 0.10

valor_bonus = faturamento_inicial * bonus
faturamento_final = faturamento_inicial - valor_bonus
print(f'O faturamento final da empresa foi de R${faturamento_final:.2f}')


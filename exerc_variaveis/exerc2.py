# Exercício 2: Controle de Estoque de E-commerce (Logística)
# Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final. 

estoque_smart = 250
vendidos= 78
reposicao_dia = 100

estoque_smart2 = estoque_smart - vendidos
estoque_final = estoque_smart2 + reposicao_dia
print(f'Iniciamos o dia com {estoque_smart} smartphones.')
print(f'Vendemos {vendidos} ao longo do dia. Tivemos uma reposição de {reposicao_dia} smartphones')
print(f'E fechamos nosso estoque com {estoque_final} aparelhos.')






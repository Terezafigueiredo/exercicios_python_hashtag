# Exercício 3: Análise de Metas de Vendas (Setor Comercial) 
# Um gerente quer comparar o desempenho de duas filiais. O programa deve:
# 1.	Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar números decimais).
# 2.	Calcular o faturamento total das duas lojas.
# 3.	Calcular a média de faturamento entre elas.
# 4.	Exibir uma única mensagem formatada informando o total e a média, utilizando o separador de milhar e duas casas decimais.

fat_a = float(input('Digite o faturamento da loja A:'))
fat_b = float(input('Digite o faturamento da loja B:'))
fat_total = fat_a + fat_b
media_fat = fat_total / 2
print(f'O faturamento total das lojas foi de {fat_total:,.2f} e a média do faturamento foi de {media_fat:,.2f}')
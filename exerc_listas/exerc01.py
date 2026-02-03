# Exercício 1: Dashboard de Vendas (Análise de Dados) 
# Você recebeu uma lista com as vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. 
# Crie um programa que exiba um pequeno relatório contendo:
# 1.	O total de vendas na semana.
# 2.	A média de vendas diária.
# 3.	O valor da melhor venda e da pior venda do período.
lista_vendas_dia = [1500, 2000, 800, 3500, 1200]
total_vendas_semana = sum(lista_vendas_dia)
print(f'O total de vendas da semana foi de R$ {total_vendas_semana:.2f}')

# print(len(lista_vendas_dia))  #me mostra o tamanho da lista e imprime o que estiver na posição que eu quiser
# primeiro = lista_vendas_dia[-1]
# print(primeiro)

#A MÉDIA DE UMA LISTA É CALCULADA DIVIDINDO A SOMA TOTAL DOS ELEMENTOS (sum()) pelo numero de itens na lista len(lista) media = (sum())/len(lista)

media = sum(lista_vendas_dia) / len(lista_vendas_dia)
print (f'A média de vendas diárias da loja foi de R$ {media:.2f}')

#O valor da melhor venda 

melhor_venda = max(lista_vendas_dia)
print(f'O valor da melhor venda do dia foi R$ {melhor_venda:.2f}')

pior_venda = min(lista_vendas_dia)
print(f'O valor da pior venda do dia foi R$ {pior_venda:.2f}')
# Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal) 
# Uma empresa de serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. 
# Como o valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
# 1.	Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
# 2.	Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
# 3.	Converter para número decimal (float).
# 4.	Calcular o valor do imposto (15% do valor bruto).
# 5.	Exibir uma mensagem formatada com f-string mostrando o valor do imposto com duas casas decimais.

valor_bruto = input('Digite o valor bruto da nota fiscal (Ex: R$ 5.000,00): ')

valor_limpo = valor_bruto.replace("R$", "").replace(".", "").replace(",", ".") 
# estou substituindo o R$, , e .  por um espaço vazio

valor_bruto = float(valor_limpo)

imposto = valor_bruto * 0.15
print(f'O valor do imposto a ser pago será de: R$ {imposto:.2f}')





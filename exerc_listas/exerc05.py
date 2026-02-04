# Exercício 5: Atualização de Preços Interativa (Input + Lista) 
# Você tem uma lista de preços de produtos: precos = [100.0, 250.0, 500.0]
# e uma com o nome: vinhos = ["Branco", "Tinto","Champagne"]. 
# Crie um programa interativo que:
# 1.	Peça para o usuário digitar qual o nome do produto.
# 2.	Peça para o usuário digitar o novo preço.
# 3.	Atualize o preço na lista e exiba as listas completas com os nomes e os preços

precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto","Champagne"]
produto = input('Digite o tipo do vinho (Branco, Tinto ou Champagne): ')
novo_preco = float(input(f'Digite o novo preço para {produto}: '))

if produto in vinhos:
    indice = vinhos.index(produto)# encontra a posição do produto
    precos[indice] = novo_preco   # atualiza o preço correspondente
    print("\nLista atualizada:")
    for nome, preco in zip(vinhos, precos): 
        print(f"{nome}: R$ {preco:.2f}")
else:
    print('Produto não encontrado na lista.')
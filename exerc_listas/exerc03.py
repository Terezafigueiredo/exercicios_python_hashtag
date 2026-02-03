# Exercício 3: Organização de Preços (Ordenação e Slicing) 
# Uma importadora listou os preços de frete em dólar: fretes = [50, 80, 20, 150, 40]. 
# Para apresentar em uma reunião, você deve:
# 1.	Ordenar a lista do maior para o menor preço.
# 2.	Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova lista chamada top_fretes.
# 3.	Exibir a lista original ordenada e a lista dos top_fretes.

fretes = [50, 80, 20, 150, 40]
# 1.	Ordenar a lista do maior para o menor preço.
fretes_ordenados = sorted(fretes, reverse= True) 
# 1. Ordenar a lista em ordem decrescente (reverse=True)
# sorted() cria uma nova lista ordenada, preservando a original.

print(fretes_ordenados)

# 2.	Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova lista chamada top_fretes.

top_fretes = fretes_ordenados[:2]
print(top_fretes)

# 3.	Exibir a lista original ordenada e a lista dos top_fretes.
print(f'Esses foram os valores dos fretes ordenados: {fretes_ordenados}')
print(f' Essa é a lista dos melhores valores de frete: {top_fretes}')





# Exercício 4: Sistema de Logística (Busca e Extensão) 
# A empresa "LogTrack" tem uma rota de entregas: rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]. 
# Novas cidades foram adicionadas por uma empresa parceira: novas_cidades = ["Itu", "Valinhos"]. Seu script deve:
# 1.	Unir as duas listas em uma só (usando extend).
# 2.	Identificar em qual posição (índice) está a cidade de "Sorocaba".
# 3.	Exibir a lista completa e a posição encontrada.
# 4.	Exibir uma mensagem final: “Sorocaba é a Xª cidade da rota”

rota = ['São Paulo', 'Campinas', 'Jundiai', 'Sorocaba']
novas_cidades = ['Itu', 'Valinhos']

rota.extend(novas_cidades) # 1.	Unir as duas listas em uma só (usando extend)
print(rota)

posicao_sorocaba = rota.index('Sorocaba') # 2.	Identificar em qual posição (índice) está a cidade de "Sorocaba"
print(f'O lista contém os seguintes itens: {rota}, e Sorocaba está na posição {posicao_sorocaba}.')# 3.	Exibir a lista completa e a posição encontrada.
print(f'Sorocaba é a {posicao_sorocaba}\u00b0 cidade da rota')# 4.	Exibir uma mensagem final: “Sorocaba é a Xª cidade da rota”

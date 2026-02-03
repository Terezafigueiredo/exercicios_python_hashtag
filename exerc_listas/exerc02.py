# #Exercício 2: Gestão de Estoque (Edição e Verificação) Uma loja de eletrônicos possui os seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"]. O gerente pediu para:
# 1.	Adicionar o item "webcam" ao final da lista.
# 2.	O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa alteração na lista.
# 3.	Verificar se "impressora" está no estoque. O programa deve exibir True ou False.
# 4.	Remover o "mouse" da lista, pois saiu de linha.



# 1.	Adicionar o item "webcam" ao final da lista.
estoque = ['Monitor', 'Teclado', 'Mouse', 'Headset']
estoque.append('Webcam')
print(estoque)

# 2.	O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa alteração na lista.
existe_na_lista = 'Teclado' in estoque #verifico se existe o produto no estoque
print(existe_na_lista)
posicao_teclado = estoque.index('Teclado')#verifico a posição do meu item na lista
print(posicao_teclado)
estoque[1] = 'Teclado mecânico'#aqui eu modifiquei o nome do meu item
print(estoque)

existe_na_lista2 = 'Impressora' in estoque # 3.	Verificar se "impressora" está no estoque. O programa deve exibir True ou False.
print(existe_na_lista2)

estoque.remove('Mouse')# 4.	Remover o "mouse" da lista, pois saiu de linha.
print(estoque)

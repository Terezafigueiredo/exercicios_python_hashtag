# Exercício 5: Personalização de E-mail de Marketing (Setor de Marketing) O marketing quer enviar um e-mail de boas-vindas. 
# O cliente forneceu o nome completo: lucas ferreira souza. 
# Você deve extrair apenas o primeiro nome para usar na saudação (ex: "Olá, Lucas!"). 
# O código deve:
# 1.	Encontrar a posição do primeiro espaço.
# 2.	Fatiar o texto para pegar apenas o primeiro nome.
# 3.	Formatar o nome com a primeira letra maiúscula.
# 4.	Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"
mensagem = 'Olá [primeiro nome], seja bem vindo ao nosso clube!' #d da mensagem modelo
nome = 'Lucas Ferreira Souza'
posicao = nome.find(' ') #encontrar a posição do primeiro espaço
pri_nome = nome[:posicao].capitalize() #pega os caracteres do início até o índice do espaço (sem incluir o espaço)
mensagem = mensagem.replace("[primeiro nome]", pri_nome)
print(mensagem)



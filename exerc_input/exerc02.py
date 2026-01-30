# Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH) 
# Ao cadastrar um novo funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o e-mail. 
# Crie um programa que:
# 1.	Peça o nome completo do colaborador.
# 2.	Peça o e-mail pessoal do colaborador.
# 3.	Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).
# 4.	Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).
# 5.	Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail padronizado]".

nome = input('Nome do colaborador: ')
email = input('E-mail do colaborador: ')
posicao = nome.find(' ') #encontrar a posição do primeiro espaço
prim_nome = nome[:posicao].title() #mostra o primeiro nome  # coloca as primeiras letras dos nomes maiuscula
email = email.strip().lower() #(remova espaços extras e deixe tudo em letras minúsculas)
print(f'Cadastro concluído: {prim_nome}. E-mail de acesso: {email}')
# Exercício 2: Padronização de Dados de CRM (Setor de Vendas) Um vendedor cadastrou um cliente com os dados desorganizados no sistema: nome = " mArCoS aNtOnIo rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ". Para evitar duplicidade e erros de envio, você deve:
# 1.	Remover os espaços extras no início e fim das duas variáveis.
# 2.	Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo (formato de nome próprio).
# 3.	Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.
# strip() → remove espaços no início e no fim.

# lstrip() → remove só do lado esquerdo.

# rstrip() → remove só do lado direito.

# replace(" ", "") → remove todos os espaços da string (inclusive entre palavras).
nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "
nome = nome.strip().title() # Remove espaços extras no início e fim # coloca as primeiras letras dos nomes maiuscula
print(nome)

email = email.strip() # Remove espaços extras no início e fim
email = email.lower() #coloca o e-mail em letra minuscula
print(email)

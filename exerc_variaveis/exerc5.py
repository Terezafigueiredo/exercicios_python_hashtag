# Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
# Cenário: Um contrato de manutenção de software tem a duração de 40 meses. 
# O cliente quer ver esse tempo no formato: "X anos e Y meses". 
# Objetivo: Utilize os operadores de divisão inteira e resto da divisão para converter os 40 meses.

duracao_contrato = 40
conversao_ano = 40 // 12
conversao_mes = 40 % 12
print(f'Seu contrato tem a duração de {conversao_ano} anos e {conversao_mes} meses')

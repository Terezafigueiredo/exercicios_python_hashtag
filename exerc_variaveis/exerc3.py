# Exercício 3: Divisão de Cargas (Logística/Transporte)
# Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. 
# Cada caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma última viagem menor? (Use %)

total_caixas = 1250
cada_caminhao = 12
caminhoes = total_caixas // cada_caminhao
sobra_caixas = total_caixas % caminhoes
print(f'Serão necessário {caminhoes} caminhões cheios e sobrarão {sobra_caixas} caixas')
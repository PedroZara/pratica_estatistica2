# Distribuição T de Student

# Importando a função para realizar o teste
from scipy.stats import t

# t.cdf -> implica em prob à esquerda da distribuição

# t.sf -> implica em prob à direita da distribuição

#%%

""" Tendo a média de salário de um cientista de dados sendo R$75,00 por hora, num amostra com 9 funcionários
 e desvio padrão sendo 10. Com isso temos t = 1.5 e n-1 = 8 """

# Qual a probabilidade de selecionar um cientista e o salário ser menor que R$80,00 por hora
prob_men80 = t.cdf(1.5, 8)

# Qual a probabilidade de selecionar um cientista e o salário ser maior que R$80,00 por hora
prob_mai80 = t.sf(1.5, 8)

#prob total

p_total = prob_men80 + prob_mai80

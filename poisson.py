from scipy.stats import poisson

"Média de acidentes de carro são 2 por dia"

#%%

'Qual a prob de acontecer 3 acidentes/dia'

prob_3_dia = poisson.pmf(3,2)

#%%

'Prob de acontecer 3 ou menos por dia'

prob_3oum_dia = poisson.cdf(3,2)

#%%

'Prob de ocorrerem mais de 3 por dia'

prob_3oumais_dia = poisson.sf(3,2)

probtotal = prob_3oumais_dia + prob_3oum_dia

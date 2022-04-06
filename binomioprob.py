from scipy.stats import binom

#%%

''' Jogando uma moeda 5x, qual a probabilidade de dar cara 3x?'''

prob1 = binom.pmf(3, 5, 0.5) * 100
print(f'A probabilidade 1 é de {prob1}%')

#%%

''' Passar por 4 sinais de 4 tempos, quais as probabilidades associadas?'''

prob_0 = binom.pmf(0, 4, 0.25) * 100
prob_1 = binom.pmf(1, 4, 0.25) * 100
prob_2 = binom.pmf(2, 4, 0.25) * 100
prob_3 = binom.pmf(3, 4, 0.25) * 100
prob_4 = binom.pmf(4, 4, 0.25) * 100
print(f'A probabilidade de zero sinais é de {prob_0}%')
print(f'A probabilidade de um sinal é de {prob_1}%')
print(f'A probabilidade de dois sinais é de {prob_2}%')
print(f'A probabilidade de três sinais é de {prob_3}%')
print(f'A probabilidade de quatro sinais é de {prob_4}%')

#%%

#probabilidade acumulativa

# 4 semáforos e 2 sucessos
prob_acum = binom.cdf(2, 4, 0.25) * 100
print(prob_acum)

#%%

''' Concurso com 12 questões, qual a probabilidade de acertar 7 no chute? Com 4 alternativas cada'''

prob_prova = binom.pmf(7, 12, 0.25) * 100
print(f'A probabilidade de passar no chute é de {prob_prova}%')

prob_cagada = binom.pmf(12, 12, 0.25) * 100
print(f'A probabilidade de acertar todas no chute é de {prob_cagada}%')

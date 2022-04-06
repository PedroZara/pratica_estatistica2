import numpy as np
from scipy.stats import chi2_contingency

#%%

''' Criando uma matriz com os dados para execução do teste'''
novela = np.array([[19,6], [43,32]])

#%%

''' O segundo valor é o pvalue'''
''' Se o valor de p é maior que 0,05 nao há evidencias de diferença significatica (hipótese nula)'''

p1 = chi2_contingency(novela)

#%%

novela2 = np.array([[22,3], [43,32]])
p2 = chi2_contingency(novela2)

#%%

print(f'No caso "novela" NÃO há evidências significativas de que a proporção de homens assistem menos novela, há que o p é igual a {p1[1]}')
print()
print(f'No caso "novela2" HÁ evidências significativas de que a proporção de homens assistem menos novela, há que o p é igual a {p2[1]}')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

#%%

# Carregamento da base de dados
tratamento = pd.read_csv('anova.csv', sep = ';')

#%%

# Boxplot agrupando os dados por remédio
tratamento.boxplot(by = 'Remedio', grid = False)
plt.tight_layout()

#%%

# Criação do modelo de regressão linear e execução do teste
modelo1 = ols('Horas ~  Remedio', data = tratamento).fit()
resultados1 = sm.stats.anova_lm(modelo1)
# Observar se p maior que 0,05 (Pr(>F)) hipótese nula de que nao haja diferença significativa

#%%

# Criação do segundo modelo de regressão linear e execução do teste
modelo2 = ols('Horas ~  Remedio * Sexo', data = tratamento).fit()
resultados2 = sm.stats.anova_lm(modelo2)
# Nenhum valor de P mostram alguma diferença significativa

#%%

# Se houver diferença o teste de Tukey é executado
# Execução e visualização dos dados

mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd()
print(resultado_teste)
resultado_teste.plot_simultaneous()

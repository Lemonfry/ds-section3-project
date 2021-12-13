import pandas as pd

df_csv = pd.read_csv('heart_disease_health_indicators_BRFSS2015.csv')
df_csv.dropna(axis = 0, how = 'any', inplace = True)
df_csv.to_csv('heart_disease_health_indicators_BRFSS2015.csv', index = False)
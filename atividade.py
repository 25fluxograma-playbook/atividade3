import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carregar os dados
df1 = pd.read_csv('oriente.csv')
df2 = pd.read_csv('mundial_petroleo.csv')

# 2. Unir datasets (ajustado para suas colunas)
df_final = pd.merge(df1, df2, left_on=['Country', 'Year'], right_on=['cty_name', 'year'])

# 3. Limpeza básica para o modelo funcionar
cols_interesse = ['oil_price_nom', 'oil_prod32_14', 'GDP_current_USD', 'GDP_growth_annual_pct']
df_ml = df_final[cols_interesse].dropna()

X = df_ml[['oil_price_nom', 'oil_prod32_14']]
y = df_ml['GDP_growth_annual_pct']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- MÉTODO DA LITERATURA (Linear) ---
model_lit = LinearRegression()
model_lit.fit(X_train[['oil_price_nom']], y_train)
pred_lit = model_lit.predict(X_test[['oil_price_nom']])

# Filtrando apenas dados de um país específico (Estruturas de Dados e Operações Básicas, ex: Irã) 
df_ira = df_final[df_final['Country'] == 'Iran']

# Selecionando apenas colunas de interesse
colunas_foco = ['Country', 'Year', 'GDP_growth_annual_pct', 'oil_price_nom']
df_resumo = df_final[colunas_foco]

# Ordenando pelos anos mais recentes e maior crescimento de PIB( Limpezae Tratamento de Dados)
df_sorted = df_final.sort_values(by=['Year', 'GDP_growth_annual_pct'], ascending=[False, False])

# Média de crescimento por país(Agrupamento)
media_pib_pais = df_final.groupby('Country')['GDP_growth_annual_pct'].mean()

# 4. MÉTODO PRÓPRIO (Random Forest) ---
model_prop = RandomForestRegressor(n_estimators=100, random_state=42)
model_prop.fit(X_train, y_train)
pred_prop = model_prop.predict(X_test)

# 5. Cálculo das Métricas (MSE)
mse_lit = mean_squared_error(y_test, pred_lit)
mse_prop = mean_squared_error(y_test, pred_prop)

# 6. Tabela de Resultados para o AVA/Demoday
resultados = pd.DataFrame({
    'Metodo': ['Literatura (Linear)', 'Proprio (Random Forest)'],
    'Erro Medio Quadratico (MSE)': [mse_lit, mse_prop],
    'Melhor Performance': ['' if mse_lit < mse_prop else 'X', 'X' if mse_prop < mse_lit else '']
})

print("\n=== TABELA DE COMPARACAO ===")
print(resultados)
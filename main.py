# main.py
import pandas as pd
import numpy as np

# =======================================
# MICROATIVIDADE 1 - Ler o arquivo CSV
# =======================================
df = pd.read_csv(
    'dataset.csv',
    header=None,
    names=['all_data'],
    engine='python',
    encoding='utf-8'
)

# Dividir a coluna 'all_data' usando o separador ';'
df = df['all_data'].str.split(';', expand=True)

# Ajustar nomes das colunas
df.columns = ['ID', 'Duration', 'Date', 'Pulse', 'Maxpulse', 'Calories']

# Remover aspas simples da coluna 'Date'
df['Date'] = df['Date'].str.replace("'", "")

# Converter colunas numéricas
numeric_cols = ['ID', 'Duration', 'Pulse', 'Maxpulse', 'Calories']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remover primeira linha caso seja o cabeçalho antigo
df = df[df['ID'].notna()]

print("======= MICROATIVIDADE 1 =======")
print("Conjunto de dados original (primeiras linhas):")
print(df.head())
print("\n")

# =======================================
# MICROATIVIDADE 2 - Criar um subconjunto de dados
# =======================================
sub_df = df[['ID', 'Date', 'Calories']]

print("======= MICROATIVIDADE 2 =======")
print("Subconjunto de dados com ID, Date e Calories:")
print(sub_df.head())
print("\n")

# =======================================
# MICROATIVIDADE 3 - Configurar número máximo de linhas exibidas
# =======================================
pd.set_option('display.max_rows', 9999)


print("======= MICROATIVIDADE 3 =======")
print("DataFrame completo exibido com to_string():")
print(df.to_string())
print("\n")

# =======================================
# MICROATIVIDADE 4 - Exibir primeiras e últimas 10 linhas
# =======================================
print("======= MICROATIVIDADE 4 =======")
print("Primeiras 10 linhas:")
print(df.head(10))
print("\nÚltimas 10 linhas:")
print(df.tail(10))
print("\n")

# =======================================
# MICROATIVIDADE 5 - Informações gerais
# =======================================
print("======= MICROATIVIDADE 5 =======")
print(df.info())
print("\n")

# =======================================
# LIMPEZA E TRATAMENTO DE DADOS
# =======================================
clean_df = df.copy()
clean_df['Calories'].fillna(0, inplace=True)
clean_df['Date'].fillna('1900/01/01', inplace=True)
clean_df['Date'].replace('1900/01/01', np.nan, inplace=True)
clean_df['Date'] = clean_df['Date'].astype(str).replace('20201226', '2020/12/26')
clean_df['Date'] = pd.to_datetime(clean_df['Date'], errors='coerce')
clean_df.dropna(subset=['Date'], inplace=True)

print("======= DATAFRAME FINAL =======")
print(clean_df)
print("\n")

# Salvar DataFrame limpo
clean_df.to_csv('dataset_limpo.csv', sep=';', index=False)
print("Arquivo 'dataset_limpo.csv' gerado com sucesso!")

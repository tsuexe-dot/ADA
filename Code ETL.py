import pandas as pd

# 1. Extract - Ler CSV do GitHub
url = "https://github.com/tsuexe-dot/ADA/blob/main/Banco.csv"
df = pd.read_csv(https://github.com/tsuexe-dot/ADA/blob/main/Banco.csv)

print("Dados originais:")
print(df.head())

# 2. Transform - Exemplo de transformação
# Remover valores nulos
df = df.dropna()

# Renomear colunas
df = df.rename(columns={"ID": "id_cliente"})

# Criar uma nova coluna derivada
df["ID"] = df["id_cliente"] * 2

print("Dados transformados:")
print(df.head())

# 3. Load - Salvar em novo CSV
df.to_csv("dados_transformados.csv", index=False)

print("ETL concluída! Arquivo salvo como dados_transformados.csv")

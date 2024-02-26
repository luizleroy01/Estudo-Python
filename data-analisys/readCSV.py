import pandas as pd

def construir_tabela(nome_arquivo):
    # Lê o arquivo CSV e cria um DataFrame
    df = pd.read_csv(nome_arquivo)
    df = df.replace(',',';')
    # Retorna o DataFrame
    return df

# Nome do arquivo CSV
nome_arquivo = 'C:\\Users\\leroy\\OneDrive\\Documentos\\Código\\Input\\Tarefas.csv'

# Constrói a tabela a partir do arquivo CSV
tabela = construir_tabela(nome_arquivo)

# Exibe a tabela
print(tabela)

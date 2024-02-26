import pandas as pd
import tkinter as tk
from tkinter import ttk

def construir_tabela(nome_arquivo):
    # Lê o arquivo CSV e cria um DataFrame
    df = pd.read_csv(nome_arquivo)
    
    # Retorna o DataFrame
    return df

# Função para criar e exibir a janela com os dados
def exibir_janela(tabela):
    # Cria uma janela
    janela = tk.Tk()
    janela.title("Tabela de Dados")

    # Cria um widget Treeview para exibir a tabela
    tree = ttk.Treeview(janela)

    # Configura as colunas do Treeview
    tree["columns"] = tuple(tabela.columns)
    tree["show"] = "headings"
    for column in tree["columns"]:
        tree.heading(column, text=column)

    # Insere os dados na Treeview
    for index, row in tabela.iterrows():
        tree.insert("", "end", values=tuple(row))

    # Adiciona uma barra de rolagem
    scrollbar = ttk.Scrollbar(janela, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Empacota o Treeview
    tree.pack(expand=True, fill="both")

    # Inicia o loop da aplicação
    janela.mainloop()

# Nome do arquivo CSV
nome_arquivo = 'C:\\Users\\leroy\\OneDrive\\Documentos\\Código\\Input\\Tarefas.csv'

# Constrói a tabela a partir do arquivo CSV
tabela = construir_tabela(nome_arquivo)

# Exibe a janela com os dados
exibir_janela(tabela)

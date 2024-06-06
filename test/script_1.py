import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.load_data import load_data
from components.calculate_avg_age import calculate_avg_age
from components.calculate_avg_children import calculate_avg_children
from components.search_name import search_name

def script_1():
    file_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP3/resources/database.csv"
    df = load_data(file_csv)

    print("Parte 1:")
    print("Realize uma consulta por um nome salvo em um dataframe pandas.")
    name = "Ana"
    search_result = search_name(df, name)
    print(search_result)
    print()
    
    print("Parte 2:")
    print("Exiba a média de idade para o dataframe recebido.")
    avg_age = calculate_avg_age(df)
    print(f"Média de idade: {avg_age}")
    print()

    print("Parte 3:")
    print("Exiba a média do número de filhos para o dataframe recebido.")
    avg_children = calculate_avg_children(df)
    print(f"Média do número de filhos: {avg_children}")
    print()

def main():
    script_1()

main()
import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.load_data import load_data

def calculate_avg_children(df):
    return df['num_filhos'].mean()

def main():
    file_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP3/resources/database.csv"

    df = load_data(file_csv)
    print(calculate_avg_children(df))

main()
import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.load_data import load_data
from components.search_id import search_id
from components.search_name import search_name

def save_json_file(file_name, json_object):
    file = f"C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP3/resources/{file_name}.json"
    with open(file, 'w') as file:
        file.write(json_object)

def main():
    file_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP3/resources/database.csv"

    df = load_data(file_csv)
    json_object_id = search_id(df,1,json_flag=True)
    json_object_name = search_name(df,"Ana",json_flag=True)
    save_json_file
    save_json_file("search_id_result", json_object_id)
    save_json_file("search_name_result", json_object_name)
    
main()

import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.load_data import load_data

def search_id(df, id, json_flag=False):
    resultado = df[df['id'] == id]
    if not json_flag:
        return resultado
    else:
        if resultado.empty:
            return pd.Series({}).to_json()
        registro = resultado.iloc[0].to_dict()
        json_result = {
            "id": registro["id"],
            "nome": registro["nome"],
            "idade": registro["idade"],
            "cidade": registro["cidade_nascimento"],
            "estado": registro["estado_nascimento"],
            "escolaridade": registro["escolaridade"],
            "num_filhos": registro["num_filhos"],
            "num_celulares": registro["num_celulares"]
        }
        return pd.Series(json_result).to_json(indent=4)

def main():
    file_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP3/resources/database.csv"

    df = load_data(file_csv)
    print(search_id(df, 1, json_flag=True))
    print(search_id(df, 1, json_flag=False))

main()

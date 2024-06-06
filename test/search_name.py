import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.load_data import load_data

def search_name(df, name, json_flag=False):
    result = df[df['nome'].str.contains(name, case=False, na=False)]
    if not json_flag:
        return result
    else:
        registers = result.reset_index(drop=True)
        register_dict = registers.to_dict(orient='index')
        json_result = {
            "registros_encontrados": len(register_dict),
            "registros": {
                f"registro_{i+1}": {
                    "id": register["id"],
                    "nome": register["nome"],
                    "idade": register["idade"]
                } for i, register in register_dict.items()
            }
        }
        return pd.Series(json_result).to_json(indent=4)


def main():
    file_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP3/resources/database.csv"

    df = load_data(file_csv)
    print(search_name(df, "Ana", json_flag=True))
    print(search_name(df, "Ana", json_flag=False))

main()
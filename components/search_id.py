import pandas as pd

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

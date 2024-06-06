import pandas as pd

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
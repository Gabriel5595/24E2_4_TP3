import pandas as pd

def carregar_base_dados(arquivo_csv):
    return pd.read_csv(arquivo_csv)
from components.load_data import load_data
from components.save_json_file import save_json_file
from components.search_name import search_name

def script_2():
    print("***SCRIPT 2***")
    file_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP3/resources/database.csv"
    df = load_data(file_csv)

    print("Parte 1:")
    print("Realize uma consulta por um nome salvo em um objeto json.")
    name = "Ana"
    search_result = search_name(df, name, json_flag=True)
    print(search_result)
    print()
    
    print("Parte 2:")
    print("Realize o salvamento do objeto json em um arquivo .json.")
    save_json_file("search_result", search_result)
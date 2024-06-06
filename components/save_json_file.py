def save_json_file(file_name, json_object):
    file = f"C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Python para Dados/TPs/TP3/resources/{file_name}.json"
    with open(file, 'w') as file:
        file.write(json_object)

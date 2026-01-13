import os

history_list = []

def save_calculator(expression_string, result_value, file_name):
    clean_expression = " ".join(expression_string.split())
    
    if result_value == int(result_value):
        result_value = int(result_value)
    
    entry = f"{clean_expression} = {result_value}"
    
    write_to_txt(entry, file_name)
    print("Calcul save in history")


def write_to_txt(line, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(line + "\n")

    

def show_history(file_name):
    if os.path.exists(file_name):
        print("HISTORIQUE COMPLET")
        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read())
    else : 
        print("Aucun historique trouvé")
            

history_list = []

def save_calculator(expression_string, result_value):
    entry = f"{expression_string} = {result_value}"
    
    history_list.append(entry)
    
    print("Calcul save in history")
    
def show_history():
    if not history_list:
        print("Aucun calcul en mémoire")
    else : 
        print("--- HISTORIQUE ---")
        for item in history_list:
            print(item)
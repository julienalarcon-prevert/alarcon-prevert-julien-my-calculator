import os, text

history_list = []

def clean_terminal():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def save_calculation(expression_string, result_value, file_name):
    clean_expression = " ".join(expression_string.split())
    
    if result_value == int(result_value):
        result_value = int(result_value)
    
    entry = f"{clean_expression} = {result_value}"
    
    write_to_txt(entry, file_name)
    print(text.messages["save"].center(text.larg))

def write_to_txt(line, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def delete_history(file_path="calculs.txt"):
    try: 
        os.remove(file_path)
        print(text.messages["dlt"].center(text.larg))
    except FileNotFoundError:
        print(f"File '{file_path}' not found")

def show_history(file_name):
    if os.path.exists(file_name):
        print("HISTORY".center(text.larg))
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip().center(text.larg))
    else: 
        print("History not found")
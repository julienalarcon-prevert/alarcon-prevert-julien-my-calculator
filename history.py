import os, text
from datetime import datetime

history_list = []

def clean_terminal():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def save_calculation(expression_string, result_value, file_name):
    clean_expression = " ".join(expression_string.split())
    
    if result_value == int(result_value):
        result_value = int(result_value)
    
    now = datetime.now().strftime("%H:%M")
    
    entry = f"[{text.BLUE}{now}{text.END}] {text.YELLOW}{clean_expression}{text.END} = {text.PURPLE}{result_value}{text.END}"
    
    write_to_txt(entry, file_name)
    print(text.messages["save"].center(text.larg))

def write_to_txt(line, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def delete_history(file_path="calculs.txt"):
    confirm = input(f"{text.RED} Are you sure you want to delete everything ? (y/n): {text.END}").lower()
    
    if confirm == 'y':
        with open(file_path, "w") as file:
            file.write("")
        print(text.messages["dlt"].center(text.larg))
    else : 
        print(f"{text.YELLOW}Deletion cancelled.{text.END}".center(text.larg))

def show_history(file_name):
    if os.path.exists(file_name):
        print("\n" + f"{text.BOLD}{text.BLUE}HISTORY{text.END}".center(text.larg))
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip().center(text.larg + 18))
    else: 
        print("History not found")
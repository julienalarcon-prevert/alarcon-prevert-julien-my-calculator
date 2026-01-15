import engine, history, parser, text

def display_header():
    history.clean_terminal()
    print(text.messages["accueil"].center(text.larg))
    print(text.messages["help"].center(text.larg))
    
def handle_calculation(entry, history_file):
    try: 
        token_list = parser.tokenizer(entry)
        if not token_list:
            print(text.messages["empty"].center(text.larg))
            return
        result = engine.evaluate_expression(token_list)
        
        if result == int(result):
            result = int(result)
        
        clean_expr = " ".join(entry.split())
        print(f"{clean_expr} = {result}")
        history.save_calculation(entry, result, history_file)
        
    except IndexError:
        print("ERROR: Your calculation is incomplete (it ends with an operator)")
    except Exception as error:
        print(f"UNKNOWN ERROR: {error}")            

def main_menu():
    history_file = "calculs.txt"
    display_header()
    
    while True:
        entry = input(">>> ").strip()
        command = entry.lower()

        if command == "quit":
            history.clean_terminal()
            print(text.messages["exit"].center(text.larg))
            break
            
        elif command == "history":
            history.clean_terminal()
            history.show_history(history_file)
            input("\nPress Enter to return to the menu...")
            display_header()
            
        elif command == "delete":
            history.delete_history(history_file)
            display_header()
            
        elif command == "help":
            print(text.messages["help"].center(text.larg))
            
        elif command == "":
            continue
            
        else:
            handle_calculation(entry, history_file)
import engine, history, parser, text

def display_header():
    history.clean_terminal()
    print(text.messages["accueil"].center(text.larg))
    print(text.messages["help"].center(text.larg))
    
def handle_calculation(entry, mon_historique):
    try : 
        list_tokens = parser.tokenizer(entry)
        if not list_tokens:
            print(text.messages["empty"].center(text.larg))
            return
        result = engine.evaluate_expression(list_tokens)
        
        if result == int(result):
            result = int(result)
        
        clean_expr = " ".join(entry.split())
        print(f"{clean_expr} = {result}")
        history.save_calculator(entry, result, mon_historique)
        
    except IndexError:
        print("ERROR: Yous calculation is incomplete (it ends with an operator)")
    except Exception as error:
        print(f"UNKNOWN ERROR : {error}")            

def main_menu():
    mon_historique = "calculs.txt"
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
            history.show_history(mon_historique)
            input("\nAppuyez sur Entrée pour revenir au menu...")
            display_header()
            
        elif command == "delete":
            history.delete_history(mon_historique)
            print("Historique supprimé.")
            display_header()
            
        elif command == "help":
            print(text.messages["help"].center(text.larg))
            
        elif command == "":
            continue
            
        else:
            handle_calculation(entry, mon_historique)
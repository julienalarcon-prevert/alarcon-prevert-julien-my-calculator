import engine, history, parser, text, re

def display_header(last_res=None):
    
    print(text.messages["accueil"].center(text.larg))
    
    if last_res is None:
        status_val = "---"
        res_color = text.PURPLE
    elif last_res > 0:
        status_val = last_res
        res_color = text.GREEN
    elif last_res < 0:
        status_val = last_res
        res_color = text.RED
    else:
        status_val = 0
        res_color = text.PURPLE

    status = f"{text.BLUE}LAST RESULT: {text.BOLD}{res_color}{status_val}{text.END}"
    print(status.center(text.larg + 18))
    
    print(f"{text.YELLOW}Type 'help' for commands{text.END}".center(text.larg))
    
    line = f"{text.BLUE}" + "─" * (text.larg // 2) + f"{text.END}"
    print(line.center(text.larg + 9))

def handle_calculation(entry, history_file):
    try: 
        token_list = parser.tokenizer(entry)
        if not token_list:
            print(text.messages["empty"].center(text.larg))
            return None
            
        result = engine.evaluate_expression(token_list)
        
        if result == int(result):
            result = int(result)
        
        clean_expr = " ".join(entry.split())
        
        print(f"{text.BLUE}───{text.END}".center(text.larg + 9)) 
        print(f"{text.PURPLE}{clean_expr} = {text.BOLD}{result}{text.END}".center(text.larg + 18))
        print(f"{text.BLUE}───{text.END}".center(text.larg + 9))
        
        history.save_calculation(entry, result, history_file)
        return result
        
    except Exception as error:
        print(f"{text.RED}ERROR: {error}{text.END}".center(text.larg))
        return None

def handle_calculation(entry, history_file):
    try: 
        token_list = parser.tokenizer(entry)
        if not token_list:
            print(text.messages["empty"].center(text.larg))
            return None
            
        result = engine.evaluate_expression(token_list)
        
        if result == int(result):
            result = int(result)
        
        clean_expr = " ".join(entry.split())
        print(f"\n  {text.BLUE}───{text.END}") 
        print(f"  {text.PURPLE}{clean_expr} = {text.BOLD}{result}{text.END}")
        print(f"  {text.BLUE}───{text.END}\n")
        
        history.save_calculation(entry, result, history_file)
        
        return result
        
    except Exception as error:
        print(f"{text.RED}ERROR: {error}{text.END}")
        return None

def main_menu():
    history_file = "calculs.txt"
    last_result = None
    display_header(last_result)
    
    while True:
        entry = input(text.messages["entry"]).strip()
        print(text.END, end="")
        
        command = entry.lower()

        if command == "quit":
            history.clean_terminal()
            print(text.messages["exit"].center(text.larg))
            break
        elif command == "history":
            history.clean_terminal()
            history.show_history(history_file)
            input("\nPress Enter to return...")
            history.clean_terminal()
            display_header(last_result)
        elif command == "delete":
            history.delete_history(history_file)
            last_result = None
            display_header(last_result)
        elif command == "":
            continue
        else:
            if "ans" in command:
                entry = command.replace("ans", str(last_result if last_result is not None else 0))
            
            if "v" in entry:
                entry = re.sub(r'v(\d+)', r'0 v \1', entry)
            
            res = handle_calculation(entry, history_file)
            if res is not None:
                last_result = res
                display_header(last_result)
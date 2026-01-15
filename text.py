import shutil

larg = shutil.get_terminal_size().columns

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
END = "\033[0m"
PURPLE = "\033[95m"

def show_detailed_help():
    title = "--- COMMAND GUIDE ---"
    
    col_cmd = 12
    col_act = 30
    table_width = col_cmd + col_act + 3
    
    margin = (larg - table_width) // 2
    pad = " " * margin

    print("\n" + (BOLD + BLUE + title + END).center(larg + 9))
    print(pad + f"{'Command':<{col_cmd}} | {'Action':<{col_act}}")
    print(pad + "-" * table_width)
    
    commands = [
        ("history", "View your past calculations"),
        ("delete", "Clear all history records"),
        ("ans", "Use the last result"),
        ("help", "Show this guide"),
        ("quit", "Shut down the calculator")
    ]
    
    for cmd, act in commands:
        colored_cmd = f"{PURPLE}{cmd}{END}"
        print(f"{pad}{colored_cmd:<{col_cmd + 9}} | {act}")
    
    print(pad + "-" * table_width + "\n")

messages = {
    "accueil": f"{BOLD}{BLUE}--- CALCULATOR ---{END}",
    "exit": f"{RED}Shutting down...{END}",
    "empty": f"{RED}ERROR: EMPTY CALCULATION{END}",
    "save": f"{GREEN}Saved to history{END}",
    "entry": f"{BOLD}{BLUE}calc{END} {GREEN}→{END} {YELLOW}",
    "dlt": f"{RED}History deleted successfully{END}",
}
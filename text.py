import shutil

larg = shutil.get_terminal_size().columns

messages = {
    "accueil": "CALCULATOR",
    "help": "Available commands: 'history', 'quit', 'help', 'delete' or enter a calculation",
    "exit": "Exiting program...",
    "empty": "ERROR: EMPTY OR UNRECOGNIZED CALCULATION",
    "incomplete": "ERROR: Your calculation is incomplete (it ends with an operator)",
    "unk": "UNKNOWN ERROR",
    "save": "Calculation saved to history",
    "dlt": "History deleted successfully",
    "byzero": "Division by zero is not allowed",
    "entry": ">>>"
}
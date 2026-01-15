import shutil

larg = shutil.get_terminal_size().columns

messages = {
    "accueil": "CALCULATOR",
    "help": "Orders available : 'history', 'quit', 'help', 'delete' or your calculation directly",
    "exit": "Exit program",
    "empty": "ERROR: EMPTY OR UNRECOGNIZED CALCULATION",
    "incomplete": "ERROR: Your calculation is incomplete (it ends with an operator)",
    "unk": "ERREUR UNKNOWN",
    "save": "Calcul save in history",
    "dlt": "History deleted succesfull",
    "byzero": "Division by 0 is not allowed",
    "entry": ">>>"
}
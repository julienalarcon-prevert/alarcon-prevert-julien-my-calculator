import text, par

def add (a, b): return float(a) + float(b)

def subtract (a, b): return float(a) - float(b)

def multiply (a, b): return float(a) * float(b)

def divide (a, b):
    if b == 0 : 
        raise ValueError(text.messages["byzero"])
    resultat = float(a) / float(b)
    return resultat

def puissance (a, b): return float(a)**float(b)

def divide_entire(a, b):
    if b == 0: raise ValueError(text.messages["byzero"].center(text.larg))
    return float(round(a / b))

def max_min (a, b):
    if a > b: return float(a)
    if a < b: return float(b)
    
def modulo(a, b):
    if b == 0 : raise ValueError(text.messages["byzero"].center(text.larg))
    return float(a%b)

def calculate_no_parents(tokens):
    apply_ope(tokens, {"^": puissance})
    apply_ope(tokens, {
              "*": multiply,
              "/": divide,
              "%": modulo,
              "!": divide_entire
    })
    apply_ope(tokens, {"+": add, "-":subtract})
    apply_ope(tokens, {
        ">": max_min,
        "<": lambda a, b: float(min(a, b))
    })
    return tokens[0]

def apply_ope(liste_tokens, table_ope):
    i = 0
    while i < len(liste_tokens):
        token = liste_tokens[i]
        if token in table_ope:
            left = liste_tokens[i-1]
            right = liste_tokens[i+1]
            op_function = table_ope[token]
            
            result = op_function(left, right)
            liste_tokens[i-1 : i+2] = [result]
            i=0
        else:
            i+=1
    return liste_tokens

def evaluate_expression(liste_tokens):

    tokens_ready = par.solve_parenthese(list(liste_tokens))
    
    return calculate_no_parents(tokens_ready)

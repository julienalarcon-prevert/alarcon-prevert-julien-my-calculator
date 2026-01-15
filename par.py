import engine

def chek_par(tokens):
    balance = 0
    for token in tokens:
        if token == "(":
            balance += 1
        elif token == ")":
            balance -= 1
        
        if balance < 0:
            raise ValueError("Error: Parenthès fermante sans parenthèse ouvrante")
    if balance != 0:
        raise ValueError("Error : Parenthès ouvrante non fermée")
    return tokens

def solve_parenthese(tokens):
    while"(" in tokens:
        last_open = -1
        for i in range(len(tokens)):
            if tokens[i] == "(":
                last_open = i
        
        first_close = tokens.index(")", last_open)
        sub_expr = tokens[last_open + 1 : first_close]
        sub_result = engine.evaluate_expression(list(sub_expr))
        tokens[last_open : first_close + 1] = [sub_result]
    return tokens
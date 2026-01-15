import engine

def check_parentheses(tokens):
    balance = 0
    for token in tokens:
        if token == "(":
            balance += 1
        elif token == ")":
            balance -= 1
        
        if balance < 0:
            raise ValueError("Error: Closing parenthesis without opening one")
            
    if balance != 0:
        raise ValueError("Error: Opening parenthesis not closed")
    return tokens

def solve_parentheses(tokens):
    from engine import calculate_no_parentheses
    
    while "(" in tokens:
        last_open = -1
        for i in range(len(tokens)):
            if tokens[i] == "(":
                last_open = i
        
        first_close = tokens.index(")", last_open)
        sub_expr = tokens[last_open + 1 : first_close]
        sub_result = calculate_no_parentheses(list(sub_expr))
        tokens[last_open : first_close + 1] = [sub_result]
        
    return tokens
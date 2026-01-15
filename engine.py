import text, par

def add(a, b): return float(a) + float(b)

def subtract(a, b): return float(a) - float(b)

def multiply(a, b): return float(a) * float(b)

def divide(a, b):
    if b == 0: 
        raise ValueError(text.messages["byzero"])
    return float(a) / float(b)

def power(a, b): return float(a)**float(b)

def divide_entire(a, b):
    if b == 0: 
        raise ValueError(text.messages["byzero"].center(text.larg))
    return float(round(a / b))

def get_max(a, b):
    return float(a) if a >= b else float(b)

def modulo(a, b):
    if b == 0: 
        raise ValueError(text.messages["byzero"].center(text.larg))
    return float(a % b)

def calculate_no_parentheses(tokens):
    apply_operation(tokens, {"^": power})
    apply_operation(tokens, {
              "*": multiply,
              "/": divide,
              "%": modulo,
              "!": divide_entire
    })
    apply_operation(tokens, {"+": add, "-": subtract})
    apply_operation(tokens, {
        ">": get_max,
        "<": lambda a, b: float(min(a, b))
    })
    return tokens[0]

def apply_operation(token_list, op_table):
    i = 0
    while i < len(token_list):
        token = token_list[i]
        if token in op_table:
            left = token_list[i-1]
            right = token_list[i+1]
            op_function = op_table[token]
            
            result = op_function(left, right)
            token_list[i-1 : i+2] = [result]
            i = 0
        else:
            i += 1
    return token_list

def evaluate_expression(token_list):
    tokens_ready = par.solve_parentheses(list(token_list))
    return calculate_no_parentheses(tokens_ready)
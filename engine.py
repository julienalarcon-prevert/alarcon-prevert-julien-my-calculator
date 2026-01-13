def add (a, b):
    return float(a) + float(b)

def subtract (a, b):
    return float(a) - float(b)

def multiply (a, b):
    return float(a) * float(b)

def divide (a, b):
    if b == 0 : 
        raise ValueError("Division by zero is not allowed")
    resultat = float(a) / float(b)
    return resultat

def puissance (a, b):
    return float(a)**float(b)

def divide_entire(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return float(round(a / b))

def max_min (a, b):
    if a > b:
        return float(a)
    if a < b:
        return float(b)

def evalutate_expression(liste_tokens):
    while "^" in liste_tokens:
        ind = liste_tokens.index("^")

        lft = liste_tokens[ind-1]
        rgt = liste_tokens[ind+1]
        result = puissance(lft, rgt)
        
        liste_tokens[ind-1 : ind+2] = [result]
        
            
    while "*" in liste_tokens or "/" in liste_tokens or "!" in liste_tokens:
        i = 0
        while i < len(liste_tokens):
            if liste_tokens[i] == "*" or liste_tokens[i] == "/" or liste_tokens[i] == "!":
                number_left = liste_tokens[i - 1]
                number_right = liste_tokens[i + 1]
                operator = liste_tokens[i]
                
                if operator == "*":
                    result = multiply(number_left, number_right)
                elif operator == "/":
                    result = divide(number_left, number_right)
                else :
                    result = divide_entire(number_left, number_right)
                
                liste_tokens[i-1 : i+2] = [result]
                break
            else : 
                i = i + 1
    while "+" in liste_tokens or "-" in liste_tokens:
        index = 0
        while index < len(liste_tokens):
            element = liste_tokens[index]
            
            if element == "+" or element == "-":
                left = liste_tokens[index - 1]
                right = liste_tokens[index + 1]
            
                if element == "+":
                    result = add(left, right)
                else :
                    result = subtract(left, right)
                
                liste_tokens[index-1 : index+2] = [result]
                break
            else:
                index = index + 1
    while "<" in liste_tokens or ">" in liste_tokens:
        j = 0
        while j < len(liste_tokens):
            if liste_tokens[j] == ">":
                res = max_min(liste_tokens[j-1], liste_tokens[j+1])
                liste_tokens[j-1 : j+1] = [res]
                break
            elif liste_tokens[j] == "<":
                res = float(min(liste_tokens[j-1], liste_tokens[j+1]))
                liste_tokens[j-1 : j+2] = [res]
                break
            j += 1
    return liste_tokens[0]
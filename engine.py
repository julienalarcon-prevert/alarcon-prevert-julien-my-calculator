def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0 : 
        raise ValueError("Division by zero is not allowed")
    resultat = a / b
    return resultat

def evalutate_expression(liste_tokens):
    while "*" in liste_tokens or "/" in liste_tokens:
        i = 0
        while i < len(liste_tokens):
            if liste_tokens[i] == "*" or liste_tokens[i] == "/":
                number_left = liste_tokens[i - 1]
                number_right = liste_tokens[i + 1]
                operator = liste_tokens[i]
                
                if operator == "*":
                    result = multiply(number_left, number_right)
                else:
                    result = divide(number_left, number_right)
                
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
    return liste_tokens[0]

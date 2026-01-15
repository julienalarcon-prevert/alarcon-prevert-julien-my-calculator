def tokenizer (input_string):
    input_string = input_string.replace("**", "^")
    input_string = input_string.replace("//", "!")
    input_string = input_string.replace(",", ".")
    supporter_operators = "+-*/^!<>%()"
    token_list = []
    current_number = ""
    
    for char in input_string:
        if char == " ":
            continue
        if char.isdigit() or char == "." :
            current_number += char
        elif char in supporter_operators:
            if current_number:
                number_float = float(current_number)
                token_list.append(number_float)
                current_number = ""
            token_list.append(char)
        else:
            raise ValueError(f"Caractère non suppoté détecté : '{char}'")
        
    if current_number:
        number_float = float(current_number)
        token_list.append(number_float)
    
    return token_list
    
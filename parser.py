def tokenizer(input_string):
    input_string = input_string.replace("**", "^").replace("//", "!").replace(",", ".")
    supported_operators = "+-*/^!<>%()v"
    token_list = []
    current_number = ""
    
    for char in input_string:
        if char == " ":
            continue
        if char.isdigit() or char == ".":
            current_number += char
        elif char in supported_operators:
            if current_number:
                token_list.append(float(current_number))
                current_number = ""
            
            if char == "-" and len(token_list) == 0 or token_list[-1] == "(":
                current_number = "-"
            else :
                token_list.append(char)
        else:
            raise ValueError(f"Unsupported character detected: '{char}'")
        
    if current_number:
        token_list.append(float(current_number))
    
    return token_list
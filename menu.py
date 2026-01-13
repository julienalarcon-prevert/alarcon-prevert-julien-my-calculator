import engine, history, parser
            
def main_menu():
    mon_historique = "mes_calculs.txt"
    print("--- CALCULATRICE INTELLIGENTE ---")
    print("Commandes disponibles : 'history', 'quit', 'help' ou votre calcul directement")
    
    while True:
        saisie = input(">>> ")
        commande = saisie.strip().lower()

        if commande == "quit":
            print("EXIT PROGRAM")
            break
        elif commande == "history":
            history.show_history(mon_historique)
        elif commande == "help":
            print("Commandes disponibles : 'history', 'quit', 'help' ou votre calcul directement")
        elif commande == "":
            continue
        else :
            try : 
                list_tokens = parser.tokenizer(saisie)
                if list_tokens:
                    result = engine.evalutate_expression(list_tokens)
                    clean_expr = " ".join(saisie.split())
                    
                    if result == int(result):
                        result = int(result)
                        
                    print(f"{clean_expr} = {result}")
                    history.save_calculator(saisie, result, mon_historique)
                else : 
                    print("ERROR : CALCUL VIDE OU NON RECONNU")   
            except IndexError :
                print("ERREUR : Ton calcul est incomplet (il finit par un opérateur)")
            except Exception as e:
                print(f"ERREUR INCONNUE : {e}")

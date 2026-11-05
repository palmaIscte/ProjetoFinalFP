import json
try:
    with open("cofre.json", "r") as ficheiro:
        utilizadores = json.load(ficheiro)
except FileNotFoundError:
    utilizadores = {}


contErradas = 0

while True:
    try:
        selecao = int(input("""
========================================
        PYVAULT: COFRE DIGITAL CLI           
======================================== 
--- MENU PRINCIPAL --- 
 1. Registo de Utilizador 
 2. Iniciar Sessão (Login) 
 0. Sair do Programa
-> Escolha uma opção: """))
    except ValueError:
        print("\nOpção inválida! Por favor escreva um número.")
        continue

    if selecao == 1:
        print("\n[ Registo de Utilizador selecionado ]")
        username = input("Digite o seu nome de username: ")
        palavra_passe = input("Digite a sua palavra-passe: ")

        if username in utilizadores:
            print("O username já existe. Por favor, escolha outro.")
        else:
            utilizadores[username] = palavra_passe
            with open("cofre.json", "w") as ficheiro:
                json.dump(utilizadores, ficheiro)
            print("Registo efetuado com sucesso!")

        input("\nPressione ENTER para voltar ao menu principal...")
         
    elif selecao == 2:
        while True:
            print("\n[ Iniciar Sessão (Login) selecionado ]")
            input_username = input("Digite o seu nome de username: ")
            input_palavra_passe = input("Digite a sua palavra-passe: ")
            if input_username in utilizadores and utilizadores[input_username] == input_palavra_passe:
                print("\nLogin efetuado com sucesso!")
                contErradas = 0
                #LOGICA DE NOTAS A SER IMPLEMENTADA 


            else:
                print("\nUsername ou palavra-passe incorretos.")
                contErradas += 1
                if contErradas >= 3:
                    print("\nNúmero máximo de tentativas atingido. Saindo do programa...")
                    break
                try:
                    nova_tentativa = int(input("\nPressione 1 para efetuar nova tentativa ou 0 para sair: "))
                    if nova_tentativa == 0:
                        break
                except ValueError:
                    print("\nOpção inválida! Por favor escreva um número.")
                    continue

    elif selecao == 0:
        print("\nSaindo do programa...")
        break
        
    else:
        print("\nOpção inválida! Tente novamente.")
        
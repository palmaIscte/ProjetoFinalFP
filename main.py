import json

def carregar_json(nome):
    try:
        with open(nome, "r") as ficheiro:
            return json.load(ficheiro)
    except FileNotFoundError:
        return {}

def guardar_json(nome, dados):
    with open(nome, "w") as ficheiro:
        json.dump(dados, ficheiro)

def menu_cofre(input_username, notas):
    while True:   
        try:
            selecao2 = int(input(f"""
    ========================================
           PYVAULT: COFRE DIGITAL CLI
    ========================================
    --- Área autenticada {input_username} ---
    1. Criar Nova Nota Secreta
    2. Listar e Decifrar Notas
    3. Terminar Sessão (Logout)
    ========================================
    -> Escolha uma opção: """))
        except ValueError:
            print("\nOpção inválida! Por favor escreva um número.")
            continue
    
        if selecao2 == 1:
            print("\n--- Criar Nova Nota ---")
            titulo = input("Título da nota: ")
            conteudo = input("Conteúdo da nota: ")
            notas.setdefault(input_username, {})[titulo] = conteudo
            guardar_json("notas.json", notas)
            print("Nota criada e cifrada com sucesso!")
            
            input("\nPressione ENTER para voltar ao menu do cofre...")
    
            
        elif selecao2 == 2:
            print("\n--- As minhas notas ---")
            if notas.get(input_username, {}):
                for titulo, conteudo in notas.get(input_username, {}).items():
                    print(f"Título: {titulo}\nConteúdo: {conteudo}\n")
            else:
                print("Não existem notas secretas.")
            input("\nPressione ENTER para voltar ao menu do cofre...")
    
    
        elif selecao2 == 3:
            print("\nA terminar sessão...")
            return
        
        else:
            (print("\nOpção inválida! Tente novamente."))


utilizadores = carregar_json("cofre.json")
notas = carregar_json("notas.json")
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
        print("\n--- Registo de Utilizador ---")
        username = input("Digite o seu username: ")
        palavra_passe = input("Digite a sua password: ")

        if username in utilizadores:
            print("O username já existe. Por favor, escolha outro.")
        else:
            utilizadores[username] = palavra_passe
            guardar_json("cofre.json", utilizadores)
            print(f"Utilizador {username} registado com sucesso!")
        input("\nPressione ENTER para voltar ao menu principal...")
         
    elif selecao == 2:
        while True:
            print("\n--- Iniciar Sessão ---")
            input_username = input("Username: ")
            input_palavra_passe = input("Password: ")
            if input_username in utilizadores and utilizadores[input_username] == input_palavra_passe:
                print(f"\nBem-vindo, {input_username}!")
                contErradas = 0
                menu_cofre(input_username, notas) 
                break
                

            else:
                print("\nUsername ou palavra-passe incorretos.")
                contErradas += 1
                if contErradas >= 3:
                    print("\nNúmero máximo de tentativas atingido. A voltar ao menu principal...")
                    contErradas = 0
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

import json
with open("cofre.json", "r") as ficheiro:
    utilizadores = json.load(ficheiro)
while True:
    selecao = int(input("""
========================================
        PYVAULT: COFRE DIGITAL CLI           
======================================== 
--- MENU PRINCIPAL --- 
 1. Registo de Utilizador 
 2. Iniciar Sessão (Login) 
 0. Sair do Programa
-> Escolha uma opção: """))

    if selecao == 1:
        print("\n[ Registo de Utilizador selecionado ]")
        
        input("\nPressione ENTER para voltar ao menu principal...")
         
    elif selecao == 2:
        print("\n[ Iniciar Sessão (Login) selecionado ]")
        
        input("\nPressione ENTER para voltar ao menu principal...")

    elif selecao == 0:
        print("\nSaindo do programa...")
        break
        
    else:
        print("\nOpção inválida! Tente novamente.")
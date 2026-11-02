while True:
    # O menu é mostrado sempre que o ciclo recomeça
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
        # Colocas o código de registo aqui
        
        # Este input pausa o programa. Quando o utilizador der ENTER, o ciclo recomeça e mostra o menu.
        input("\nPressione ENTER para voltar ao menu principal...")
         
    elif selecao == 2:
        print("\n[ Iniciar Sessão (Login) selecionado ]")
        # Colocas o código de login aqui
        
        input("\nPressione ENTER para voltar ao menu principal...")

    elif selecao == 0:
        print("\nSaindo do programa...")
        break # O 'break' serve para destruir o loop e acabar o programa imediatamente
        
    else:
        # É sempre boa prática ter um 'else' caso o utilizador digite um número que não existe no menu (ex: 3)
        print("\nOpção inválida! Tente novamente.")
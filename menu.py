import vendas_pizza as vp
def menuPizzaiolo():
    print("_________MENU_________")
    print("1 - Cadastrar pizza")
    print("2 - Vender pizza")
    opcao = input("Qual a opção: ")
    return int(opcao)

def selecionarOpc(opc):
    if opc == 1:
        print("Opção 1")
    elif opc == 2:
        print("Opção 2")
        vp.listar_pizza()
        pz = int(input("Qual a pizza: "))
        vp.vender_pizza(pz)
    else:
        print("Saíndo do programa")


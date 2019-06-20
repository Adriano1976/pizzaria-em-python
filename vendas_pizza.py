import persistencia as per
arquivo = "pizza.pickle"
pizza = per.carregar_dados(arquivo)
def cadastro_pizza(pizzas):
    pizza.append(pizzas)
    per.salvar(pizza, arquivo)

def listar_pizza():
    lista_pizza = per.carregar_dados(arquivo)
    i = 1
    for nome, valor in lista_pizza:
        print(i)
        print(nome)
        print(valor)
        i += 1
def vender_pizza(numero):
    qtd = int(input("Quantas pizzas deseja: "))
    pizzaselect = pizza[numero-1].copy()
    print(pizzaselect)
    total = pizzaselect[1] * qtd
    print("Valor total")
    print(total)

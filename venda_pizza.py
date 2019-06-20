def valor_pizza(valor, quantidade):
    """ Função calcula o desconto no valor da pizza"""
    valor_total = (valor * quantidade)
    if quantidade > 2 and quantidade < 5:
        valor_total *= 0.9
    elif quantidade >=5:
        valor_total *= 0.8
    return valor_total

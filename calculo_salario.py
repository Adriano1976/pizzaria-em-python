import array as arr
import persistencia as per
#Função para calculo de INSS
def calculo_inss(salario_bruto):
    if salario_bruto < 1693.73:
        inss = salario_bruto * 8 /100
    elif salario_bruto >= 1693.73 and salario_bruto < 2822.91:
        inss = salario_bruto * 9 / 100
    elif  salario_bruto > 2822.90 and salario_bruto < 5645.80:
        inss = salario_bruto * 11 / 100
    else:
        inss = 621.03
    return inss

#Função para calculo de imposto de renda retido na fonte
def calculo_irrf(salario_bruto):
    salario = salario_bruto - calculo_inss(salario_bruto)
    if salario >= 1903.99 and salario < 2826.66:
        irrf = (salario - 142.82) * 7.5 / 100
    elif salario >= 2826.66 and salario < 3751.06:
        irrf = (salario - 354.80) * 15 / 100
    elif salario >= 3751.05 and salario < 4664.69:
        irrf = (salario - 636.13) * 22.5 / 100
    elif salario >= 4664.69:
        irrf = (salario - 869.36) * 27.5 / 100
    return irrf
#Função para exibir folha de pagamento
def folha(salario_bruto):
    print("Folha de Pagamento")
    print("Salario Bruto")
    print(salario_bruto)
    print("Descontos")
    print("_______________________")
    print("INSS")
    print(calculo_inss(salario_bruto))
    print("IRRF")
    print(calculo_irrf(salario_bruto))
    print("Total de descontos")
    total = calculo_irrf(salario_bruto) + calculo_inss(salario_bruto)
    print(total)
    salario_liquido = salario_bruto - total
    print("_______________________")
    print("Salario líquido")
    print(salario_liquido)
    print("_______________________")
# Calculo do desconto do vale transporte
def vale_transporte(salario_bruto, vale):
    seis = salario_bruto * 0.06
    if seis < vale:
        return seis
    else:
        return vale

#Salvar folha de pagamento
def salvar_folha(salario_bruto, funcionario):
    filename = funcionario +".txt"
    arquivo = open(filename , "w+")
    arquivo.write("\nSalario Bruto: %f\r\n" % salario_bruto)
    arquivo.write("\n Descontos \n")
    arquivo.write("\n_______________________\n")
    arquivo.write("\nINSS: %f\n" % calculo_inss(salario_bruto))
    arquivo.write("\nIRRF: %f \n" % calculo_irrf(salario_bruto))
    total = calculo_irrf(salario_bruto) + calculo_inss(salario_bruto)
    arquivo.write("\nTotal de descontos: %f \n" % total)
    salario_liquido = salario_bruto - total
    arquivo.write("\n_______________________\n")
    arquivo.write("\nSalario líquido: %f \n" % salario_liquido)
    arquivo.write("\n_______________________\n")
    arquivo.close()
#Salvar folha de pagamento por via persistencia
def salvar_folha_dump(salario_bruto, funcionario):
    total = calculo_irrf(salario_bruto) + calculo_inss(salario_bruto)
    salario_liquido = salario_bruto - total
    a = ['Salario Bruto', salario_bruto, 'Inss', calculo_inss(salario_bruto), 'IRRF', calculo_irrf(salario_bruto), 'Total de desconto', total, 'Salário Liquido', salario_liquido]
    per.salvar(a, "bancodados.pickle")
#Carregar folha de pagamento por via persistencia
def carregar_folha_dump():
    a = per.carregar_dados("bancodados.pickle")
    print(a)









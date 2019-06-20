import pickle
import pandas

def salvar(dados, nomearquivo):
    pickle.dump(dados, open(nomearquivo, "wb"))

def carregar_dados(nomearquivo):
    dados_carregados = pickle.load(open(nomearquivo, "rb"))
    return dados_carregados
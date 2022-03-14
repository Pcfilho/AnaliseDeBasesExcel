import pandas as pd

base_alunos = pd.read_excel(r"Bases/Base de Alunos0.xlsx", engine='openpyxl')
base_dengue = pd.read_excel(r"Bases/Base de Dengue0.xlsx", engine='openpyxl')
base_onibus = pd.read_excel(r"Bases/Base de Onibus0.xlsx", engine='openpyxl')

nomes, ids, nomes_pai, nomes_mae, Token = [], [], [], [], []


for z, i in base_alunos.iterrows():
    for y, j in base_dengue.iterrows():
        if i['TOKEN'] == j['TOKEN']:
            nomes.append(i['nome'])
            ids.append(i['id'])
            nomes_pai.append(i['nome_do_pai'])
            nomes_mae.append(i['nome_da_mae'])
            Token.append(i['TOKEN'])


tabela = {'id':ids, 'nome':nomes, 'pai':nomes_pai, 'mae':nomes_mae, 'Token':Token}
dataframe = pd.DataFrame(tabela)
dataframe.to_excel('resultado.xlsx')

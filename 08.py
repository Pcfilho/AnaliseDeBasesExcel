import pandas as pd

base_alunos = pd.read_excel(r"Bases/Base de Alunos0.xlsx", engine='openpyxl')
base_dengue = pd.read_excel(r"Bases/Base de Dengue0.xlsx", engine='openpyxl')
base_onibus = pd.read_excel(r"Bases/Base de Onibus0.xlsx", engine='openpyxl')

nomes, ids, datas_nascimentos, data_dengue, eliminados = [], [], [], [], []

for z, i in base_dengue.iterrows():
    for y, j in base_onibus.iterrows():
        if i['TOKEN'] == j['TOKEN']:
            eliminados.append(i['TOKEN'])

for z, i in base_dengue.iterrows():
    if i['TOKEN'] not in eliminados:
        nomes.append(i['nome'])
        ids.append(i['id'])
        datas_nascimentos.append((i['data_de_nascimento']))
        data_dengue.append(i['data_da_dengue'])

tabela = {'id': ids, 'nome': nomes, 'data_de_nascimento': datas_nascimentos, 'data_dengue': data_dengue}
dataframe = pd.DataFrame(tabela)
dataframe.to_excel('Relatorios/8relatorio_saude_menos_mobilidade.xlsx')


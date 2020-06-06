import pandas as pd
import csv
def abrindoarquivos():
    #abrimos o arquivo e organizamos ele em uma tabela no panda dataframe
    arquivo = pd.read_csv('curriculos-lattes.csv', encoding='UTF8')
    #excluimos as colunas que não vamos utilizar
    arquivo = arquivo.drop(columns = ['_id', 'data_atualizacao','pos_doutorado','area_pos_doutorado'])
    #aqui trocamos os valores de sim e não para True e false fazendo com que o dataframe ficasse mais facil de trabalhar
    arquivo = arquivo.replace('SIM', True)
    arquivo = arquivo.replace('NAO', False)
    arquivo = arquivo = arquivo.replace('----', '')
    #informações estatisticas sobre o database
    info = [arquivo['nome'].value_counts().count(), arquivo['graduacao'].value_counts(True)*100, arquivo['especializacao'].value_counts(True)*100, arquivo['mestrado'].value_counts(True)*100, arquivo['doutorado'].value_counts(True)*100]

    #aqui eu transformei num array para que eu pudesse colocar mais facilmente dentro do objeto criado
    arquivo = arquivo.reset_index().values
    return arquivo, info

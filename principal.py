from Classes import *
from readingdata import *

def carregar_arquivo():
    arquivo, info = abrindoarquivos()
    arvore = Tree()
    for i in arquivo:
        arvore.add_tree(No(i))
    return arvore, info
def pesquisar(palavra, arvore, area):
    show = 'Nome'.ljust(50)+ 'Graduação'
    array = arvore.pesquisar(palavra, area)
    array.sort()
    for i in array:
        show = show + '\n' + i[0].ljust(50) + i[1]
    if len(array) > 0:
        return show, len(array)
    else:
        return show + 'Não há especializações que atendam ao critério'

def informação(arquivo):
    print('Total de registros ',arquivo[0],
     '\nPorcentagem de registros com graduações: ',round(arquivo[1][True], 2),
    '\nPorcentagem de registros sem graduação: ',round(arquivo[1][False], 2),
     '\nPorcentagem de registros com especialização: ',round(arquivo[2][True], 2),
     '\nPorcentagem de registros sem especialização: ', round(arquivo[2][False], 2),
     '\nPorcentagem de registros com mestrado: ', round(arquivo[3][True], 2),
    '\nPorcentagem de registros sem mestrado: ', round(arquivo[3][False], 2),
    '\nPorcentagem de registros com doutorado: ', round(arquivo[4][True], 2),
    '\nPorcentagem de registros sem doutorado: ', round(arquivo[4][False], 2)

        )    
def sobre():
    print("Aluno: Pablo Fernandes Santos de Aragão Téjo\nMatrícula: 20181370044\nDisciplina: Estrutura de dados")
def show_lista(lista):
    lista.show_lista()
print('Bem vindos ao sistema de pesquisa de graduação.')
while True:
     
    print('''Escolha uma das opções abaixo
             Para carregar o arquivo digite (c)
             Para pesquisar digite (p)
             Para sair digite (s)
             Para estatisticas da base de dados digite (e)
             Sobre (i) ''')
    opcao = input('Digite:\t')
    if opcao == 'c':
        graduacoes, info = carregar_arquivo()
        print('Arquivo carregado com sucesso!')
    elif opcao == 'p':
        try:
            area = input('Digite a área de especialização \nPara especialização(e)\nPara mestrado digite (m)\nPara doutorado (d)\nPara graduação digite qualquer coisa\nEscolha:')
            chave = input('Digite a área de pesquisa:').lower()
            assert chave.replace(' ', '').isalpha()
            print('Aguarde...')
            busca = pesquisar(chave, graduacoes, area)
            print(busca[0],'\nQuantidade de resultados encontrado: ', busca[1] )
        except NameError:
            print('Carregue o arquivo primeiro!')
        except AssertionError:
            print('Valor inválido para área de pesquisa informe apenas caracteres sem números letras ou caracteres especiais.')
    elif opcao == 'e':
        try:
            informação(info)
        except:
            print('Carregue o arquivo antes.')
    elif opcao == 'i':
        sobre()
    elif opcao == 's':
        print('Adeus')
        break
    else:
        print('Digite uma opção valida!')






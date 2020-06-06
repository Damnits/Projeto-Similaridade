from Algoritmos import *


class Dados:

    #Classe de organização dos dados na tabela panda
    def __init__(self, nome, graduacao, area_graduacao, especializacao, area_especializacao, mestrado, area_mestrado, doutorado, area_doutorado):
        self.__nome = nome
        self.__graduacao = graduacao
        self.__area_graduacao = area_graduacao
        self.__especializacao = especializacao
        self.__area_especializacao =  area_especializacao 
        self.__mestrado = mestrado
        self.__area_mestrado = area_mestrado 
        self.__doutorado = doutorado
        self.__area_doutorado = area_doutorado 
        #GETTERS
    def get_nome(self):
        return self.__nome

    def get_graduacao(self):
        return self.__graduacao

    def get_area_graduacao(self):
        return self.__area_graduacao

    def get_especializacao(self):
        return self.__especializacao

    def get_area_especializacao(self):
        return self.__area_especializacao

    def get_mestrado(self):
        return self.__mestrado

    def get_area_mestrado(self):
        return self.__area_mestrado

    def get_doutorado(self):
        return self.__doutorado

    def get_area_doutorado(self):
        return self.__area_doutorado

    
class No:
    def __init__(self, array):
        self.__dado = Dados(array[1],array[2],array[3],array[4], array[5], array[6], array[7], array[8], array[9])
        self.__next = None
        self.__left = None
        self.__right = None
    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_left(self, no):
        self.__left = no
    def set_right(self, no):
        self.__right = no
    def get_next(self):
        return self.__next
    def set_next(self, node):
        self.__next = node
    def get_nome(self):
        return self.__dado.get_nome()

    def get_graduacao(self):
        return self.__dado.get_graduacao()

    def get_area_graduacao(self):
        return self.__dado.get_area_graduacao()

    def get_especializacao(self):
        return self.__dado.get_especializacao()

    def get_area_especializacao(self):
        return self.__dado.get_area_especializacao()

    def get_mestrado(self):
        return self.__dado.get_mestrado()

    def get_area_mestrado(self):
        return self.__dado.get_area_mestrado()

    def get_doutorado(self):
        return self.__dado.get_doutorado()

    def get_area_doutorado(self):
        return self.__dado.get_area_doutorado()

class Tree:
    def __init__(self):
        
        self.__raiz = None
    def add_tree(self, no):
        if self.__raiz == None:
            self.__raiz = no
        else:
            self._add_tree(no, self.__raiz)
    def _add_tree(self, novo, no):
        if novo.get_nome() > no.get_nome():
            if no.get_right() != None:
                self._add_tree(novo, no.get_right())
            else:
                no.set_right(novo)
        else:
            if no.get_left() != None:
                self._add_tree(novo, no.get_left())
            else:
                no.set_left(novo)
    def pesquisar(self, key, area):
        array = []
        if area == 'm':
            self._pesquisar_mestrado(self.__raiz, key, array)
        elif area == 'e':
            self._pesquisar_especializacao(self.__raiz, key, array)
        elif area == 'd':
            self._pesquisar_doutorado(self.__raiz, key, array)
        else:
            self._pesquisar_graduacao(self.__raiz, key, array)
        return array
    def _pesquisar_graduacao(self, node, key, array):
        if node != None:
            if node.get_graduacao()==True:
                if valueLevensh(key, node.get_area_graduacao())==True:
                    array.append([node.get_nome(), show_pretty(node.get_area_graduacao())])
            self._pesquisar_graduacao(node.get_left(), key, array)
            self._pesquisar_graduacao(node.get_right(), key, array)
    def _pesquisar_mestrado(self, node, key, array):
        if node != None:
            if node.get_mestrado()==True:            
                if valueLevensh(key, node.get_area_mestrado())==True:
                    array.append([node.get_nome(), show_pretty(node.get_area_mestrado())])
            self._pesquisar_mestrado(node.get_left(), key, array)
            self._pesquisar_mestrado(node.get_right(), key, array)
    def _pesquisar_especializacao(self, node, key, array):
        if node != None:
            if node.get_especializacao()==True:
                if valueLevensh(key, node.get_area_especializacao())==True:
                    array.append([node.get_nome(), show_pretty(node.get_area_especializacao())])
            self._pesquisar_especializacao(node.get_left(), key, array)
            self._pesquisar_especializacao(node.get_right(), key, array)
    def _pesquisar_doutorado(self, node, key, array):
        if node != None:
            if node.get_doutorado()==True:
                if valueLevensh(key, node.get_area_doutorado())==True:
                    array.append([node.get_nome(), show_pretty(node.get_area_doutorado())])
            self._pesquisar_doutorado(node.get_left(), key, array)
            self._pesquisar_doutorado(node.get_right(), key, array)

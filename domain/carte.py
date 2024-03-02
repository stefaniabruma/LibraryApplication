'''
Created on 12 nov. 2022

@author: stefa
'''
class carte(object):
    '''
    Tip de data pentru carte
    Domain: id_crt este idul cartii, titlu_crt este titlul cartii, desc_crt este descrierea crtii, autor_crt este autorul cartii
    '''
    
    def __init__(self, id_crt, titlu_crt, desc_crt, autor_crt):
        '''
        Creeaza o noua instanta de carte
        '''
        self.__id_crt = id_crt
        self.__titlu_crt = titlu_crt
        self.__desc_crt = desc_crt
        self.__autor_crt = autor_crt

    def __str__(self):
        '''
        returneaza felul in care va arata cartea la momentul apelarii functiei print
        '''
        
        return f"{self.__id_crt},{self.__titlu_crt},{self.__desc_crt},{self.__autor_crt}"
    
    def __eq__(self, __obj):
        '''
        verifica daca id-ul obiectului carte este egal cu idul altui obiect de tip carte
        '''
        return self.__id_crt == __obj.__id_crt
    
    def getIdCrt(self):
        '''
        Getter method
        returneaza id-ul string al cartii
        '''
        return self.__id_crt
    def getTitluCrt(self):
        '''
        getter method
        returneaza titlul string al cartii
        '''
        return self.__titlu_crt
    def getDescCrt(self):
        '''
        getter method
        returneaza  descrierea string al cartii
        '''
        return self.__desc_crt
    def getAutorCrt(self):
        '''
        getter method
        returneaza autorul string al cartii
        '''
        return self.__autor_crt


        
        

    
        









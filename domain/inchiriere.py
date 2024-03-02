'''
Created on 3 dec. 2022

@author: stefa
'''

class inchiriere(object):
    '''
    tip de date pentru inchiriere
    domain: id_clt - id-ul clientului care inchiriaza; id_clt - id-ul cartii inchiriate
    '''
    
    def __init__(self, client, carte):
        '''
        initializeaza o noua instanta de inchiriere
        '''
        self.__client = client
        self.__carte = carte
    
    
    def getCltInc(self):
        '''
        returneaza clientul care inchiriaza cartea
        '''
        return self.__client
    
    def getCrtInc(self):
        '''
        returneaza cartea inchiriata
        '''
        return self.__carte
    
    def __str__(self):
        '''
        rescrie functia str() pentru tipul de data inchiriere
        '''
        return f'{str(self.__client)}:{str(self.__carte)}'

    def __eq__(self, __o):
        '''
        rescrie functia = pentru inchirieri
        '''
        
        return self.__carte == __o.__carte and self.__client == __o.__client

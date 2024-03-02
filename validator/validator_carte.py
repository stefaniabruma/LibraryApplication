'''
Created on 21 nov. 2022

@author: stefa
'''


class validator_crt(object):
    '''
    tip de data pentru validatorul de carti
    Domain: carte - cu id unic, titlu, descriere si autor
    '''
    def __init__(self, carte):
        self.__crtDeVerificat = carte
    
    def valideaza_crt(self):
        '''
        verifica daca datele unei carti care urmeaza sa fie creata sunt valide
        stringurile id_crt, titlu, desc si autor trebuie sa fie nevide
        '''
        
        errors = ''
        if self.__crtDeVerificat.getIdCrt() == '': 
            errors+= 'Id invalid!\n'
        if self.__crtDeVerificat.getTitluCrt() == '':
            errors += 'Titlu invalid!\n'
        if self.__crtDeVerificat.getDescCrt() == '':
            errors += 'Descriere invalida!\n'
        if self.__crtDeVerificat.getAutorCrt() == '':
            errors += 'Autor invalid!\n'
        if len(errors) > 0:
            raise ValueError(errors)
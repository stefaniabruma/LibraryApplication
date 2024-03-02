'''
Created on 21 nov. 2022

@author: stefa
'''


class validator_clt(object):
    '''
    tip de data pentru validatorul de clienti
    Domain: cltDeVerificat este clientul care se doreste a fi verificat
    '''
    
    def __init__(self, client):
        self.__cltDeVerificat = client
        
    def valideaza_clt(self):
        '''
        verifica daca datele unui client care urmeaza sa fie introdus sunt valide
        id-ul trebuie sa fie nevid
        numele trebuie sa fie nevid
        cnp-ul trebuie sa fie nevid si sa contina doar cifre
        '''
        errors = ''
        
        if self.__cltDeVerificat.getIdClt() == '':
            errors += 'Id invalid!\n'
        
        if self.__cltDeVerificat.getNumeClt() == '':
            errors += 'Nume invalid!\n'
        
        if self.__cltDeVerificat.getCnpClt() == '':
            errors += 'CNP invalid!\n'
        else:
            for i in self.__cltDeVerificat.getCnpClt():
                if not(i >= '0' and i <= '9'):
                    errors += 'CNP invalid!\n'
                    break
        
        if len(errors) > 0:
            raise ValueError(errors)
'''
Created on 21 nov. 2022

@author: stefa
'''
from carte import carte
from validator.validator_carte import validator_crt

class repo_crt(object):
    '''
    Tip de data pentru lista de carti
    Domain: carti
    '''
    def __init__(self, carti):
        '''
        intializeaza repository ul de carti
        carti -  lista de carti
        '''
        self._carti = carti
    
    def __str__(self):
        '''
        felul in care va arata repo_crt la apelarea functiei print
        '''
        rtrn = ""
        for i in self.getAll().keys():
            rtrn += f"{self._carti[i].__str__()}\n"
        rtrn += "\n"
        return rtrn
    
    def verificaIDcrt(self, crt):
        '''
        verifica daca nu cumva o carte ce se afla deja in memorie are acelasi id cu o carte crt care se doreste a fi adaugata
        daca da, arunca exceptie
        '''
        for i in self.getAll().keys():
            if self.getAll()[i].__eq__(crt):
                raise ValueError("Id existent!\n")
        
    def getAll(self):
        '''
        returneaza toate cartile
        '''
        return self._carti
    
    def adauga_carte(self, crt):
        '''
        adauga o carte in lista de carti
        '''
        self.getAll()[crt.getIdCrt()] = crt
        
    def lungimeListaCarti(self):
        '''
        returneaza lungimea listei de carti
        '''
        return len(self._carti)
    
    def stergeCrtDupaID(self, id_crt):
        '''
        sterge din repo cartea cu idul id_crt
        '''
        if not(id_crt in self.getAll().keys()):
            raise ValueError("Nu exista nicio carte cu acest id!\n")
        
        
        del self.getAll()[id_crt]
    
    def modificaCrtDupaID(self, id_crt, titlu_nou, desc_nou, autor_nou):
        '''
        modifica cartea cu id-ul id_crt la noile valori: titlu_nou, desc_nou, autor_nou
        '''
        
        if not(id_crt in self.getAll().keys()):
            raise ValueError("Nu exista nicio carte cu acest id!\n")
        
        crtn = carte(id_crt, titlu_nou, desc_nou, autor_nou)
        
        vldtr = validator_crt(crtn)
        try:
            vldtr.valideaza_crt()
        except ValueError as ve:
            raise ve
        
        self.getAll()[id_crt] = crtn
        
    def cautaCrtDupaID(self, id_crt):
        '''
        cauta cartea cu id-ul id_crt in repository
        returneaza cartea cu id-ul id_crt
        '''
        if not(id_crt in self.getAll().keys()):
            raise ValueError("Nu exista nicio carte cu acest id!\n")
        
        return self.getAll()[id_crt]
    
    
    
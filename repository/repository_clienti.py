'''
Created on 21 nov. 2022

@author: stefa
'''
from client import client
from validator.validator_client import validator_clt

class repo_clt(object):
    
    '''
    tip de data pentru lista de clienti
    Domain: clienti - lista de clienti
    '''
    
    def __init__(self, clienti):
        '''
        initializeaza repository-ul de clienti
        '''
        self._clienti = clienti
    
    def __str__(self):
        '''
        returneaza felul in care va arata repository ul de clientii la momentul apelarii functiei print
        '''
        rtrn = ""
        for i in self.getAll().keys():
            rtrn += f"{self._clienti[i].__str__()}\n"

        rtrn += '\n'
        return rtrn
    
    def verificaIDclt(self, clt):
        '''
        verifica daca nu cumva in lista de clienti se afla deja un client cu idul egal cu idul clientului care urmeaza sa fie adaugat clt
        daca da, arunca exceptie
        '''
        self.verificaIDcltREC(clt, list(self._clienti.values()))
        
        '''for i in self.getAll().keys():
            if self.getAll()[i].__eqid__(clt):
                raise ValueError("Id existent!\n")'''
    
    def verificaIDcltREC(self, clt, listaclienti):
        '''
        verifica daca un client din lista are id-ul egal cu id-ul clientului clt
        daca da, arunca exceptie
        '''
        if listaclienti == []:
            return
        if listaclienti[0].getIdClt() == clt.getIdClt():
            raise ValueError('Id existent!\n')
        self.verificaIDcltREC(clt, listaclienti[1:])
    
    def verificaCNPclt(self, clt):
        '''
        verifica daca nu cumva in lista de clienti se afla deja un client cu cnpul egal cu cnpul clientului care urmeaza sa fie adaugat clt
        daca da, arunca exceptie
        '''
        for i in self.getAll().keys():
            if self.getAll()[i].__eqcnp__(clt):
                raise ValueError("CNP existent!\n")
            
    def getAll(self):
        '''
        returneaza toti clientii:
        '''
        return self._clienti
    
    def adauga_client(self, clt):
        '''
        adauga un nou client in repository
        '''
        self.getAll()[clt.getIdClt()] = clt
    
    def lungimeListaClienti(self):
        '''
        returneaza lungimea repository ului de clienti
        '''
        
        return len(self._clienti)
    
    def stergeCltDupaID(self, id_clt):
        '''
        sterge din repo-ul de clienti clientul cu id-ul id_clt
        '''
        if not(id_clt in self.getAll().keys()):
            raise ValueError("Nu exista niciun client cu acest id!\n")
        del self.getAll()[id_clt]
        
    def modificaCltDupaID(self, id_clt, nume_nou, cnp_nou):
        '''
        modifica clientul cu idul id_clt la noile valori: nume_nou, cnp_nou
        '''
        
        if not(id_clt in self.getAll().keys()):
            raise ValueError("Nu exista niciun client cu acest id!\n")
        
        cltn = client(id_clt, nume_nou, cnp_nou)
        vldtr = validator_clt(cltn)
        try:
            vldtr.valideaza_clt()
        except ValueError as ve:
            raise ve
        
        self.getAll()[id_clt] = cltn
    
    def cautaCltDupaID(self, id_clt):
        '''
        cauta clientul cu id-ul id_clt in repository
        returneaza clientul cu id-ul egal cu stringul id_clt
        '''
        
        if not(id_clt in self.getAll().keys()):
            raise ValueError("Nu exista niciun client cu acest id!\n")
        
        return self.getAll()[id_clt]
        
    
   
    
    
    
    
    
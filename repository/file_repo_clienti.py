'''
Created on 5 dec. 2022

@author: stefa
'''
from repository.repository_clienti import repo_clt
from client import client

class file_repo_clt(repo_clt):
    '''
    tip de data epntru repository-ul de clienti cu fisiere
    '''
    
    def __init__(self, clienti, cale):
        '''
        initializeaza o noua instanta de repository clienti cu fisiere
        '''
        repo_clt.__init__(self, clienti)
        self.__cale = cale
    
    def __readAll(self):
        '''
        citeste toti clientii din fisier
        '''
        with open(self.__cale, "r") as f:
            lines = f.readlines()
            self._clienti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_clt = parts[0]
                    nume_clt = parts[1]
                    cnp_clt = parts[2]
                    clt = client(id_clt, nume_clt, cnp_clt)
                    self._clienti[id_clt] = clt
                    
    def __writeAll(self):
        '''
        scrie toti clientii in fisier
        '''
        with open(self.__cale, "w") as f:
            for clt in self._clienti:
                f.write(str(self._clienti[clt]) + "\n")
    
    def __appendToFile(self, clt):
        '''
        scrie un client la finalul fisierului
        '''
        with open(self.__cale, "a") as f:
            f.write(str(clt) + "\n")
    
    def __str__(self):
        self.__readAll()
        return repo_clt.__str__(self)
    
    def verificaIDclt(self, clt):
        self.__readAll()
        repo_clt.verificaIDclt(self, clt)
    
    def verificaCNPclt(self, clt):
        self.__readAll()
        repo_clt.verificaCNPclt(self, clt)
    
    def getAll(self):
        self.__readAll()
        return repo_clt.getAll(self)
    
    def adauga_client(self, clt):
        self.__readAll()
        repo_clt.adauga_client(self, clt)
        self.__appendToFile(clt)
    
    def lungimeListaClienti(self):
        self.__readAll()
        return repo_clt.lungimeListaClienti(self)
    
    def stergeCltDupaID(self, id_clt):
        self.__readAll()
        repo_clt.stergeCltDupaID(self, id_clt)
        self.__writeAll()
    
    def modificaCltDupaID(self, id_clt, nume_nou, cnp_nou):
        self.__readAll()
        repo_clt.modificaCltDupaID(self, id_clt, nume_nou, cnp_nou)
        self.__writeAll()
    
    def cautaCltDupaID(self, id_clt):
        self.__readAll()
        return repo_clt.cautaCltDupaID(self, id_clt)
    
    
        
'''
Created on 5 dec. 2022

@author: stefa
'''
from repository.repository_inchirieri import repo_inc
from inchiriere import inchiriere
from client import client
from carte import carte


class file_repo_inc(repo_inc):
    '''
    tip de data pentru repository-ul de inchirieri
    '''
    
    def __init__(self, incs, cale):
        '''
        initializeaza o noua instanta de repository de inchirieri cu fisiere
        '''
        repo_inc.__init__(self, incs)
        self.__cale = cale
        
    
    def __readAll(self):
        '''
        scrie inchirierile din fisier in lista
        '''
        with open(self.__cale, "r") as f:
            lines = f.readlines()
            self._incs.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(":")
                    cltprts = parts[0].split(",")
                    clt = client(cltprts[0], cltprts[1], cltprts[2])
                    crtprts = parts[1].split(",")
                    crt = carte(crtprts[0], crtprts[1], crtprts[2], crtprts[3])
                    
                    inc = inchiriere(clt, crt)
                    self._incs.append(inc)
    
    def __writeAll(self):
        '''
        scrie inchirierile din lista in fisier
        '''
        
        with open(self.__cale, "w") as f:
            for inc in self._incs:
                f.write(str(inc) + "\n")
    
    def __str__(self):
        '''
        rescrie functia str() pentru tipul de data file_repo_inc
        '''
        
        return repo_inc.__str__(self)
    
    def adaugaInc(self, inc):
        '''
        adauga o inhchiriere noua in lista de inchirieri
        '''
        
        self.__readAll()
        repo_inc.adaugaInc(self, inc)
        self.__writeAll()
    
    def lungime(self):
        '''
        returneaza lungimea listei de inchirieri
        '''
        self.__readAll()
        return repo_inc.lungime(self)
    
    def stergeInc(self, inc):
        self.__readAll()
        repo_inc.stergeInc(self, inc)
        self.__writeAll()
    
    def verificaExistenta(self, inc):
        self.__readAll()
        repo_inc.verificaExistenta(self, inc)
        self.__writeAll()
    
    def getAll(self):
        self.__readAll()
        return repo_inc.getAll(self)    
        
        
        
                    
'''
Created on 4 dec. 2022

@author: stefa
'''
from repository.repository_carti import repo_crt
from carte import carte

class file_repo_crt(repo_crt):
    '''
    tip de data pentru repo-ul de carti in fisiere
    '''
    def __init__(self, carti, cale):
        '''
        intializeaza o noua instanta de repository cu fisiere pentru carti
        '''
        repo_crt.__init__(self, carti)
        self.__cale = cale
        
    def __readAll(self):
        '''
        citeste toate cartile din fisier
        '''

        with open(self.__cale, "r") as f:
            lines = f.readlines()
            self._carti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_crt = parts[0]
                    nume_crt= parts[1]
                    desc_crt = parts[2]
                    titlu_crt = parts[3]
                    crt = carte(id_crt, nume_crt, desc_crt, titlu_crt)
                    self._carti[id_crt] = crt            
    
    def __writeAll(self):
        '''
        scrie toate cartile in fisier
        '''
        with open(self.__cale, "w") as f:
            for crt in self._carti:
                f.write(str(self._carti[crt])+"\n")
                
    def __appendToFile(self, crt):
        '''
        scrie o carte in fisier
        '''
        
        with open(self.__cale, "a") as f:
            f.write(str(crt) + "\n")
    
    def adauga_carte(self, crt):
        '''
        adauga o carte in repo
        '''
        self.__readAll()
        repo_crt.adauga_carte(self, crt)
        self.__appendToFile(crt)
        
    def modificaCrtDupaID(self, id_crt, titlu_nou, desc_nou, autor_nou):
        '''
        modifica o carte din fisier
        '''
        
        self.__readAll()
        repo_crt.modificaCrtDupaID(self, id_crt, titlu_nou, desc_nou, autor_nou)
        self.__writeAll()
    
    def stergeCrtDupaID(self, id_crt):
        '''
        sterge cartea cu id ul id_crt din fisier
        '''
        
        self.__readAll()
        repo_crt.stergeCrtDupaID(self, id_crt)
        self.__writeAll()
    
    def getAll(self):
        '''
        returneaza toate cartile din fisier
        '''
        
        self.__readAll()
        return repo_crt.getAll(self)
    
    def lungimeListaCarti(self):
        '''
        returneaza lungimea listei de carti
        '''
        self.__readAll()
        return repo_crt.lungimeListaCarti(self)
    
    def cautaCrtDupaID(self, id_crt):
        '''
        returneaza cartea cu id-ul id_Crt
        '''
        self.__readAll()
        return repo_crt.cautaCrtDupaID(self, id_crt)
    
    def verificaIDcrt(self, crt):
        '''
        verifica daca nu cumva o carte ce se afla deja in memorie are acelasi id cu o carte crt care se doreste a fi adaugata
        '''
        self.__readAll()
        repo_crt.verificaIDcrt(self, crt)
    
    def __str__(self):
        self.__readAll()
        return repo_crt.__str__(self)
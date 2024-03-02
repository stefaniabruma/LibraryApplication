'''
Created on 21 nov. 2022

@author: stefa
'''
from client import client
from validator.validator_client import validator_clt
from repository.repository_clienti import repo_clt
import random
from repository.file_repo_clienti import file_repo_clt

    
class client_controller():
    '''
    tip de data pentru controller clienti
    '''
    
    def __init__(self, clienti, dec, cale):
        '''
        intializeaza controllerul de clienti
        '''
        if dec == 2:
            self.__clt_cntrl = repo_clt(clienti)
        else:
            self.__clt_cntrl = file_repo_clt(clienti, cale)
        self.generator = genereazaClt(clienti, dec, cale)
    
    def __str__(self):
        '''
        returneaza felul in care controllerul va arata la apelul functiei print
        '''
        return f"{self.__clt_cntrl}"
    
    def cmd2(self):
        '''
        functia care se apeleaza atunci cand clientul introduce valoarea 2 in consola
        afiseaza lista de clienti
        '''
        return self.__clt_cntrl.getAll()
    
    def cmd4(self, id_clt, nume_clt, cnp_clt):
        '''
        functia care se apeleaza atunci cand clientul introduce valoarea 4 in consola
        adauga un client in lista de clienti
        '''
        
        clt = client(id_clt, nume_clt, cnp_clt)
        
        vldtr = validator_clt(clt)
        
        vldtr.valideaza_clt()
    
        errors = ''
        try:
            self.__clt_cntrl.verificaIDclt(clt)
        except ValueError as ve:
            errors += str(ve)
        
        try:
            self.__clt_cntrl.verificaCNPclt(clt)
        except ValueError as ve:
            errors += str(ve)
            
        if len(errors) > 0:
            raise ValueError(errors)
        
        
        self.__clt_cntrl.adauga_client(clt)
        
    
    def cmd8(self, id_clt, nume_nou, cnp_nou):
        '''
        functia care se apeleaza cand utilizatorul introduce in consola comanda 8
        modifica clientul cu un anumit id
        '''
        
        self.__clt_cntrl.modificaCltDupaID(id_clt, nume_nou, cnp_nou)
        
    
    def cmd10(self, id_clt):
        '''
        functia care se apeleaza atunci cand utilizatorul introduce in consola comanda 10
        afiseaza clientul cu un anumit id
        '''
        cltc = self.__clt_cntrl.cautaCltDupaID(id_clt)
        return cltc
        
    def cmd12(self, nr_gen):
        '''
        genereaza nr_gen entitati de tip client
        '''
        self.generator.genreazaRandomClt(nr_gen)
            
        
class genereazaClt():
    '''
    clasa pentru generarea aleatoare de clienti
    '''
    def __init__(self, clienti, dec, cale):
        '''
        intializeaza generatorul de clienti
        '''
        if dec == 2:
            self.genClt = repo_clt(clienti)
        else:
            self.genClt = file_repo_clt(clienti, cale)
        
    def genreazaRandomClt(self, nr_gen):
        '''
        populeaza repo-ul de clienti cu nr_gen entitati client
        '''
        
        if nr_gen<1:
            raise ValueError("Valoare invalida!\n")
        
        lnume = ['Bradu Lucretia', 'Baciu Radu', 'Vranciu Alexia', 'Asaftei Stefan', 'Taranu Robert', 'Soptica Tamara', 'Popescu Alexandra', 'Sas Mircea', 'Codreanu Cosmin']
        
        cnt = 1
        
        while cnt<=nr_gen:
            ok = 0
            while ok == 0:
                ok = 1
                id_clt = random.randint(100,9999)
                nume_clt = random.choice(lnume)
                i = 1
                cnp_clt = ''
                while i<13:
                    cif = random.randint(0,9)
                    cnp_clt += str(cif)
                    i += 1
                clt = client(id_clt, nume_clt, cnp_clt)
                
                
                try:
                    self.genClt.verificaIDclt(clt)
                except ValueError:
                    ok = 0
                try:
                    self.genClt.verificaCNPclt(clt)
                except ValueError:
                    ok = 0
            self.genClt.adauga_client(clt)
            cnt += 1
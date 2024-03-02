'''
Created on 21 nov. 2022

@author: stefa
'''
from carte import carte
from repository.repository_carti import repo_crt
from validator.validator_carte import validator_crt
import random
from repository.file_repo_carti import file_repo_crt

class carte_controller():
    '''
    tip de data controller de carti
    '''
    
    def __init__(self, carti, dec, cale):
        '''
        initializeaza cotnrollerul de carti
        '''
        if dec == 2:
            self.__crt_cntrl = repo_crt(carti)
        else:
            self.__crt_cntrl = file_repo_crt(carti, cale)
        self.generator = genereazaCrt(carti, dec, cale)
    
    def __str__(self):
        '''
        returneaza modul in care va fi afisat controllerul la apelul functiei print
        '''
        return f"{self.__crt_cntrl}"   
    
    def cmd1(self):
        '''
        functia ce este apelata daca utilizatorul introduce in consola comanda 1
        afiseaza lista de carti
        '''
        
        return self.__crt_cntrl.getAll()
    
    def cmd3(self, id_crt, titlu, desc, autor):
        '''
        functia ce este apelata daca utilizatorul introduce in consola comanda 2
        adauga o carte in repo
        '''
        crt = carte(id_crt, titlu, desc, autor)
        vldtr = validator_crt(crt)
        
        
        vldtr.valideaza_crt()
        self.__crt_cntrl.verificaIDcrt(crt)
        
        self.__crt_cntrl.adauga_carte(crt)
    
    
    def cmd7(self, id_crt, titlu_nou, desc_nou, autor_nou):
        '''
        functia care este apelata daca utilizatorul introduce in consola comanda 7
        modifica cartea cu un anumit id
        '''
        self.__crt_cntrl.modificaCrtDupaID(id_crt, titlu_nou, desc_nou, autor_nou)
        
    def cmd9(self, id_crt):
        '''
        functia care este apelata atunci cand utilizatorul introduce in consola comanda 9
        afiseaza cartea cu un anumit id
        '''
        
        crtc = self.__crt_cntrl.cautaCrtDupaID(id_crt)
        
        return crtc
    
    def cmd11(self, nr_gen):
        '''
        genereaza nr_gen clienti
        '''
        self.generator.genereazaRandomCrt(nr_gen)
        

class genereazaCrt():
    '''
    clasa pentru generarea aleatoare de carti
    '''
    def __init__(self, carti, dec, cale):
        '''
        intializeaza generatorul de carti
        '''
        if dec == 2:
            self.genCrt = repo_crt(carti)
        else:
            self.genCrt = file_repo_crt(carti, cale)
    
    def genereazaRandomCrt(self, nr_gen):
        '''
        populeaza repo-ul de carti cu nr_gen entitati carte
        '''
        if nr_gen < 1:
            raise ValueError("Valoare invalida!\n")
        
        cnt = 1
        
        ltitluri = ['Ion', 'Amintiri din copilarie', 'Enigma Otiliei', 'Harry Potter', 'Un barbat pe nume Ove', 'Ugly Love', 'Moara cu Noroc']
        lautori = ['Liviu Rebreanu', 'Ion Creanga', 'George Calinescu', 'JK Rowlling', 'Fredrick Backman', 'Coleen Hoover', 'Ioan Slavici']
        ldescrieri = ['O carte despre un taran', ' O carte despre copilarie', 'O carte despre un tanar', 'O carte despre magie', 'O carte despre un batran', 'O carte despre iubire', 'O carte despre ispita banului'] 
        
        while cnt<=nr_gen:
            ok = 0
            while ok == 0:
                id_clt = random.randint(100,9999)
                titlu_crt = random.choice(ltitluri)
                desc_crt = random.choice(ldescrieri)
                autor_crt = random.choice(lautori)
                crt = carte(id_clt, titlu_crt, desc_crt, autor_crt)
                
                
                ok = 1
                try:
                    self.genCrt.verificaIDcrt(crt)
                except ValueError:
                    ok = 0
                    
            self.genCrt.adauga_carte(crt)
            cnt += 1
        
        
        
        
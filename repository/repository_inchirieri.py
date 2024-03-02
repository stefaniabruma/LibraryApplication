'''
Created on 3 dec. 2022

@author: stefa
'''



class repo_inc(object):
    '''
    tip de data pentru lista de inchirieri
    domain: incs = lista de carti
    '''
    
    def __init__(self, incs):
        '''
        intializeaza o noua instanta de lista de inchirieri
        '''
        self._incs = incs
    
    def adaugaInc(self, inc):
        '''
        adauga o noua inchiriere in lista de inchirieri
        '''
        self._incs.append(inc)
    
    def lungime(self):
        '''
        returneaza numarul de inchirieri inregistrate
        '''
        return len(self._incs)
    
    def stergeInc(self, inc):
        '''
        sterge o inchiriere din lista
        '''
        if inc not in self._incs:
            raise ValueError("Clientul nu are aceasta carte inchiriata!\n")
        self._incs.remove(inc)   
    
    def __str__(self):
        '''
        rescrie functia str() pentru tipul de data repo_inc
        '''
        sir = ""
        for inc in self._incs:
            sir += str(inc) + "\n"
        
        return sir
    
    def verificaExistenta(self, inc):
        '''
        verifica daca o carte este deja inchiriata
        '''
        for inchiere in self._incs:
            if inchiere.getCrtInc() == inc.getCrtInc():
                raise ValueError("Carte deja inchiriata!\n")
    
    def getAll(self):
        '''
        returneaza toate inchirierile
        '''
        
        return self._incs   

class client(object):
    '''
    tip de data pentru client
    domain: id_clt este idul clientului, nume_clt este numele clientului, cnp_clt este cnpul clientului
    '''
    
    
    def __init__(self, id_clt, nume_clt, cnp_clt):
        '''
        initializeaza o noua instanta de client
        '''
        
        self.__id_clt = id_clt
        self.__nume_clt = nume_clt
        self.__cnp_clt = cnp_clt
    
    def __eqid__(self, __o):
        ''''
        verifica daca idul obiectului client este egal cu idul altui obiect de acelasi tip
        '''
        
        return self.__id_clt == __o.__id_clt
    
    def __eqcnp__(self, __o):
        '''
        verifica daca cnpul obiectului client este egal cu cnpul altui obiect de acelasi tip
        '''
        return self.__cnp_clt == __o.__cnp_clt
    
    def __str__(self):
        '''
        returneaza felul in care obiectul client va arata la apelul functiei print
        '''
        
        return f"{self.__id_clt},{self.__nume_clt},{self.__cnp_clt}"
    
    def __eq__(self, __o):
        return self.__id_clt == __o.__id_clt

    def getIdClt(self):
        '''
        returneaza idul string al clientului
        '''
        return self.__id_clt
    
    def getNumeClt(self):
        '''
        returneaza numele string al clientului
        '''
        return self.__nume_clt
    
    def getCnpClt(self):
        '''
        returneaza cnp-ul string al clientului
        '''
        return self.__cnp_clt
    
    def getIncClt(self):
        '''
        returneaza numarul de inchirieri ale clientului
        '''
        return self.__inchirieri     


        
        


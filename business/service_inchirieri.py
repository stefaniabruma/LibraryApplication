'''
Created on 3 dec. 2022

@author: stefa
'''
from repository.repository_carti import repo_crt
from repository.repository_clienti import repo_clt
from repository.repository_inchirieri import repo_inc
from inchiriere import inchiriere
from repository.file_repo_carti import file_repo_crt
from repository.file_repo_clienti import file_repo_clt
from repository.file_repo_inchirieri import file_repo_inc



class inc_controller():
    '''
    tip de data pentru controller inchirieri
    '''
    
    def __init__(self, carti, clienti, inchirieri, dec, cale1, cale2, cale3):
        if dec == 2:
            self.__cntrlcrt = repo_crt(carti)
            self.__cntrlclt = repo_clt(clienti)
            self.__cntrlinc = repo_inc(inchirieri)
        else:
            self.__cntrlcrt = file_repo_crt(carti, cale1)
            self.__cntrlclt = file_repo_clt(clienti, cale2)
            self.__cntrlinc = file_repo_inc(inchirieri, cale3)
        
            
        self.__cntrlserv = serviceInc(carti, clienti, inchirieri, dec, cale1, cale2, cale3)
    
    def cmd5(self, id_crt):
        '''
        functia ce este apelata daca utilizatorul introduce in consola comanda 5
        sterge cartea cu un anumit id
        '''
        
        try:
            self.__cntrlserv.stergeIncAnumitaCrt(id_crt)
        except ValueError:
            pass
    
        self.__cntrlcrt.stergeCrtDupaID(id_crt)
    
    def cmd6(self, id_clt):
        '''
        functia care se apeleaza cand utilizatorul introduce in consola comanda 6
        sterge clientul cu un anumit id
        '''
        
        try:
            self.__cntrlserv.stergeIncAnumitClient(id_clt)
        except ValueError:
            pass
        
        self.__cntrlclt.stergeCltDupaID(id_clt)
        
    def cmd13(self, id_clt, id_crt):
        '''
        functia ce se apeleaza cand utilizatorul introduce valoarea 13
        inchiriaza carte
        '''
        errors = ''
        try:
            clt = self.__cntrlclt.cautaCltDupaID(id_clt)
        except ValueError as ve:
            errors += str(ve)
        try:
            crt = self.__cntrlcrt.cautaCrtDupaID(id_crt)
        except ValueError as ve:
                errors += str(ve)
        
        if len(errors) > 0:
            raise ValueError(errors)
        
        inc = inchiriere(clt, crt)
        
        self.__cntrlinc.verificaExistenta(inc)
        self.__cntrlinc.adaugaInc(inc)
        
        self.__cntrlserv.incrementareIncCarte(crt)
        self.__cntrlserv.incrementareIncClient(clt)
    
    def cmd14(self):
        '''
        functia ce se apeleaza atunci cand utilizatorul introduce valoarea 14
        afiseaza inchirierile
        '''
        return self.__cntrlinc.getAll()
    
    def cmd15(self, id_clt, id_crt):
        '''
        functia ce este apelata atunci cand utilizatorul introduce valoarea 15
        returneaza carte
        '''
        
        errors = ''
        try:
            clt = self.__cntrlclt.cautaCltDupaID(id_clt)
        except ValueError as ve:
            errors += str(ve)
        try:
            crt = self.__cntrlcrt.cautaCrtDupaID(id_crt)
        except ValueError as ve:
                errors += str(ve)
        
        if len(errors) > 0:
            raise ValueError(errors)
        
        inc = inchiriere(clt, crt)
        
        self.__cntrlinc.stergeInc(inc)
        
    
    def cmd16(self):
        '''
        functia care este apelata atunci cand utiliziatorul introduce valoarea 16
        afiseaza cele mai inchiriate carti
        '''
        return self.__cntrlserv.mostRented()
    
    def cmd17(self):
        '''
        functia care este apelata atunci cand utilizatorul introduce valoarea 17
        afiseaza primii 20% cei mai activi clienti
        '''
        
        
        lista = self.__cntrlserv.mostActive()
        
        nr = self.__cntrlclt.lungimeListaClienti()
        nr = nr // 5
        
        listanoua = {}
        contor = 0 
        for clt in lista:
            numeClt = clt.getNumeClt()
            inchirieri = self.__cntrlserv.getNrIncClient(clt)
            listanoua[numeClt] = inchirieri
            contor += 1
            if contor == nr:
                return listanoua
            
    def cmd18(self):
        '''
        functia care este apelata atunci cand utilizatorul introduce valoarea 18
        afiseaza clientii cu carti inchiriate ordonati dupa nume
        '''
        return self.__cntrlserv.ordDupaNume()
    
    def cmd19(self):
        '''
        functia care este apelata atunci cand utilizatorul introduce valoarea 19
        afiseaza clientii care au carti inchiriate dupa numarul de carti inchiriate
        '''
        
        return self.__cntrlserv.ordDupaNrCrt()
        
    
    def cmd20(self, c):
        '''
        functia care este apelata atunci cand utilizatorul introduce valoarea 20
        afiseaza clientii care au inchiriat o carte care incepe cu o litera introdusa de utilizator
        '''
        return self.__cntrlserv.clientiCartiAnumitaLitera(c)
    
    def cmd21(self):
        '''
        functia care este apelata cand utilizatorul introduce valoarea 21
        returneaza clientii cu carti inchiriate ordonati dupa numarul de carti inchiriate, apoi dupa nume
        '''
        return self.__cntrlserv.ordDupaNrCrtSINume()
    
class serviceInc():
    '''
    tip de data pentru service ul de inchirieri
    '''
    def __init__(self, carti, clienti, inchirieri, dec, cale1, cale2, cale3):
        '''
        intializeaza o noua instanta de service de inchirieri
        '''
        if dec == 2:
            self.__carti = repo_crt(carti)
            self.__clienti = repo_clt(clienti)
            self.__inc = repo_inc(inchirieri)
        else:
            self.__carti = file_repo_crt(carti, cale1)
            self.__clienti = file_repo_clt(clienti, cale2)
            self.__inc = file_repo_inc(inchirieri, cale3)
        
        self.__clientiPlusNumar = {}
        self.__cartiPlusNumar = {}
    
    def mergeSort(self, lista, start, end, key = None, reversed = False, cmp = None):
        '''
        sorteaza elementele unei liste
        l - lista de elemente
        returneaza lista sortata
        '''
        if start >= end:
            return
        m = (end+start) // 2
        self.mergeSort(lista, start, m, key = key, reversed = reversed, cmp = cmp)
        self.mergeSort(lista, m+1, end, key = key, reversed = reversed, cmp = cmp)
        self.merge(lista, start, end, m, key = key, reversed = reversed, cmp = cmp)
    
    def merge(self, lista, start, end, m, key = None, reversed = False, cmp = None):
        '''
        interclasarea a doua secvente
        '''
        stanga = start
        dreapta = m+1
        linterclasata = []
        while stanga<=m and dreapta<=end:
            if reversed == False:
                if cmp:
                    if cmp(lista[stanga], lista[dreapta]) < 0:
                        linterclasata.append(lista[stanga])
                        stanga += 1
                    else:
                        linterclasata.append(lista[dreapta])
                        dreapta += 1
                elif key:
                    if key(lista[stanga]) < key(lista[dreapta]):
                        linterclasata.append(lista[stanga])
                        stanga += 1
                    else:
                        linterclasata.append(lista[dreapta])
                        dreapta += 1
                else:
                    if lista[stanga] < lista[dreapta]:
                        linterclasata.append(lista[stanga])
                        stanga += 1
                    else: 
                        linterclasata.append(lista[dreapta])
                        dreapta += 1
            else:
                if cmp:
                    if cmp(lista[stanga], lista[dreapta]) > 0:
                        linterclasata.append(lista[stanga])
                        stanga += 1
                    else:
                        linterclasata.append(lista[dreapta])
                        dreapta += 1
                elif key:
                    if key(lista[stanga]) > key(lista[dreapta]):
                        linterclasata.append(lista[stanga])
                        stanga += 1
                    else:
                        linterclasata.append(lista[dreapta])
                        dreapta += 1
                else:
                    if lista[stanga] > lista[dreapta]:
                        linterclasata.append(lista[stanga])
                        stanga += 1
                    else: 
                        linterclasata.append(lista[dreapta])
                        dreapta += 1
        
        while stanga<=m:
            linterclasata.append(lista[stanga])
            stanga += 1
        
        while dreapta<=end:
            linterclasata.append(lista[dreapta])
            dreapta += 1
        
        for i in range(len(linterclasata)):
            lista[start+i] = linterclasata[i]
    
    def maxMin(self, lista, key = None, reversed = False, cmp = None):
        '''
        returneaza cel mai mic si cel mai mare element al unei liste
        '''
        minn = lista[0]
        maxx = lista[0]
        if reversed == False:
            for element in lista:
                if cmp:
                    if cmp(element, minn) < 0:
                        minn = element
                    if cmp(element, maxx) > 0:
                        maxx = element
                elif key:
                    if key(element) < key(minn):
                        minn = element
                    if key(element) > key(maxx):
                        maxx = element
                else:
                    if element < minn:
                        minn = element
                    if element > maxx:
                        maxx = element
        else:
            for element in lista:
                if cmp:
                    if cmp(element, minn) > 0:
                        minn = element
                    if cmp(element, maxx) < 0:
                        maxx = element
                elif key:
                    if key(element) > key(minn):
                        minn = element
                    if key(element) < key(maxx):
                        maxx = element
                else:
                    if element > minn:
                        minn = element
                    if element < maxx:
                        maxx = element
            
        listaNoua = [minn, maxx]
        return listaNoua
               
    def bingoSort(self, lista, key = None, reversed = False, cmp = None):
        '''
        sorteaza elementele unei liste
        '''
        lungime = len(lista)
        
        minsimax = self.maxMin(lista, key = key, reversed=reversed, cmp=cmp)
        bingo = minsimax[0]
        nextBingo = minsimax[1]
        celmaimare = nextBingo
        pozurmelem = 0
        if reversed == False:
            if cmp:
                while cmp(bingo, nextBingo) < 0:
                    pozstart = pozurmelem
                    for i in range(pozstart, lungime):
                        if cmp(lista[i], bingo) == 0:
                            lista[i], lista[pozurmelem] = lista[pozurmelem], lista[i]
                            pozurmelem += 1
                        elif cmp(lista[i], nextBingo) < 0:
                            nextBingo = lista[i]
                    bingo = nextBingo
                    nextBingo = celmaimare
            elif key:
                while bingo < nextBingo:
                    pozstart = pozurmelem
                    for i in range(pozstart, lungime):
                        if lista[i] == bingo:
                            lista[i], lista[pozurmelem] = lista[pozurmelem], lista[i]
                            pozurmelem += 1
                        elif lista[i] < nextBingo:
                            nextBingo = lista[i]
                    bingo = nextBingo   
                    nextBingo = celmaimare    
            else:    
                while bingo < nextBingo:
                    pozstart = pozurmelem
                    for i in range(pozstart, lungime):
                        if lista[i] == bingo:
                            lista[i], lista[pozurmelem] = lista[pozurmelem], lista[i]
                            pozurmelem += 1
                        elif lista[i] < nextBingo:
                            nextBingo = lista[i]
                    bingo = nextBingo
                    nextBingo = celmaimare
        else:
            if cmp:
                while cmp(bingo, nextBingo) > 0:
                    pozstart = pozurmelem
                    for i in range(pozstart, lungime):
                        if cmp(lista[i], bingo) == 0:
                            lista[i], lista[pozurmelem] = lista[pozurmelem], lista[i]
                            pozurmelem += 1
                        elif cmp(lista[i], nextBingo) > 0:
                            nextBingo = lista[i]
                    bingo = nextBingo
                    nextBingo = celmaimare
            elif key:
                while bingo > nextBingo:
                    pozstart = pozurmelem
                    for i in range(pozstart, lungime):
                        if lista[i] == bingo:
                            lista[i], lista[pozurmelem] = lista[pozurmelem], lista[i]
                            pozurmelem += 1
                        elif lista[i] > nextBingo:
                            nextBingo = lista[i]
                    bingo = nextBingo   
                    nextBingo = celmaimare    
            else:    
                while bingo > nextBingo:
                    pozstart = pozurmelem
                    for i in range(pozstart, lungime):
                        if lista[i] == bingo:
                            lista[i], lista[pozurmelem] = lista[pozurmelem], lista[i]
                            pozurmelem += 1
                        elif lista[i] > nextBingo:
                            nextBingo = lista[i]
                    bingo = nextBingo
                    nextBingo = celmaimare
                      
    def stergeIncAnumitaCrt(self, id_crt):
        '''
        sterge inchirierile din repo-ul de inchirieri care contin cartea cu id-ul id_crt
        '''
        crt = self.__carti.cautaCrtDupaID(id_crt)
        for i in self.__inc.getAll():
            if i.getCrtInc() == crt:
                self.__inc.stergeInc(i)
    
    def stergeIncAnumitClient(self, id_clt):
        '''
        sterge inchirierile din repo=ul de inchirieri care contin clientrul cu id-ul id_clt
        '''
        clt = self.__clienti.cautaCltDupaID(id_clt)
        for i in self.__inc.getAll():
            if i.getCltInc() == clt:
                self.__inc.stergeInc(i)
    
    def mostRented(self):
        '''
        returneaza lista de carti sortata dupa numarul de inchirieri
        '''
     
        listaValori = []
        listaCarti = []
        
        if self.__cartiPlusNumar == {}:
            return []
        for valoare in self.__cartiPlusNumar.values():
            if valoare not in listaValori:
                listaValori.append(valoare)
        
        self.mergeSort(listaValori, 0, len(listaValori) -1, reversed = True)
        
        for valoare in listaValori:
            for id_crt in self.__cartiPlusNumar.keys():
                if self.__cartiPlusNumar[id_crt] == valoare:
                    listaCarti.append(self.__carti.cautaCrtDupaID(id_crt))
        
        return listaCarti
                
    def mostActive(self):
        '''
        returneaza lista de clienti sortata dupa numarul de inchirieri
        '''
        
        listaValori = []
        listaClienti = []
        
        if self.__clientiPlusNumar == {}:
            return []
        
        for valoare in self.__clientiPlusNumar.values():
            if valoare not in listaValori:
                listaValori.append(valoare)
        
        self.bingoSort(listaValori, reversed=True)
        
        for valoare in listaValori:
            for id_clt in self.__clientiPlusNumar.keys():
                if self.__clientiPlusNumar[id_clt] == valoare:
                    listaClienti.append(self.__clienti.cautaCltDupaID(id_clt))
        
        return listaClienti
        
        
    def getNrIncClient(self, clt):
        '''
        returneaza numarul de inchirieri al unui client
        '''
        return self.__clientiPlusNumar[clt.getIdClt()]
    
    def ordDupaNume(self):
        '''
        returneaza lista de clienti cu carti inchiriate ordonati dupa nume
        '''
        
        listaNume= []
        listaClienti = []
        
        if self.__inc.getAll() == []:
            return []
        for inch in self.__inc.getAll():
            clt = inch.getCltInc()
            nume_clt = clt.getNumeClt()
            if nume_clt not in listaNume:
                listaNume.append(nume_clt)
        
        self.mergeSort(listaNume, 0, len(listaNume)-1)
        for nume in listaNume:
            for inch in self.__inc.getAll():
                clt = inch.getCltInc()
                numeClt = clt.getNumeClt()
                if numeClt == nume:
                    listaClienti.append(clt)
        
        return listaClienti
    
    def ordDupaNrCrt(self):
        '''
        returneaza lista de clienti cu carti inchiriate ordonati dupa numarul de carti inchiriate
        '''
        
        dic = {}
        listaValori = []
        listaClienti = []
        
        if self.__inc.getAll() == []:
            return []
        
        for inch in self.__inc.getAll():
            clt = inch.getCltInc()
            if clt.getIdClt() not in dic.keys():
                dic[clt.getIdClt()] = 1
            else:
                dic[clt.getIdClt()] += 1
            
        for numar in dic.values():
            if numar not in listaValori:
                listaValori.append(numar)
        
        self.bingoSort(listaValori, reversed=True)
        
        for valoare in listaValori:
            for id_clt in dic:
                if dic[id_clt] == valoare:
                    listaClienti.append(self.__clienti.cautaCltDupaID(id_clt))
        
        return listaClienti  
        
    def ordDupaNrCrtSINume(self):
        '''
        ordoneaza lista de clienti cu carti inchiriate dupa numarul de carti inchiriate, iar daca acesta este egal, dupa nume
        '''
        
        listaClienti = []
        dic = {}
        if self.__inc.getAll() == []:
            return []
        
        for inch in  self.__inc.getAll():
            clt =  inch.getCltInc()
            if clt not in listaClienti:
                listaClienti.append(clt)
            if clt.getIdClt() not in dic.keys():
                dic[clt.getIdClt()] = 1
            else:
                dic[clt.getIdClt()] += 1
        
        listaClienti.sort(key = lambda x:(dic[x.getIdClt()], x.getNumeClt()), reverse = True)
        return listaClienti      
    
    def clientiCartiAnumitaLitera(self, c):
        '''
        returneaza lista de clienti care au inchiriat o carte care incepe cu litera c
        '''
        if not(c.isalpha()):
            raise ValueError("Valoare invalida!\n")
        listaClienti = []

        for inch in self.__inc.getAll():
            crt = inch.getCrtInc()
            clt  =inch.getCltInc()
            if crt.getTitluCrt()[0] == c:
                listaClienti.append(clt)
        
        if listaClienti == []:
            raise ValueError("Nu exista clienti care sa indeplineasca cerinta!\n")
        
        return listaClienti
    
    
    def incrementareIncClient(self, clt):
        '''
        incrementeaza numarul de inchirieri al unui client dat clt
        '''
        id_clt = clt.getIdClt()
        
        if id_clt not in self.__clientiPlusNumar.keys():
            self.__clientiPlusNumar[id_clt] = 1
        else:
            self.__clientiPlusNumar[id_clt] += 1
    
        
    def incrementareIncCarte(self, crt):
        '''
        incrementeaza numarul de inchirieri al unei carti date crt
        '''
        id_crt = crt.getIdCrt()
        
        if id_crt not in self.__cartiPlusNumar.keys():
            self.__cartiPlusNumar[id_crt] = 1
        else:
            self.__cartiPlusNumar[id_crt] += 1        


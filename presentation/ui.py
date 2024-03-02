
class userInterface(object):
    def run(self, executacrt, executaclt, executainc):
        self.print_menu()
        cmd = self.getComanda()
        self.execute(executacrt, executaclt, executainc, cmd)
        self.run(executacrt, executaclt, executainc)
    
    def printDecision(self):
        '''
        printeaza optiunile de a lucra cu sau fara fisiere
        '''
        print("Cum doriti sa ruleze aplicatia?")
        print("1 - cu fisiere")
        print("2 - fara fisiere")
        
    def print_menu(self):
        print("Comenzi")
        print("1 - Afiseaza toate cartile")
        print("2 - Afiseaza toti clientii")
        print("3 - Adauga carte")
        print("4 - Adauga client")
        print("5 - Sterge carte dupa ID")
        print("6 - Sterge client dupa ID")
        print("7 - Modifica carte dupa ID")
        print("8 - Modifica client dupa ID")
        print("9 - Cauta carte dupa ID")
        print("10 - Cauta client dupa ID")
        print("11 - Populeaza lista de carti cu x entitati")
        print("12 - Populeaza lista de clienti cu x entitati")
        print("13 - Inchiriaza carte")
        print("14 - Afiseaza inchirierile (sub forma id client:id carte)")
        print("15 - Returneaza carte")
        print("16 - Raport: cele mai inchiriate carti")
        print("17 - Raport: primii 20% cei mai activi clienti")
        print("18 - Raport: clientii cu carti inchiriate ordonati dupa nume")
        print("19 - Raport: clientii cu carti inchiriate ordonati dupa numarul de carti inchiriate")
        print("20 - Raport: clientii care au inchiriat o carte a carui titlu incepe cu o anumita litera")
        print("21 - Raport: clienti cu carti inchiriate ordonati dupa numarul de carti inchiriate, nume")
        
    def getComanda(self):
        print("Introduceti comanda:")
        cmd  = int(input())
        return cmd
    
    def getDecizie(self):
        dec = int(input())
        return dec
    
    def execute(self, executacrt, executaclt, executainc, cmd):
        if cmd == 1:
            print("Cartile sunt:")
            rezultat = executacrt.cmd1()
            for carte in rezultat.values():
                print(carte)
            
        if cmd == 2:
            print("Clientii sunt:")
            rezultat = executaclt.cmd2()
            for client in rezultat.values():
                print(client)
            
        if cmd == 3:
            id_crt = input("Introduceti id_ul cartii:")
            titlu = input("Intoduceti titlul cartii:")
            desc = input("Introduceti descrierea cartii:")
            autor = input("Introduceti autorul cartii:")
            try:
                executacrt.cmd3(id_crt, titlu, desc, autor)
            except ValueError as ve:
                print(ve)
                return
            print("Carte adaugata cu succes!")
            
        if cmd == 4:
            id_clt = input("Introduceti id-ul clientului:")
            nume_clt = input("Introduceti numele clientului:")
            cnp_clt = input("Introduceti cnp-ul clientului:")
            try:
                executaclt.cmd4(id_clt, nume_clt, cnp_clt)
            except ValueError as ve:
                print(ve)
                return
            print("Client adaugat cu succes!")
            
        if cmd == 5:
            id_crt = input("Introduceti id-ul cartii pe care doriti sa o stergeti:")
            try:
                executainc.cmd5(id_crt)
            except ValueError as ve:
                print(ve)
                return
            print("Carte stearsa!")
            
        if cmd == 6:
            id_clt = input("Introduceti id-ul clientului pe care doriti sa il stergeti:")
            try:
                executainc.cmd6(id_clt)
            except ValueError as ve:
                print(ve)
                return
            print("Client sters!\n")
            
        if cmd == 7:
            id_crt = input("Introduceti id-ul cartii pe care doriti sa o modificati:")
            titlu_nou = input("Noul titlu este:")
            desc_nou = input("Noua descriere este:")
            autor_nou = input("Noul autor este:")
            try:
                executacrt.cmd7(id_crt, titlu_nou, desc_nou, autor_nou)
            except ValueError as ve:
                print(ve)
                return
            print("Carte modificata!")
            
        if cmd == 8:
            id_clt = input("Introduceti di-ul clientului pe care doriti sa il modificati:")
            nume_nou = input("Noul nume este: ")
            cnp_nou= input("Noul cnp este: ")
            try:
                executaclt.cmd8(id_clt, nume_nou, cnp_nou)
            except ValueError as ve:
                print(ve)
                return
            print("Client modificat!")
            
        if cmd == 9:
            id_crt = input("Introduceti id-ul cartii cautate: ")
            try:
                rezultat = executacrt.cmd9(id_crt)
            except ValueError as ve:
                print(ve)
                return
            print(rezultat)
            
        if cmd == 10:
            id_clt = input("Introduceti id-ul clientului cautat: ")
            try:
                rezultat = executaclt.cmd10(id_clt)
            except ValueError as ve:
                print(ve)
                return
            print(rezultat)
            
        if cmd == 11:
            nr_gen = int(input("Introduceti numarul de carti aleatoare pe care vreti sa le introduceti: "))
            try:
                executacrt.cmd11(nr_gen)
            except ValueError as ve:
                print(ve)
                return
            
        if cmd == 12:
            nr_gen = int(input("Introduceti numarul de clienti aleatorii pe care vreti sa ii introduceti: "))
            try:
                executaclt.cmd12(nr_gen)
            except ValueError as ve:
                print(ve)
                return
            
        if cmd == 13:
            id_clt = input("Introducet id-ul clientului: ")
            id_crt = input("Introdcueti id-ul cartii inchiriate: ")
            try:
                executainc.cmd13(id_clt, id_crt)
            except ValueError as ve:
                print(ve)
                return
            print("Carte inchiriata cu succes!")
            
        if cmd == 14:
            inchirieri = executainc.cmd14()
            for inc in inchirieri:
                print(inc.getCltInc().getIdClt() + ":" + inc.getCrtInc().getIdCrt())
            
        if cmd == 15:
            id_clt = input("Introduceti id-ul clientului care doreste sa returneze: ")
            id_crt = input("Introduceti id-ul cartii pe care clientul doreste sa o returneze: ")
            try:
                executainc.cmd15(id_clt, id_crt)
            except ValueError as ve:
                print(ve)
                return
            print("Carte returnata cu succes!\n")
            
        if cmd == 16:
            print("Cele mai inchiriate carti sunt:")
            carti = executainc.cmd16()
            for carte in carti:
                print(carte, "\n")
            
        if cmd == 17:
            print("Primii 20% cei mai activi clienti sunt:")
            clienti = executainc.cmd17()
            for client in clienti:
                print(client, ": ", clienti[client], " carti inchiriate")
                
        if cmd == 18:
            print("Clientii cu carti inchiriate ordonati dupa nume sunt:")
            clienti = executainc.cmd18()
            for client in clienti:
                print(client, "\n")
            
        if cmd == 19:
            print("Clientii cu carti inchiriate sortati dupa numarul de carti inchiriate sunt:")
            clienti = executainc.cmd19()
            for client in clienti:
                print(client, "\n")
            
        if cmd == 20:
            c = input("Introduceti litera cu care doriti sa inceapa titlul cartii: ")
            try:
                clienti = executainc.cmd20(c)
            except ValueError as ve:
                print(ve)
                return
            print("Clientii care au inchiriata o carte a carui titlu incepe cu litera introdusa sunt:")
            for client in clienti:
                print(client, "\n")
        
        if cmd == 21:
            print("Clientii cu carti inchiriate sortati dupa numarul de carti inchiriate, nume sunt:")
            clienti = executainc.cmd21()
            for client in clienti:
                print(client, "\n")
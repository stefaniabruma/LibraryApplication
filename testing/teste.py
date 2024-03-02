'''
Created on 12 nov. 2022

@author: stefa
'''
from carte import carte
from repository.repository_carti import repo_crt
from validator.validator_carte import validator_crt
from client import client
from repository.repository_clienti import repo_clt
from validator.validator_client import validator_clt
from business.service_carti import genereazaCrt
from business.service_clienti import genereazaClt
from inchiriere import inchiriere
from repository.repository_inchirieri import repo_inc
from business.service_inchirieri import serviceInc
from repository.file_repo_carti import file_repo_crt
from repository.file_repo_clienti import file_repo_clt
from repository.file_repo_inchirieri import file_repo_inc



class ruleaza_teste:
    def test_creare_carte(self):
        id_crt = '123'
        titlu_crt = 'Ion'
        desc_crt = 'O carte despre un taran'
        autor_crt = 'Liviu Rebreanu'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        assert crt.getIdCrt() == '123'
        assert crt.getTitluCrt() == 'Ion'
        assert crt.getDescCrt() == 'O carte despre un taran'
        assert crt.getAutorCrt() == 'Liviu Rebreanu'

    def test_repo_crt(self):
        id_crt = '123'
        titlu_crt = 'Ion'
        desc_crt = 'O carte despre un taran'
        autor_crt = 'Liviu Rebreanu'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        

        carti = {}
        lcarti = repo_crt(carti)
        assert lcarti.lungimeListaCarti() == 0
        
        try:
            lcarti.verificaIDcrt(crt)
            assert True
        except ValueError:
            assert False
        
        lcarti.adauga_carte(crt)
        assert lcarti.lungimeListaCarti() == 1
        
        id_crt = '123'
        titlu_crt = 'Harry Potter si piatra filosofala'
        desc_crt = 'volumul 1'
        autor_crt = 'JK Rowlling'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        try:
            lcarti.verificaIDcrt(crt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Id existent!\n"
            
        id_crt = '213'
        
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        lcarti.adauga_carte(crt)
        assert lcarti.__str__() == "123,Ion,O carte despre un taran,Liviu Rebreanu\n213,Harry Potter si piatra filosofala,volumul 1,JK Rowlling\n\n"
        assert lcarti.lungimeListaCarti() == 2
        
        id_crt = '123'
        lcarti.stergeCrtDupaID(id_crt)
        assert lcarti.__str__() == "213,Harry Potter si piatra filosofala,volumul 1,JK Rowlling\n\n"
        assert lcarti.lungimeListaCarti() == 1
        
        id_crt = '2421'
        try:
            lcarti.stergeCrtDupaID(id_crt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista nicio carte cu acest id!\n"
        
        id_crt = '213'
        titlu_nou = 'Ugly Love'
        desc_noua = 'O carte despre iubire'
        autor_nou = 'Coleen Hoover'
        
        try:
            lcarti.modificaCrtDupaID(id_crt, titlu_nou, desc_noua, autor_nou)
            assert True
        except ValueError as ve:
            assert False
        
        assert lcarti.__str__() == "213,Ugly Love,O carte despre iubire,Coleen Hoover\n\n"
        
        id_crt = '213'
        titlu_nou = ''
        desc_noua = ''
        autor_nou = ''
        
        try:
            lcarti.modificaCrtDupaID(id_crt, titlu_nou, desc_noua, autor_nou)
            assert False
        except ValueError as ve:
            assert str(ve) == "Titlu invalid!\nDescriere invalida!\nAutor invalid!\n"
        
        
        
        id_crt = '1234'
        titlu_nou = 'Harap-Alb'
        desc_noua = 'basm'
        autor_nou = 'Ion Creanga'
        
        try:
            lcarti.modificaCrtDupaID(id_crt, titlu_nou, desc_noua, autor_nou)
        except ValueError as ve:
            assert str(ve) == "Nu exista nicio carte cu acest id!\n"
        
        id_crt = '175'
        titlu_crt = 'Where the crawdads sing'
        desc_crt = 'O carte despre o fetita'
        autor_crt = 'Delia Owens'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        lcarti.adauga_carte(crt)
    
        id_crt = '213'
        
        try:
            assert lcarti.cautaCrtDupaID(id_crt).__str__() == '213,Ugly Love,O carte despre iubire,Coleen Hoover'
            assert True
        except ValueError:
            assert False
        
        id_crt = '980'
        
        try:
            lcarti.cautaCrtDupaID(id_crt) 
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista nicio carte cu acest id!\n"
        
        id_crt = ''
        
        try:
            lcarti.cautaCrtDupaID(id_crt) 
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista nicio carte cu acest id!\n"
    
    def test_generator_carti(self):
        carti = {}
        
        generator = genereazaCrt(carti)
        
        assert generator.genCrt.lungimeListaCarti() == 0
        
        nr_gen = 3
        
        try:
            generator.genereazaRandomCrt(nr_gen)
            assert True
        except ValueError:
            assert False
        
        assert generator.genCrt.lungimeListaCarti() == 3
        
        nr_gen = 0
        
        try:
            generator.genereazaRandomCrt(nr_gen)
            assert False
        except ValueError as ve:
            assert str(ve) == "Valoare invalida!\n"
            
        
            
    def test_valid_carte(self):
        id_crt = '123'
        titlu_crt = 'Ion'
        desc_crt = 'O carte despre un taran'
        autor_crt = 'Liviu Rebreanu'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        crtDeValidat = validator_crt(crt)
        
        try:
            crtDeValidat.valideaza_crt()
            assert True
        except ValueError:
            assert False

        id_crt_incorect = ''
        titlu_crt_incorect = ''
        desc_crt_incorect = ''
        autor_crt_incorect = ''
        crt = carte(id_crt_incorect, titlu_crt_incorect, desc_crt_incorect, autor_crt_incorect)
        crtDeNevalidat = validator_crt(crt)
        
        try:
            crtDeNevalidat.valideaza_crt()
            assert False
        except ValueError as ve:
            assert str(ve) == "Id invalid!\nTitlu invalid!\nDescriere invalida!\nAutor invalid!\n"
    
    def test_creare_client(self):
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        assert clt.getIdClt() == id_clt
        assert clt.getNumeClt() == nume_clt
        assert clt.getCnpClt() == cnp_clt
        
    def test_repo_clt(self):
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        clienti = {}
        lclienti = repo_clt(clienti)
        assert lclienti.lungimeListaClienti() == 0
        
        try:
            lclienti.verificaIDclt(clt)
            assert True
        except ValueError:
            assert False
        
        lclienti.adauga_client(clt)
        assert lclienti.lungimeListaClienti() == 1
        
        id_clt = '475'
        nume_clt ='Taranu Robert'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        try:
            lclienti.verificaIDclt(clt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Id existent!\n"
        
        try:
            lclienti.verificaCNPclt(clt)
            assert False
        except ValueError as ve:
            assert str(ve) == "CNP existent!\n" 
            
        id_clt = '812'
        nume_clt ='Taranu Robert'
        cnp_clt = '507122000811223'
        clt = client(id_clt, nume_clt, cnp_clt)
        lclienti.adauga_client(clt)
        
        assert lclienti.__str__() == "475,Asaftei Stefan,506072003890023\n812,Taranu Robert,507122000811223\n\n"
        assert lclienti.lungimeListaClienti() == 2
        
        id_clt = '475'
        lclienti.stergeCltDupaID(id_clt)
        assert lclienti.__str__() == "812,Taranu Robert,507122000811223\n\n"
        assert lclienti.lungimeListaClienti() == 1
        
        id_clt = '1334'
        try:
            lclienti.stergeCltDupaID(id_clt)
        except ValueError as ve:
            assert str(ve) == "Nu exista niciun client cu acest id!\n"
        
        id_clt = '812'
        nume_nou = 'Tamara Soptica'
        cnp_nou = '607122000811223'
        
        try:
            lclienti.modificaCltDupaID(id_clt, nume_nou, cnp_nou)
            assert True
        except ValueError:
            assert False
        
        assert lclienti.__str__() == "812,Tamara Soptica,607122000811223\n\n"
        
        id_clt = '812'
        nume_nou = ''
        cnp_nou = ''
        
        try:
            lclienti.modificaCltDupaID(id_clt, nume_nou, cnp_nou)
        except ValueError as ve:
            assert str(ve) == "Nume invalid!\nCNP invalid!\n"
        
        id_clt = '218'
        nume_nou = 'Sorina Cront'
        cnp_nou = '604021997678900'
        
        try:
            lclienti.modificaCltDupaID(id_clt, nume_nou, cnp_nou)
        except ValueError as ve:
            assert str(ve) == "Nu exista niciun client cu acest id!\n"
        
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)
        lclienti.adauga_client(clt)

        id_c = '812'
        
        try:
            assert lclienti.cautaCltDupaID(id_c).__str__() == "812,Tamara Soptica,607122000811223"
            assert True
        except ValueError:
            assert False
        
        id_c = '150'
        
        try:
            lclienti.cautaCltDupaID(id_c)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista niciun client cu acest id!\n"
        
        id_c = ''
        try:
            lclienti.cautaCltDupaID(id_c)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista niciun client cu acest id!\n"
    
    def test_generator_clienti(self):
        clienti = {}
        
        generator = genereazaClt(clienti)
        
        assert generator.genClt.lungimeListaClienti() == 0
        
        nr_gen = 3
        
        try:
            generator.genClt.genereazaRandomCrt(nr_gen)
            assert True
        except ValueError:
            assert False
        
        assert generator.genClt.lungimeListaClienti() == 3
        
        nr_gen = 0
        
        try:
            generator.genClt.genereazaRandomCrt(nr_gen)
            assert False
        except ValueError as ve:
            assert str(ve) == ("Valoare invalida!\n")
    
        
    def teste_valid_client(self):
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        cltDeValidat = validator_clt(clt)
        
        try:
            cltDeValidat.valideaza_clt()
            assert True
        except ValueError:
            assert False
        
        id_clt = ''
        nume_clt = ''
        cnp_clt = '12cd'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        cltDeNevalidat = validator_clt(clt)
        
        try:
            cltDeNevalidat.valideaza_clt()
            assert False
        except ValueError as ve:
            assert str(ve) == "Id invalid!\nNume invalid!\nCNP invalid!\n"
        
        id_clt = ''
        nume_clt = ''
        cnp_clt = ''
        clt = client(id_clt, nume_clt, cnp_clt)
        
        cltDeNevalidat = validator_clt(clt)
        
        try:
            cltDeNevalidat.valideaza_clt()
            assert False
        except ValueError as ve:
            assert str(ve) == "Id invalid!\nNume invalid!\nCNP invalid!\n"
    
    def teste_creare_inchiriere(self):
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)   
        
        id_crt = '175'
        titlu_crt = 'Where the crawdads sing'
        desc_crt = 'O carte despre o fetita'
        autor_crt = 'Delia Owens'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        inc = inchiriere(clt, crt)
            
        assert inc.getCltInc() ==  clt
        assert inc.getCrtInc() == crt
            
            
    def teste_repo_inc(self):
        incs = []
        linc = repo_inc(incs)
        assert linc.lungime() == 0
        
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)   
        
        id_crt = '175'
        titlu_crt = 'Where the crawdads sing'
        desc_crt = 'O carte despre o fetita'
        autor_crt = 'Delia Owens'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        inc = inchiriere(clt, crt)
        linc.adaugaInc(inc)
        assert linc.lungime() == 1
        
        id_clt = '812'
        nume_clt ='Taranu Robert'
        cnp_clt = '507122000811223'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        inc = inchiriere(clt, crt)
        
        try:
            linc.verificaExistenta(inc)
            assert False
        except ValueError as ve:
            assert str(ve) == "Carte deja inchiriata!\n"
        
        id_crt = '123'
        titlu_crt = 'Harry Potter si piatra filosofala'
        desc_crt = 'volumul 1'
        autor_crt = 'JK Rowlling'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        inc = inchiriere(clt, crt)
        
        try:
            linc.verificaExistenta(inc)
            assert True
        except ValueError:
            assert False
        
        try:
            linc.stergeInc(inc)
            assert False
        except ValueError as ve:
            assert str(ve) == "Clientul nu are aceasta carte inchiriata!\n"
        
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)   
        
        id_crt = '175'
        titlu_crt = 'Where the crawdads sing'
        desc_crt = 'O carte despre o fetita'
        autor_crt = 'Delia Owens'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        inc = inchiriere(clt, crt)
        
        try:
            linc.stergeInc(inc)
            assert True
        except ValueError:
            assert False
    
    def teste_service_inchirieri(self):
        clienti = {}
        carti = {}
        incs = []
        
        repocrt = repo_crt(carti)
        repoclt = repo_clt(clienti)
        repoinc = repo_inc(incs)
        
        
        id_crt = "1"
        titlu_crt = "Ugly love"
        desc_crt = "O carte despre iubire"
        autor_crt = "Colleen Hoover"
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        repocrt.adauga_carte(crt)
        
        id_crt = "2"
        titlu_crt = "Enigma Otiliei"
        desc_crt = "O carte despre maturizare"
        autor_crt = "George Calinescu"
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        repocrt.adauga_carte(crt)
        
        id_crt = "3"
        titlu_crt = "Un barbat pe nume Ove"
        desc_crt = "O carte despre un  batran"
        autor_crt = "Fredrick Backman"
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        repocrt.adauga_carte(crt)
        
        id_clt = "11"
        nume_clt = "Asaftei Stefan"
        cnp_clt = "502032000637489"
        clt = client(id_clt, nume_clt, cnp_clt)
        repoclt.adauga_client(clt)
        
        id_clt = "12"
        nume_clt = "Taranu Robert"
        cnp_clt = "505121999647288"
        clt = client(id_clt, nume_clt, cnp_clt)
        repoclt.adauga_client(clt)
        
        id_clt = "13"
        nume_clt = "Vranciu Alexia"
        cnp_clt = "612062001767898"
        clt = client(id_clt, nume_clt, cnp_clt)
        repoclt.adauga_client(clt)
        
        service = serviceInc(carti, clienti, incs, 2, "", "", "")
        assert service.mostRented() == []
        assert service.mostActive() == []
        
        
        inc = inchiriere(repoclt.cautaCltDupaID('12'), repocrt.cautaCrtDupaID('3'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('12'))
        service.incrementareIncCarte(repocrt.cautaCrtDupaID('3'))
        repoinc.adaugaInc(inc)
        service.stergeIncAnumitaCrt('2')
        assert repoinc.lungime() == 1
        service.stergeIncAnumitaCrt('3')
        assert repoinc.lungime() == 0
        
        inc = inchiriere(repoclt.cautaCltDupaID('12'), repocrt.cautaCrtDupaID('3'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('12'))
        service.incrementareIncCarte(repocrt.cautaCrtDupaID('3'))
        repoinc.adaugaInc(inc)
        service.stergeIncAnumitClient('11')
        assert repoinc.lungime() == 1
        service.stergeIncAnumitClient('12')
        assert repoinc.lungime() == 0
        
        inc = inchiriere(repoclt.cautaCltDupaID('11'), repocrt.cautaCrtDupaID('2'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('11'))
        service.incrementareIncCarte(repocrt.cautaCrtDupaID('2'))
        repoinc.adaugaInc(inc)
        repoinc.stergeInc(inc)
        
    
        assert service.mostRented() == [repocrt.cautaCrtDupaID('3'), repocrt.cautaCrtDupaID('2')]
        
        inc = inchiriere(repoclt.cautaCltDupaID('13'),repocrt.cautaCrtDupaID('2'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('13'))
        service.incrementareIncCarte(repocrt.cautaCrtDupaID('2'))
        repoinc.adaugaInc(inc)
        assert service.mostRented() == [repocrt.cautaCrtDupaID('3'), repocrt.cautaCrtDupaID('2')]
        assert service.mostActive() == [repoclt.cautaCltDupaID('12'), repoclt.cautaCltDupaID('11'), repoclt.cautaCltDupaID('13')]
        
        inc = inchiriere(repoclt.cautaCltDupaID('12'), repocrt.cautaCrtDupaID('3'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('12'))
        service.incrementareIncCarte(repocrt.cautaCrtDupaID('3'))
        repoinc.adaugaInc(inc)
        assert service.ordDupaNume()  == [repoclt.cautaCltDupaID('12'), repoclt.cautaCltDupaID('13')]
        
        inc = inchiriere(repoclt.cautaCltDupaID('13'), repocrt.cautaCrtDupaID('1'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('13'))
        service.incrementareIncCarte(repocrt.cautaCrtDupaID('1'))
        repoinc.adaugaInc(inc)
        assert service.ordDupaNrCrt() == [repoclt.cautaCltDupaID('13'), repoclt.cautaCltDupaID('12')]
        
        assert service.clientiCartiAnumitaLitera('U') ==  [repoclt.cautaCltDupaID('12'), repoclt.cautaCltDupaID('13')]
        try:
            service.clientiCartiAnumitaLitera('s')
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista clienti care sa indeplineasca cerinta!\n"  
                                       
    def goleste_fisier(self, cale):
        with open(cale, "w") as f:
            f.write("")
            
    def teste_fisiere_crt(self):
        carti = {}
        cale = "teste_carti.txt"
        repo = file_repo_crt(carti, cale)
        self.goleste_fisier(cale)
        assert repo.lungimeListaCarti() == 0
        
        id_crt = '123'
        titlu_crt = 'Ugly Love'
        desc_crt = 'Iubire'
        autor_crt ='Colleen Hoover'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        repo.adauga_carte(crt)
        assert repo.lungimeListaCarti() == 1
        
        crt_gasita = repo.cautaCrtDupaID(id_crt)
        
        assert crt_gasita.getIdCrt() == id_crt
        assert crt_gasita.getTitluCrt() == titlu_crt
        assert crt_gasita.getDescCrt() == desc_crt
        assert crt_gasita.getAutorCrt() == autor_crt
        
        id_crt = '123'
        titlu_crt = 'Enigma Otiliei'
        desc_crt = 'Maturizare'
        autor_crt ='George Calinescu'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        try:
            repo.verificaIDcrt(crt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Id existent!\n"
        
        id_crt = '234'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        repo.adauga_carte(crt)
        assert repo.lungimeListaCarti() == 2
        
        id_crt = '123'
        repo.stergeCrtDupaID(id_crt)
        assert repo.lungimeListaCarti() == 1
        assert str(repo) == "234,Enigma Otiliei,Maturizare,George Calinescu\n\n"
        
        id_crt = '1234'
        try:
            repo.stergeCrtDupaID(id_crt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista nicio carte cu acest id!\n"
        
        id_crt = '234'
        titlu_crt = 'Ugly Love'
        desc_crt = 'Iubire'
        autor_crt = 'Colleen Hoover'
        
        repo.modificaCrtDupaID(id_crt, titlu_crt, desc_crt, autor_crt)
        
        crt_gasita = repo.cautaCrtDupaID(id_crt)
        assert crt_gasita.getIdCrt() == id_crt
        assert crt_gasita.getTitluCrt() == titlu_crt
        assert crt_gasita.getDescCrt() == desc_crt
        assert crt_gasita.getAutorCrt() == autor_crt
        
        id_crt = '1234'
        
        try:
            repo.modificaCrtDupaID(id_crt, titlu_crt, desc_crt, autor_crt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista nicio carte cu acest id!\n"
        
        id_crt = '234'
        titlu_crt = ''
        desc_crt = ''
        autor_crt = ''
        
        try:
            repo.modificaCrtDupaID(id_crt, titlu_crt, desc_crt, autor_crt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Titlu invalid!\nDescriere invalida!\nAutor invalid!\n"
           
        id_crt = '1234' 
        try:
            repo.cautaCrtDupaID(id_crt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista nicio carte cu acest id!\n"
        
        id_crt = ''
        try:
            repo.cautaCrtDupaID(id_crt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista nicio carte cu acest id!\n"
    
            
    def teste_fisiere_clt(self):
        clienti = {}
        cale = "teste_clienti.txt"
        self.goleste_fisier(cale)
        repo = file_repo_clt(clienti, cale)
        assert repo.lungimeListaClienti() == 0
        
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        assert repo.lungimeListaClienti() == 0
        
        try:
            repo.verificaIDclt(clt)
            assert True
        except ValueError:
            assert False
        
        repo.adauga_client(clt)
        assert repo.lungimeListaClienti() == 1
        
        id_clt = '475'
        nume_clt ='Taranu Robert'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        try:
            repo.verificaIDclt(clt)
            assert False
        except ValueError as ve:
            assert str(ve) == "Id existent!\n"
        
        try:
            repo.verificaCNPclt(clt)
            assert False
        except ValueError as ve:
            assert str(ve) == "CNP existent!\n" 
            
        id_clt = '812'
        nume_clt ='Taranu Robert'
        cnp_clt = '507122000811223'
        clt = client(id_clt, nume_clt, cnp_clt)
        repo.adauga_client(clt)
        
        assert repo.__str__() == "475,Asaftei Stefan,506072003890023\n812,Taranu Robert,507122000811223\n\n"
        assert repo.lungimeListaClienti() == 2
        
        id_clt = '475'
        repo.stergeCltDupaID(id_clt)
        assert repo.__str__() == "812,Taranu Robert,507122000811223\n\n"
        assert repo.lungimeListaClienti() == 1
        
        id_clt = '1334'
        try:
            repo.stergeCltDupaID(id_clt)
        except ValueError as ve:
            assert str(ve) == "Nu exista niciun client cu acest id!\n"
        
        id_clt = '812'
        nume_nou = 'Tamara Soptica'
        cnp_nou = '607122000811223'
        
        try:
            repo.modificaCltDupaID(id_clt, nume_nou, cnp_nou)
            assert True
        except ValueError:
            assert False
        
        assert repo.__str__() == "812,Tamara Soptica,607122000811223\n\n"
        
        id_clt = '812'
        nume_nou = ''
        cnp_nou = ''
        
        try:
            repo.modificaCltDupaID(id_clt, nume_nou, cnp_nou)
        except ValueError as ve:
            assert str(ve) == "Nume invalid!\nCNP invalid!\n"
        
        id_clt = '218'
        nume_nou = 'Sorina Cront'
        cnp_nou = '604021997678900'
        
        try:
            repo.modificaCltDupaID(id_clt, nume_nou, cnp_nou)
        except ValueError as ve:
            assert str(ve) == "Nu exista niciun client cu acest id!\n"
        
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)
        repo.adauga_client(clt)

        id_c = '812'
        
        try:
            assert repo.cautaCltDupaID(id_c).__str__() == "812,Tamara Soptica,607122000811223"
            assert True
        except ValueError:
            assert False
        
        id_c = '150'
        
        try:
            repo.cautaCltDupaID(id_c)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista niciun client cu acest id!\n"
        
        id_c = ''
        try:
            repo.cautaCltDupaID(id_c)
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista niciun client cu acest id!\n"
    
    
    def teste_fisiere_inchirieri(self):
        cale = "teste_inchirieri.txt"
        incs = []
        linc = file_repo_inc(incs, cale)
        self.goleste_fisier(cale)
        assert linc.lungime() == 0
        
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)   
        
        id_crt = '175'
        titlu_crt = 'Where the crawdads sing'
        desc_crt = 'O carte despre o fetita'
        autor_crt = 'Delia Owens'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        inc = inchiriere(clt, crt)
        linc.adaugaInc(inc)  
        assert linc.lungime() == 1
             
        id_clt = '812'
        nume_clt ='Taranu Robert'
        cnp_clt = '507122000811223'
        clt = client(id_clt, nume_clt, cnp_clt)
        
        inc = inchiriere(clt, crt)
        
        try:
            linc.verificaExistenta(inc)
            assert False
        except ValueError as ve:
            assert str(ve) == "Carte deja inchiriata!\n"
        
        id_crt = '123'
        titlu_crt = 'Harry Potter si piatra filosofala'
        desc_crt = 'volumul 1'
        autor_crt = 'JK Rowlling'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        inc = inchiriere(clt, crt)
        
        try:
            linc.verificaExistenta(inc)
            assert True
        except ValueError:
            assert False
        
        try:
            linc.stergeInc(inc)
            assert False
        except ValueError as ve:
            assert str(ve) == "Clientul nu are aceasta carte inchiriata!\n"
        
        id_clt = '475'
        nume_clt ='Asaftei Stefan'
        cnp_clt = '506072003890023'
        clt = client(id_clt, nume_clt, cnp_clt)   
        
        id_crt = '175'
        titlu_crt = 'Where the crawdads sing'
        desc_crt = 'O carte despre o fetita'
        autor_crt = 'Delia Owens'
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        
        inc = inchiriere(clt, crt)
        
        try:
            linc.stergeInc(inc)
            assert True
        except ValueError:
            assert False
    
    def teste_service_cu_fisiere_inchirieri(self):
        clienti = {}
        carti = {}
        incs = []
        caleclt = "teste_clienti.txt"
        calecrt = "teste_carti.txt"
        caleinc = "teste_inchirieri.txt"
        repocrt = file_repo_crt(carti, calecrt)
        repoclt = file_repo_clt(clienti, caleclt)
        repoinc = file_repo_inc(incs, caleinc)
        
        service = serviceInc(clienti, carti, incs, 1, calecrt, caleclt, caleinc)
        
        id_crt = "1"
        titlu_crt = "Ugly love"
        desc_crt = "O carte despre iubire"
        autor_crt = "Colleen Hoover"
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        repocrt.adauga_carte(crt)
        
        id_crt = "2"
        titlu_crt = "Enigma Otiliei"
        desc_crt = "O carte despre maturizare"
        autor_crt = "George Calinescu"
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        repocrt.adauga_carte(crt)
        
        id_crt = "3"
        titlu_crt = "Un barbat pe nume Ove"
        desc_crt = "O carte despre un  batran"
        autor_crt = "Fredrick Backman"
        crt = carte(id_crt, titlu_crt, desc_crt, autor_crt)
        repocrt.adauga_carte(crt)
        
        id_clt = "11"
        nume_clt = "Asaftei Stefan"
        cnp_clt = "502032000637489"
        clt = client(id_clt, nume_clt, cnp_clt)
        repoclt.adauga_client(clt)
        
        id_clt = "12"
        nume_clt = "Taranu Robert"
        cnp_clt = "505121999647288"
        clt = client(id_clt, nume_clt, cnp_clt)
        repoclt.adauga_client(clt)
        
        id_clt = "13"
        nume_clt = "Vranciu Alexia"
        cnp_clt = "612062001767898"
        clt = client(id_clt, nume_clt, cnp_clt)
        repoclt.adauga_client(clt)
        
        assert service.mostRented() == []
        assert service.mostActive() == []
        
        inc = inchiriere(repoclt.cautaCltDupaID('12'), repocrt.cautaCrtDupaID('3'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('12'))
        service.incrementareIncClient(repocrt.cautaCrtDupaID('3'))
        repoinc.adaugaInc(inc)
        service.stergeIncAnumitaCrt('2')
        assert repoinc.lungime() == 1
        service.stergeIncAnumitaCrt('3')
        assert repoinc.lungime() == 0
        
        inc = inchiriere(repoclt.cautaCltDupaID('12'), repocrt.cautaCrtDupaID('3'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('12'))
        service.incrementareIncClient(repocrt.cautaCrtDupaID('3'))
        repoinc.adaugaInc(inc)
        service.stergeIncAnumitClient('11')
        assert repoinc.lungime() == 1
        service.stergeIncAnumitClient('12')
        assert repoinc.lungime() == 0
        
        inc = inchiriere(repoclt.cautaCltDupaID('11'), repocrt.cautaCrtDupaID('2'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('11'))
        service.incrementareIncClient(repocrt.cautaCrtDupaID('2'))
        repoinc.stergeInc(inc)
        
        assert service.mostRented() == [repocrt.cautaCrtDupaID('3'), repocrt.cautaCrtDupaID('2'), repocrt.cautaCrtDupaID('1')]
        
        inc = inchiriere(repoclt.cautaCltDupaID('13'),repocrt.cautaCrtDupaID('2'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('13'))
        service.incrementareIncClient(repocrt.cautaCrtDupaID('2'))
        assert service.mostRented() == [repocrt.cautaCrtDupaID('3'), repocrt.cautaCrtDupaID('2'), repocrt.cautaCrtDupaID('1')]
        assert service.mostActive() == [repoclt.cautaCltDupaID('12'), repoclt.cautaCltDupaID('11'), repoclt.cautaCltDupaID('13')]
        
        inc = inchiriere(repoclt.cautaCltDupaID('12'), repocrt.cautaCrtDupaID('3'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('12'))
        service.incrementareIncClient(repocrt.cautaCrtDupaID('3'))
        assert service.ordDupaNume(repoclt.cautaCltDupaID('12'), repoclt.cautaCltDupaID('13'))
        
        inc = inchiriere(repoclt.cautaCltDupaID('13'), repocrt.cautaCrtDupaID('1'))
        service.incrementareIncClient(repoclt.cautaCltDupaID('13'))
        service.incrementareIncClient(repocrt.cautaCrtDupaID('1'))
        assert service.ordDupaNrCrt(repoclt.cautaCltDupaID('13'), repoclt.cautaCltDupaID('12'))
        
        assert service.clientiCartiAnumitaLitera('U') ==  [repoclt.cautaCltDupaID('12'), repoclt.cautaCltDupaID('13')]
        try:
            service.clientiCartiAnumitaLitera('s')
            assert False
        except ValueError as ve:
            assert str(ve) == "Nu exista clienti care sa indeplineasca cerinta!\n" 
            
     
    def teste_algoritmi_sortare(self):
        carti = {}
        clienti = {}
        incs = []
        serv = serviceInc(carti, clienti, incs, 2, "teste_carti.txt", "teste_clienti.txt", "teste_inchirieri.txt")
        lista = [7,2,3,8,9,0]
        serv.mergeSort(lista, 0, 5)
        assert lista == [0,2,3,7,8,9]
        lista = [7,2,3,8,9,0]
        serv.mergeSort(lista, 0, 5, reversed = True)
        assert lista == [9,8,7,3,2,0]
        
        lista = [7,2,3,8,9,0]
        serv.bingoSort(lista)
        assert lista == [0,2,3,7,8,9]
        lista = [7,2,3,8,9,0]
        serv.bingoSort(lista, reversed=True)
        assert lista == [9,8,7,3,2,0]
        
    def ruleaza_toate_testele(self):
        self.test_creare_carte()
        print("Teste creare carte rulate cu succes!")
        
        self.test_repo_crt()
        print("Teste repo carte rulate cu succes!")
        
        self.test_valid_carte()
        print("Teste validator carte rulate cu succes!")
        
        self.test_creare_client()
        print("Teste creare client rulate cu succes!")
        
        self.test_repo_clt()
        print("Teste repo client rulate cu succes!")
        
        self.teste_valid_client()
        print("Teste validator client rulate cu succes!")
        
        self.teste_creare_inchiriere()
        print("Teste crearee inchiriere rulate cu succes!")
        
        self.teste_repo_inc()
        print("Teste repo inchiriere rulate cu succes!")
        
        self.teste_service_inchirieri()
        print("Teste inchirieri rulate cu succes!")
        
        self.teste_fisiere_crt()
        print("Teste fisiere carti rulate cu succes!")
        
        self.teste_fisiere_clt()
        print("Teste fisiere clienti rulate cu succes!")
        
        self.teste_fisiere_inchirieri()
        print("Teste fisiere inchirieri rulate cu succes!")

        self.teste_algoritmi_sortare()
        print("Teste algoritmi sortare rulate cu succes!")
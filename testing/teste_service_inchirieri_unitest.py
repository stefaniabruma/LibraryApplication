'''
Created on 20 dec. 2022

@author: stefa
'''
import unittest
from business.service_inchirieri import serviceInc
from repository.repository_clienti import repo_clt
from repository.repository_carti import repo_crt
from client import client
from carte import carte
from repository.repository_inchirieri import repo_inc
from inchiriere import inchiriere

class TestCaseServiceInchirieriFaraFisiere(unittest.TestCase):
    '''
    un nnou tip de data pentru testele service-ului de inchirieri fara fisiere
    '''
    def setUp(self):
        clienti = {}
        carti = {}
        incs = []
        
        self.__repoclt = repo_clt(clienti)
        self.__repocrt = repo_crt(carti)
        
        self.__repoclt.adauga_client(client('1', 'Asaftei Stefan', '512032000566787'))
        self.__repoclt.adauga_client(client('2', 'Taranu Robert', '517111999099889'))
        self.__repoclt.adauga_client(client('3', 'Vranciu Alexia', '610082001998873'))
        self.__repoclt.adauga_client(client('4', 'Aioanei Laura', '603021999998447'))
        self.__repoclt.adauga_client(client('5', 'Soptica Tamara', '610041998998772'))
        
        self.__repocrt.adauga_carte(carte('11', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover'))
        self.__repocrt.adauga_carte(carte('12', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu'))
        self.__repocrt.adauga_carte(carte('13', 'Un barbat pe nume Ove', 'O carte despre un batran', 'Fredrick Backman'))
        self.__repocrt.adauga_carte(carte('14', 'Harry Potter si piatra filosofala', 'O carte despre magie', 'JK Rowlling'))
        
        self.__repoinc = repo_inc(incs)
        
        self.__serv = serviceInc(carti, clienti, incs, 2, "teste_carti_unitest.txt", "teste_clienti_unitest.txt", "teste_inchirieri_unitest.txt")
        inc = inchiriere(self.__repoclt.cautaCltDupaID('1'), self.__repocrt.cautaCrtDupaID('13'))
        self.__repoinc.adaugaInc(inc)
        self.__serv.incrementareIncClient(self.__repoclt.cautaCltDupaID('1'))
        self.__serv.incrementareIncCarte(self.__repocrt.cautaCrtDupaID('13'))
        inc = inchiriere(self.__repoclt.cautaCltDupaID('2'), self.__repocrt.cautaCrtDupaID('11'))
        self.__repoinc.adaugaInc(inc)
        self.__serv.incrementareIncClient(self.__repoclt.cautaCltDupaID('2'))
        self.__serv.incrementareIncCarte(self.__repocrt.cautaCrtDupaID('11'))
        
        inc = inchiriere(self.__repoclt.cautaCltDupaID('1'), self.__repocrt.cautaCrtDupaID('13'))
        self.__repoinc.stergeInc(inc)
        
        inc = inchiriere(self.__repoclt.cautaCltDupaID('4'), self.__repocrt.cautaCrtDupaID('13'))
        self.__repoinc.adaugaInc(inc)
        self.__serv.incrementareIncClient(self.__repoclt.cautaCltDupaID('4'))
        self.__serv.incrementareIncCarte(self.__repocrt.cautaCrtDupaID('13'))
        inc = inchiriere(self.__repoclt.cautaCltDupaID('1'), self.__repocrt.cautaCrtDupaID('14'))
        self.__repoinc.adaugaInc(inc)
        self.__serv.incrementareIncClient(self.__repoclt.cautaCltDupaID('1'))
        self.__serv.incrementareIncCarte(self.__repocrt.cautaCrtDupaID('14'))

        
    def test_StergereEntitatiDeBaza(self):
        self.assertEqual(self.__repoclt.lungimeListaClienti(), 5)
        self.assertEqual(self.__repoinc.lungime(), 3)
        self.assertEqual(self.__repocrt.lungimeListaCarti(), 4)
        self.__serv.stergeIncAnumitClient('4')
        self.assertEqual(self.__repoclt.lungimeListaClienti(), 5)
        self.assertEqual(self.__repoinc.lungime(), 2)
        self.__serv.stergeIncAnumitaCrt('14')
        self.assertEqual(self.__repocrt.lungimeListaCarti(), 4)
        self.assertEqual(self.__repoinc.lungime(), 1)
    
    def test_MostRented(self):
        self.assertEqual(self.__serv.mostRented(), [self.__repocrt.cautaCrtDupaID('13'), self.__repocrt.cautaCrtDupaID('11'), self.__repocrt.cautaCrtDupaID('14')])
    
    def test_MostActive(self):
        self.assertEqual(self.__serv.mostActive(), [self.__repoclt.cautaCltDupaID('1'), self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4')])
    
    def test_OrdDupaNume(self):
        self.assertEqual(self.__serv.ordDupaNume(), [self.__repoclt.cautaCltDupaID('4'), self.__repoclt.cautaCltDupaID('1'), self.__repoclt.cautaCltDupaID('2')])
        
    def test_OrdDupaCartiInc(self):
        self.assertEqual(self.__serv.ordDupaNrCrt(), [self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4'), self.__repoclt.cautaCltDupaID('1')])
    
    def test_ClientiCuCartiCuAnumitaLitera(self):
        self.assertEqual(self.__serv.clientiCartiAnumitaLitera('U'), [self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4')])
        self.assertRaises(ValueError, self.__serv.clientiCartiAnumitaLitera, 'O')
        self.assertRaises(ValueError, self.__serv.clientiCartiAnumitaLitera, ';')
        
class TestCaseServiceInchirieriCuFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele service-ului de inchirieri cu fisiere
    '''
    def setUp(self):
        clienti = {}
        carti = {}
        incs = []
        self.golesteFisier("teste_carti_unitest.txt")
        self.golesteFisier("teste_clienti_unitest.txt")
        self.golesteFisier("teste_inchirieri_unitest.txt")
        
        self.__repoclt = repo_clt(clienti)
        self.__repocrt = repo_crt(carti)
        
        self.__repoclt.adauga_client(client('1', 'Asaftei Stefan', '512032000566787'))
        self.__repoclt.adauga_client(client('2', 'Taranu Robert', '517111999099889'))
        self.__repoclt.adauga_client(client('3', 'Vranciu Alexia', '610082001998873'))
        self.__repoclt.adauga_client(client('4', 'Aioanei Laura', '603021999998447'))
        self.__repoclt.adauga_client(client('5', 'Soptica Tamara', '610041998998772'))
        
        self.__repocrt.adauga_carte(carte('11', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover'))
        self.__repocrt.adauga_carte(carte('12', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu'))
        self.__repocrt.adauga_carte(carte('13', 'Un barbat pe nume Ove', 'O carte despre un batran', 'Fredrick Backman'))
        self.__repocrt.adauga_carte(carte('14', 'Harry Potter si piatra filosofala', 'O carte despre magie', 'JK Rowlling'))
        
        self.__repoinc = repo_inc(incs)
        
        self.__serv = serviceInc(carti, clienti, incs, 2, "teste_carti_unitest.txt", "teste_clienti_unitest.txt", "teste_inchirieri_unitest.txt")
        inc = inchiriere(self.__repoclt.cautaCltDupaID('1'), self.__repocrt.cautaCrtDupaID('13'))
        self.__repoinc.adaugaInc(inc)
        self.__serv.incrementareIncClient(self.__repoclt.cautaCltDupaID('1'))
        self.__serv.incrementareIncCarte(self.__repocrt.cautaCrtDupaID('13'))
        inc = inchiriere(self.__repoclt.cautaCltDupaID('2'), self.__repocrt.cautaCrtDupaID('11'))
        self.__repoinc.adaugaInc(inc)
        self.__serv.incrementareIncClient(self.__repoclt.cautaCltDupaID('2'))
        self.__serv.incrementareIncCarte(self.__repocrt.cautaCrtDupaID('11'))
        
        inc = inchiriere(self.__repoclt.cautaCltDupaID('1'), self.__repocrt.cautaCrtDupaID('13'))
        self.__repoinc.stergeInc(inc)
        
        inc = inchiriere(self.__repoclt.cautaCltDupaID('4'), self.__repocrt.cautaCrtDupaID('13'))
        self.__repoinc.adaugaInc(inc)
        self.__serv.incrementareIncClient(self.__repoclt.cautaCltDupaID('4'))
        self.__serv.incrementareIncCarte(self.__repocrt.cautaCrtDupaID('13'))
        inc = inchiriere(self.__repoclt.cautaCltDupaID('1'), self.__repocrt.cautaCrtDupaID('14'))
        self.__repoinc.adaugaInc(inc)
        self.__serv.incrementareIncClient(self.__repoclt.cautaCltDupaID('1'))
        self.__serv.incrementareIncCarte(self.__repocrt.cautaCrtDupaID('14'))

    def golesteFisier(self, cale):
        with open(cale, "w") as f:
            f.write("")
             
    def test_StergereEntitatiDeBaza(self):
        self.assertEqual(self.__repoclt.lungimeListaClienti(), 5)
        self.assertEqual(self.__repoinc.lungime(), 3)
        self.assertEqual(self.__repocrt.lungimeListaCarti(), 4)
        self.__serv.stergeIncAnumitClient('4')
        self.assertEqual(self.__repoclt.lungimeListaClienti(), 5)
        self.assertEqual(self.__repoinc.lungime(), 2)
        self.__serv.stergeIncAnumitaCrt('14')
        self.assertEqual(self.__repocrt.lungimeListaCarti(), 4)
        self.assertEqual(self.__repoinc.lungime(), 1)
    
    def test_MostRented(self):
        self.assertEqual(self.__serv.mostRented(), [self.__repocrt.cautaCrtDupaID('13'), self.__repocrt.cautaCrtDupaID('11'), self.__repocrt.cautaCrtDupaID('14')])
    
    def test_MostActive(self):
        self.assertEqual(self.__serv.mostActive(), [self.__repoclt.cautaCltDupaID('1'), self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4')])
    
    def test_OrdDupaNume(self):
        self.assertEqual(self.__serv.ordDupaNume(), [self.__repoclt.cautaCltDupaID('4'), self.__repoclt.cautaCltDupaID('1'), self.__repoclt.cautaCltDupaID('2')])
        
    def test_OrdDupaCartiInc(self):
        self.assertEqual(self.__serv.ordDupaNrCrt(), [self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4'), self.__repoclt.cautaCltDupaID('1')])
    
    def test_ClientiCuCartiCuAnumitaLitera(self):
        self.assertEqual(self.__serv.clientiCartiAnumitaLitera('U'), [self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4')])
        self.assertRaises(ValueError, self.__serv.clientiCartiAnumitaLitera, 'O')
        self.assertRaises(ValueError, self.__serv.clientiCartiAnumitaLitera, ';')
    
if __name__ == '__main__':
    unittest.main()
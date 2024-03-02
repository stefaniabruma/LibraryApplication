'''
Created on 18 dec. 2022

@author: stefa
'''
import unittest
from repository.repository_clienti import repo_clt
from client import client
from repository.repository_carti import repo_crt
from carte import carte
from business.service_inchirieri import inc_controller
from repository.repository_inchirieri import repo_inc

class TestCaseControllerInchirieri(unittest.TestCase):
    '''
    un nou tip de data pentru testele service-ului de inchirieri fara fisiere
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
        
        self.__cntrl = inc_controller(carti, clienti, incs, 2, "teste_carti_unitest.txt", "teste_clienti_unitest.txt", "teste_inchirieri_unitest.txt")
        self.__cntrl.cmd13('1', '13')
        self.__cntrl.cmd13('2', '11')
        
        self.__cntrl.cmd15('1', '13')
        
        self.__cntrl.cmd13('4', '13')
        self.__cntrl.cmd13('1', '14')
    
    def teste_Creare(self):
        self.assertTrue(len(self.__cntrl.cmd14()) == 3)
        self.assertRaises(ValueError, self.__cntrl.cmd13,'5', '15')
        self.assertRaises(ValueError, self.__cntrl.cmd13, '4', '14')
        
    def test_StergereEntitatiDeBaza(self):
        self.assertRaises(ValueError, self.__cntrl.cmd6, '6')
        self.assertEqual(self.__repoclt.lungimeListaClienti(), 5)
        self.assertEqual(self.__repoinc.lungime(), 3)
        self.__cntrl.cmd6('4')
        self.assertEqual(self.__repoclt.lungimeListaClienti(), 4)
        self.assertEqual(self.__repoinc.lungime(), 2)
        self.__cntrl.cmd5('14')
        self.assertEqual(self.__repocrt.lungimeListaCarti(), 3)
        self.assertEqual(self.__repoinc.lungime(), 1)
    
    def test_StergereInchirieri(self):
        self.assertRaises(ValueError, self.__cntrl.cmd15, '5', '15')
        self.assertRaises(ValueError, self.__cntrl.cmd15, '4', '14')
        self.__cntrl.cmd15('1', '14')
        self.assertTrue(self.__repoinc.lungime() == 2)
    
    def test_MostRented(self):
        self.assertEqual(self.__cntrl.cmd16(), [self.__repocrt.cautaCrtDupaID('13'), self.__repocrt.cautaCrtDupaID('11'), self.__repocrt.cautaCrtDupaID('14')])
    
    def test_MostActive(self):
        self.assertEqual(self.__cntrl.cmd17(), {'Asaftei Stefan':  2})
    
    def test_OrdDupaNume(self):
        self.assertEqual(self.__cntrl.cmd18(), [self.__repoclt.cautaCltDupaID('4'), self.__repoclt.cautaCltDupaID('1'), self.__repoclt.cautaCltDupaID('2')])
        
    def test_OrdDupaCartiInc(self):
        self.assertEqual(self.__cntrl.cmd19(), [self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4'), self.__repoclt.cautaCltDupaID('1')])
    
    def test_ClientiCuCartiCuAnumitaLitera(self):
        self.assertEqual(self.__cntrl.cmd20('U'), [self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4')])
        self.assertRaises(ValueError, self.__cntrl.cmd20, 'O')
        self.assertRaises(ValueError, self.__cntrl.cmd20, ';')

class TestCaseControllerInchirieriCuFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele service-ului de inchirieri cu fisiere
    '''
    
    def setUp(self):
        self.golesteFisier("teste_carti_unitest.txt")
        self.golesteFisier("teste_clienti_unitest.txt")
        self.golesteFisier("teste_inchirieri_unitest.txt")
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
        
        self.__cntrl = inc_controller(carti, clienti, incs, 2, "teste_carti_unitest.txt", "teste_clienti_unitest.txt", "teste_inchirieri_unitest.txt")
        self.__cntrl.cmd13('1', '13')
        self.__cntrl.cmd13('2', '11')
        
        self.__cntrl.cmd15('1', '13')
        
        self.__cntrl.cmd13('4', '13')
        self.__cntrl.cmd13('1', '14')
    
    def golesteFisier(self, cale):
        with open(cale, "w") as f:
            f.write("")
            
    def teste_Creare(self):
        self.assertTrue(len(self.__cntrl.cmd14()) == 3)
        self.assertRaises(ValueError, self.__cntrl.cmd13,'5', '15')
        self.assertRaises(ValueError, self.__cntrl.cmd13, '4', '14')
        
    def test_StergereEntitatiDeBaza(self):
        self.assertRaises(ValueError, self.__cntrl.cmd6, '6')
        self.assertEqual(self.__repoclt.lungimeListaClienti(), 5)
        self.assertEqual(self.__repoinc.lungime(), 3)
        self.__cntrl.cmd6('4')
        self.assertEqual(self.__repoclt.lungimeListaClienti(), 4)
        self.assertEqual(self.__repoinc.lungime(), 2)
        self.__cntrl.cmd5('14')
        self.assertEqual(self.__repocrt.lungimeListaCarti(), 3)
        self.assertEqual(self.__repoinc.lungime(), 1)
    
    def test_StergereInchirieri(self):
        self.assertRaises(ValueError, self.__cntrl.cmd15, '5', '15')
        self.assertRaises(ValueError, self.__cntrl.cmd15, '4', '14')
        self.__cntrl.cmd15('1', '14')
        self.assertTrue(self.__repoinc.lungime() == 2)
    
    def test_MostRented(self):
        self.assertEqual(self.__cntrl.cmd16(), [self.__repocrt.cautaCrtDupaID('13'), self.__repocrt.cautaCrtDupaID('11'), self.__repocrt.cautaCrtDupaID('14')])
    
    def test_MostActive(self):
        self.assertEqual(self.__cntrl.cmd17(), {'Asaftei Stefan':  2})
    
    def test_OrdDupaNume(self):
        self.assertEqual(self.__cntrl.cmd18(), [self.__repoclt.cautaCltDupaID('4'), self.__repoclt.cautaCltDupaID('1'), self.__repoclt.cautaCltDupaID('2')])
        
    def test_OrdDupaCartiInc(self):
        self.assertEqual(self.__cntrl.cmd19(), [self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4'), self.__repoclt.cautaCltDupaID('1')])
    
    def test_ClientiCuCartiCuAnumitaLitera(self):
        self.assertEqual(self.__cntrl.cmd20('U'), [self.__repoclt.cautaCltDupaID('2'), self.__repoclt.cautaCltDupaID('4')])
        self.assertRaises(ValueError, self.__cntrl.cmd20, 'O')
        self.assertRaises(ValueError, self.__cntrl.cmd20, ';')
    
if __name__ == '__main__':
    unittest.main()
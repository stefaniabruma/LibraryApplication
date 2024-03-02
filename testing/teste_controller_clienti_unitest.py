'''
Created on 18 dec. 2022

@author: stefa
'''
import unittest
from business.service_clienti import client_controller

class TestCaseClientiControllerFaraFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele controller ului de clienti fara fisiere
    '''
    def setUp(self):
        clienti = {}
        self.__cntrl = client_controller(clienti, 2, "teste_clienti_unitest.txt")
        self.__cntrl.cmd4('1', 'Asaftei Stefan', '512092000788998')
    
    def test_Creare(self):
        self.assertTrue(len(self.__cntrl.cmd2()) == 1)
        self.assertRaises(ValueError, self.__cntrl.cmd4, "", "", "")
        self.assertRaises(ValueError, self.__cntrl.cmd4, '1', 'Taranu Robert', '512092000788998')
    
    def test_Cautare(self):
        self.assertTrue(self.__cntrl.cmd10('1').getIdClt() == '1' and self.__cntrl.cmd10('1').getNumeClt() == "Asaftei Stefan" and self.__cntrl.cmd10('1').getCnpClt() == '512092000788998')
        self.assertRaises(ValueError, self.__cntrl.cmd10, '2')
    
    def test_Modificare(self):
        self.__cntrl.cmd8('1', 'Taranu Robert', '513041999273773')
        self.assertTrue(self.__cntrl.cmd10('1').getIdClt() == '1' and self.__cntrl.cmd10('1').getNumeClt() == 'Taranu Robert' and self.__cntrl.cmd10('1').getCnpClt() == '513041999273773')
        self.assertRaises(ValueError, self.__cntrl.cmd8, '2', 'Vranciu Alexia', '623122000677887')
        
    def test_Generare(self):
        self.assertRaises(ValueError, self.__cntrl.cmd12, -1)
        self.__cntrl.cmd12(3)
        self.assertTrue(len(self.__cntrl.cmd2()) == 4)
        
class TestCaseClientiControllerCuFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele controller ului de clienti cu fisiere
    '''
    def setUp(self):
        clienti = {}
        self.__cntrl = client_controller(clienti, 1, "teste_clienti_unitest.txt")
        self.golesteFisier("teste_clienti_unitest.txt")
        self.__cntrl.cmd4('1', 'Asaftei Stefan', '512092000788998')
    
    def golesteFisier(self, cale):
        with open(cale, "w") as f:
            f.write("")
    
    def test_Creare(self):
        self.assertTrue(len(self.__cntrl.cmd2()) == 1)
        self.assertRaises(ValueError, self.__cntrl.cmd4, "", "", "")
        self.assertRaises(ValueError, self.__cntrl.cmd4, '1', 'Taranu Robert', '512092000788998')
    
    def test_Cautare(self):
        self.assertTrue(self.__cntrl.cmd10('1').getIdClt() == '1' and self.__cntrl.cmd10('1').getNumeClt() == "Asaftei Stefan" and self.__cntrl.cmd10('1').getCnpClt() == '512092000788998')
        self.assertRaises(ValueError, self.__cntrl.cmd10, '2')
    
    def test_Modificare(self):
        self.__cntrl.cmd8('1', 'Taranu Robert', '513041999273773')
        self.assertTrue(self.__cntrl.cmd10('1').getIdClt() == '1' and self.__cntrl.cmd10('1').getNumeClt() == 'Taranu Robert' and self.__cntrl.cmd10('1').getCnpClt() == '513041999273773')
        self.assertRaises(ValueError, self.__cntrl.cmd8, '2', 'Vranciu Alexia', '623122000677887')
        
    def test_Generare(self):
        self.assertRaises(ValueError, self.__cntrl.cmd12, -1)
        self.__cntrl.cmd12(3)
        self.assertTrue(len(self.__cntrl.cmd2()) == 4)

if __name__ == '__main__':
    unittest.main()
'''
Created on 18 dec. 2022

@author: stefa
'''
import unittest
from business.service_carti import carte_controller
class TestCaseCartiControllerFaraFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele controller ului de carti
    '''
    def setUp(self):
        carti = {}
        self.__cntrl = carte_controller(carti, 2, "teste_carti_unitest.txt")
        self.__cntrl.cmd3('1', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover')
    
    def tearDown(self):
        pass
    
    def test_Creare(self):
        '''
        test blackbox
        '''
        
        self.assertTrue(len(self.__cntrl.cmd1()) == 1)
        self.assertRaises(ValueError, self.__cntrl.cmd3, '', '' ,'', '')
        self.assertRaises(ValueError, self.__cntrl.cmd3, '1', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu')
        self.assertRaises(ValueError, self.__cntrl.cmd3, '', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu')
        self.assertRaises(ValueError, self.__cntrl.cmd3, '1', '', 'O carte despre maturizare', 'George Calinescu')
        self.assertRaises(ValueError, self.__cntrl.cmd3, '1', 'Enigma Otiliei', '', 'George Calinescu')
        self.assertRaises(ValueError, self.__cntrl.cmd3, '1', 'Enigma Otiliei', 'O carte despre maturizare', '')
        self.__cntrl.cmd3('0', 'E', 'O', 'G')
        self.assertTrue(len(self.__cntrl.cmd1()) == 2)
        self.__cntrl.cmd3('1111111111111111111111111111111', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')
        self.assertTrue(len(self.__cntrl.cmd1()) == 3)
        self.__cntrl.cmd3('8', '2434', '4379347', '8737438')
        self.assertTrue(len(self.__cntrl.cmd1()) == 4)
        
    def test_Cautare(self):
        self.assertTrue(self.__cntrl.cmd9('1').getIdCrt() == '1' and self.__cntrl.cmd9('1').getTitluCrt() == 'Ugly Love' and self.__cntrl.cmd9('1').getDescCrt() == 'O carte despre iubire', self.__cntrl.cmd9('1').getAutorCrt() == 'Colleen Hoover')
        self.assertRaises(ValueError, self.__cntrl.cmd9,'2')
        
        
    def test_Modificare(self):
        self.__cntrl.cmd7('1', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu')
        self.assertTrue(self.__cntrl.cmd9('1').getIdCrt() == '1' and self.__cntrl.cmd9('1').getTitluCrt() == 'Enigma Otiliei' and self.__cntrl.cmd9('1').getDescCrt() == 'O carte despre maturizare', self.__cntrl.cmd9('1').getAutorCrt() == 'George Calinescu')
        self.assertRaises(ValueError, self.__cntrl.cmd7, '2', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover')
        
    def test_Generare(self):
        self.assertRaises(ValueError, self.__cntrl.cmd11, -1)
        self.__cntrl.cmd11(3)
        self.assertTrue(len(self.__cntrl.cmd1()) == 4)

class TestCaseCartiControllerCuFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele controller ului de carti
    '''
    def setUp(self):
        carti = {}
        self.__cntrl = carte_controller(carti, 1, "teste_carti_unitest.txt")
        self.golesteFisier('teste_carti_unitest.txt')
        self.__cntrl.cmd3('1', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover')
        
    def golesteFisier(self, cale):
        with open(cale, "w") as f:
            f.write("")
            
    def tearDown(self):
        pass
    
    def test_Creare(self):
        self.assertTrue(len(self.__cntrl.cmd1()) == 1)
        self.assertRaises(ValueError, self.__cntrl.cmd3, '', '' ,'', '')
        self.assertRaises(ValueError, self.__cntrl.cmd3, '1', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu')
        
    def test_Cautare(self):
        self.assertTrue(self.__cntrl.cmd9('1').getIdCrt() == '1' and self.__cntrl.cmd9('1').getTitluCrt() == 'Ugly Love' and self.__cntrl.cmd9('1').getDescCrt() == 'O carte despre iubire', self.__cntrl.cmd9('1').getAutorCrt() == 'Colleen Hoover')
        self.assertRaises(ValueError, self.__cntrl.cmd9,'2')
        
        
    def test_Modificare(self):
        self.__cntrl.cmd7('1', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu')
        self.assertTrue(self.__cntrl.cmd9('1').getIdCrt() == '1' and self.__cntrl.cmd9('1').getTitluCrt() == 'Enigma Otiliei' and self.__cntrl.cmd9('1').getDescCrt() == 'O carte despre maturizare', self.__cntrl.cmd9('1').getAutorCrt() == 'George Calinescu')
        self.assertRaises(ValueError, self.__cntrl.cmd7, '2', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover')
        
    def test_Generare(self):
        self.assertRaises(ValueError, self.__cntrl.cmd11, -1)
        self.__cntrl.cmd11(3)
        self.assertTrue(len(self.__cntrl.cmd1()) == 4)
if __name__ == '__main__':
    unittest.main()
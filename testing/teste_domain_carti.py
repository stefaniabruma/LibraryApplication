'''
Created on 20 dec. 2022

@author: stefa
'''
import unittest
from carte import carte


class TestCaseDomainCarti(unittest.TestCase):
    '''
    un nou tip de data pentru testele domeniului de carti
    '''
    def setUp(self):
        self.__crt = carte('1', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover')
    
    def teste_getteri(self):
        self.assertEqual(self.__crt.getIdCrt(), '1')
        self.assertEqual(self.__crt.getTitluCrt(), 'Ugly Love')
        self.assertEqual(self.__crt.getDescCrt(), 'O carte despre iubire')
        self.assertEqual(self.__crt.getAutorCrt(), 'Colleen Hoover')

if __name__ == '__main__':
    unittest.main()   
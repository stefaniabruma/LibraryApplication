'''
Created on 20 dec. 2022

@author: stefa
'''
import unittest
from client import client

class TestCaseDomainClienti(unittest.TestCase):
    '''
    un nou tip de data pentru testele domeniului de clienti
    '''
    def setUp(self):
        self.__clt = client('1', 'Asaftei Stefan', '12032000887765')
    
    def teste_getteri(self):
        self.assertEqual(self.__clt.getIdClt(), '1')
        self.assertEqual(self.__clt.getNumeClt(), 'Asaftei Stefan')
        self.assertEqual(self.__clt.getCnpClt(), '12032000887765')
        
    def teste_duplicatedCNP(self):
        self.assertTrue(self.__clt.__eqcnp__(client('2', 'Asfatei Stefan', '12032000887765')))

if __name__ == '__main__':
    unittest.main()
'''
Created on 20 dec. 2022

@author: stefa
'''
import unittest
from inchiriere import inchiriere
from client import client
from carte import carte

class TestCaseDomainInchirieri(unittest.TestCase):
    '''
    un nou tip de data pentru testele domeniului de inchireri
    '''
    def setUp(self):
        self.__inc = inchiriere(client('1', 'Asaftei Stefan', '12032000657849'), carte('11', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover'))
    
    def teste_getteri(self):
        self.assertEqual(self.__inc.getCltInc(), client('1', 'Asaftei Stefan', '12032000657849'))
        self.assertEqual(self.__inc.getCrtInc(), carte('11', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover'))
    
if __name__ == '__main__':
    unittest.main()
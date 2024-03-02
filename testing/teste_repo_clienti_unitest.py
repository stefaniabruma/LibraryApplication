'''
Created on 20 dec. 2022

@author: stefa
'''
import unittest
from repository.repository_clienti import repo_clt
from client import client
from validator.validator_client import validator_clt
from repository.file_repo_clienti import file_repo_clt

class TestCaseRepositoryClientiFaraFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele repo-ului de clienti fara fisiere
    '''
    def setUp(self):
        clienti = {}
        self.__repo = repo_clt(clienti)
        
        clt = client('1', 'Asaftei Stefan', '12032000665898')
        self.__repo.adauga_client(clt)
        clt = client('2', 'Taranu Robert', '04061999556335')
        self.__repo.adauga_client(clt)
        clt = client('', '', '32cd')
        self.__validator = validator_clt(clt)
        
    def teste_adaugareClient(self):
        self.assertEqual(self.__repo.lungimeListaClienti(), 2)
        clt = client('3', 'Vranciu Alexia', '23102001776389')
        self.__repo.adauga_client(clt)
        self.assertEqual(self.__repo.lungimeListaClienti(), 3)
    
    def teste_verificareDuplicatedID(self):
        clt = client('1', 'Vranciu Alexia', '23102001776389')
        self.assertRaises(ValueError, self.__repo.verificaIDclt, clt)
    
    def teste_verificaDuplicatedCNP(self):
        clt = client('4', 'Vranciu Alexia', '04061999556335')
        self.assertRaises(ValueError, self.__repo.verificaCNPclt, clt)
        
    def teste_Validator(self):
        self.assertRaises(ValueError, self.__validator.valideaza_clt)
    
    def teste_getAll(self):
        self.assertEqual(len(self.__repo.getAll()), 2)
    
    def teste_stergere(self):
        self.__repo.stergeCltDupaID('1')
        self.assertEqual(self.__repo.lungimeListaClienti(), 1)
        self.assertRaises(ValueError, self.__repo.stergeCltDupaID, '3')
    
    def teste_Cautare(self):
        self.assertTrue(self.__repo.cautaCltDupaID('1').getIdClt() == '1' and self.__repo.cautaCltDupaID('1').getNumeClt() == 'Asaftei Stefan' and  self.__repo.cautaCltDupaID('1').getCnpClt() == '12032000665898')
        self.assertRaises(ValueError, self.__repo.cautaCltDupaID, '3')
        
    def teste_Modficare(self):
        self.__repo.modificaCltDupaID('1', 'Vranciu Alexia', '23102001776389')
        self.assertTrue(self.__repo.cautaCltDupaID('1').getIdClt() == '1' and self.__repo.cautaCltDupaID('1').getNumeClt() == 'Vranciu Alexia' and self.__repo.cautaCltDupaID('1').getCnpClt() == '23102001776389')
        self.assertRaises(ValueError, self.__repo.modificaCltDupaID, '3', 'Nume', '123')
        self.assertRaises(ValueError, self.__repo.modificaCltDupaID, '1', '', '')

class TestCaseRepositoryClientiCuFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele repo-ului de clienti cu fisiere
    '''
    def setUp(self):
        self.golesteFisier('teste_clienti_unitest.txt')
        clienti = {}
        self.__repo = file_repo_clt(clienti, 'teste_clienti_unitest.txt')
        
        clt = client('1', 'Asaftei Stefan', '12032000665898')
        self.__repo.adauga_client(clt)
        clt = client('2', 'Taranu Robert', '04061999556335')
        self.__repo.adauga_client(clt)
        clt = client('', '', '32cd')
        self.__validator = validator_clt(clt)
        
    def golesteFisier(self, cale):
        with open(cale, "w") as f:
            f.write("")
       
    def teste_adaugareClient(self):
        self.assertEqual(self.__repo.lungimeListaClienti(), 2)
        clt = client('3', 'Vranciu Alexia', '23102001776389')
        self.__repo.adauga_client(clt)
        self.assertEqual(self.__repo.lungimeListaClienti(), 3)
    
    def teste_verificareDuplicatedID(self):
        clt = client('1', 'Vranciu Alexia', '23102001776389')
        self.assertRaises(ValueError, self.__repo.verificaIDclt, clt)
    
    def teste_verificaDuplicatedCNP(self):
        clt = client('4', 'Vranciu Alexia', '04061999556335')
        self.assertRaises(ValueError, self.__repo.verificaCNPclt, clt)
        
    def teste_Validator(self):
        self.assertRaises(ValueError, self.__validator.valideaza_clt)
    
    def teste_getAll(self):
        self.assertEqual(len(self.__repo.getAll()), 2)
    
    def teste_stergere(self):
        self.__repo.stergeCltDupaID('1')
        self.assertEqual(self.__repo.lungimeListaClienti(), 1)
        self.assertRaises(ValueError, self.__repo.stergeCltDupaID, '3')
    
    def teste_Cautare(self):
        self.assertTrue(self.__repo.cautaCltDupaID('1').getIdClt() == '1' and self.__repo.cautaCltDupaID('1').getNumeClt() == 'Asaftei Stefan' and  self.__repo.cautaCltDupaID('1').getCnpClt() == '12032000665898')
        self.assertRaises(ValueError, self.__repo.cautaCltDupaID, '3')
        
    def teste_Modficare(self):
        self.__repo.modificaCltDupaID('1', 'Vranciu Alexia', '23102001776389')
        self.assertTrue(self.__repo.cautaCltDupaID('1').getIdClt() == '1' and self.__repo.cautaCltDupaID('1').getNumeClt() == 'Vranciu Alexia' and self.__repo.cautaCltDupaID('1').getCnpClt() == '23102001776389')
        self.assertRaises(ValueError, self.__repo.modificaCltDupaID, '3', 'Nume', '123')
        self.assertRaises(ValueError, self.__repo.modificaCltDupaID, '1', '', '')


if __name__ == '__main__':
    unittest.main()
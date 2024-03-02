'''
Created on 20 dec. 2022

@author: stefa
'''
import unittest
from repository.repository_inchirieri import repo_inc
from client import client
from carte import carte
from inchiriere import inchiriere
from repository.file_repo_inchirieri import file_repo_inc

class TestCaseRepositoryInchirieri(unittest.TestCase):
    '''
    un nou tip de data pentru repository-ul de inchirieri cu fisiere
    '''
    def setUp(self):
        incs = []
        self.__repo = repo_inc(incs)
        inc = inchiriere(client('1', 'Asaftei Stefan' , '12032000678898'), carte('11', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover'))
        self.__repo.adaugaInc(inc)
        inc = inchiriere(client('2', 'Taranu Robert', '04061999665773'), carte('12', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu'))
        self.__repo.adaugaInc(inc)
        
    def teste_adaugare(self):
        self.assertEqual(self.__repo.lungime(), 2)
        inc = inchiriere(client('1', 'Asaftei Stefan' , '12032000678898'), carte('13', 'Un barbat pe nume Ove', 'O carte despre un batran', 'Fredrick Backman'))
        self.__repo.adaugaInc(inc)
        self.assertEqual(self.__repo.lungime(), 3)
        
    def teste_verificareExistenta(self):
        inc = inchiriere(client('2', 'Taranu Robert', '04061999665773'), carte('11', 'Ugly Love','O carte despre iubire', 'Colleen Hoover'))
        self.assertRaises(ValueError, self.__repo.verificaExistenta, inc)
    
    def teste_stergeri(self):
        inc = inchiriere(client('1', 'Asaftei Stefan' , '12032000678898'), carte('11', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover'))
        self.__repo.stergeInc(inc)
        self.assertEqual(self.__repo.lungime(), 1)
        self.assertRaises(ValueError, self.__repo.stergeInc, inc)
    
    def teste_getAll(self):
        self.assertEqual(len(self.__repo.getAll()), 2)
        
class TestCaseRepositoryInchirieriCuFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele repo-ului de inchirieri cu fisiere
    '''
    def setUp(self):
        self.golesteFisier('teste_clienti_unitest.txt')
        incs = []
        self.__repo = file_repo_inc(incs, 'teste_clienti_unitest.txt')
        inc = inchiriere(client('1', 'Asaftei Stefan' , '12032000678898'), carte('11', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover'))
        self.__repo.adaugaInc(inc)
        inc = inchiriere(client('2', 'Taranu Robert', '04061999665773'), carte('12', 'Enigma Otiliei', 'O carte despre maturizare', 'George Calinescu'))
        self.__repo.adaugaInc(inc)
    
    def golesteFisier(self, cale):
        with open(cale, "w") as f:
            f.write("")
       
    def teste_adaugare(self):
        self.assertEqual(self.__repo.lungime(), 2)
        inc = inchiriere(client('1', 'Asaftei Stefan' , '12032000678898'), carte('13', 'Un barbat pe nume Ove', 'O carte despre un batran', 'Fredrick Backman'))
        self.__repo.adaugaInc(inc)
        self.assertEqual(self.__repo.lungime(), 3)
        
    def teste_verificareExistenta(self):
        inc = inchiriere(client('2', 'Taranu Robert', '04061999665773'), carte('11', 'Ugly Love','O carte despre iubire', 'Colleen Hoover'))
        self.assertRaises(ValueError, self.__repo.verificaExistenta, inc)
    
    def teste_stergeri(self):
        inc = inchiriere(client('1', 'Asaftei Stefan' , '12032000678898'), carte('11', 'Ugly Love', 'O carte despre iubire', 'Colleen Hoover'))
        self.__repo.stergeInc(inc)
        self.assertEqual(self.__repo.lungime(), 1)
        self.assertRaises(ValueError, self.__repo.stergeInc, inc)
    
    def teste_getAll(self):
        self.assertEqual(len(self.__repo.getAll()), 2)
    
if __name__ == '__main__':
    unittest.main()
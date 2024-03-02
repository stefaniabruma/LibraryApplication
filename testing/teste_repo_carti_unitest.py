'''
Created on 20 dec. 2022

@author: stefa
'''
import unittest
from repository.repository_carti import repo_crt
from carte import carte
from validator.validator_carte import validator_crt
from repository.file_repo_carti import file_repo_crt

class TestCaseRepositoryCartiFaraFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele repo-ului de carti fara fisiere
    '''
    def setUp(self):
        carti = {}
        self.__repo = repo_crt(carti)
        crt = carte('1','Ugly Love', 'O carte despre iubire', 'Colleen Hoover')
        self.__repo.adauga_carte(crt)
        crt = carte('2', 'Engima Otiliei', 'O carte despre mturizare', 'George Calinescu')
        self.__repo.adauga_carte(crt)
        crt = carte('', '', '', '')
        self.__validator = validator_crt(crt)
    
    def teste_adaugaCarte(self):
        self.assertEqual(self.__repo.lungimeListaCarti(), 2)
        crt = carte('3', 'Un barbat pe nume Ove', 'O carte despre un batran', 'Fredrick Backman')
        self.__repo.adauga_carte(crt)
        self.assertEqual(self.__repo.lungimeListaCarti(), 3)
    
    def teste_VerificareDuplicatedID(self):
        crt = carte('1', 'Un barbat pe nume Ove', 'O carte despre un batran', 'Fredrick Backman')
        self.assertRaises(ValueError, self.__repo.verificaIDcrt, crt)
    
    def teste_ValidatorCrt(self):
        self.assertRaises(ValueError, self.__validator.valideaza_crt)
    
    def teste_GetALL(self):
        self.assertEqual(len(self.__repo.getAll()), 2)
    
    def teste_Stergere(self):
        self.__repo.stergeCrtDupaID('1')
        self.assertEqual(self.__repo.lungimeListaCarti(), 1)
        self.assertRaises(ValueError, self.__repo.stergeCrtDupaID, '3')
    def teste_Cautare(self):
        self.assertTrue(self.__repo.cautaCrtDupaID('1').getIdCrt() == '1' and self.__repo.cautaCrtDupaID('1').getTitluCrt() == 'Ugly Love' and self.__repo.cautaCrtDupaID('1').getDescCrt() == 'O carte despre iubire' and self.__repo.cautaCrtDupaID('1').getAutorCrt() == 'Colleen Hoover') 
        self.assertRaises(ValueError, self.__repo.cautaCrtDupaID, '3')
        
    def teste_Modificare(self):
        self.__repo.modificaCrtDupaID('1', 'Acolo unde canta racii', 'O carte despre o fetita', 'Delia Owens') 
        self.assertTrue(self.__repo.cautaCrtDupaID('1').getIdCrt() == '1' and self.__repo.cautaCrtDupaID('1').getTitluCrt() == 'Acolo unde canta racii' and self.__repo.cautaCrtDupaID('1').getDescCrt() == 'O carte despre o fetita' and self.__repo.cautaCrtDupaID('1').getAutorCrt() == 'Delia Owens')
        self.assertRaises(ValueError, self.__repo.modificaCrtDupaID,'3', 'Titlu', 'Descriere', 'Autor')
        self.assertRaises(ValueError, self.__repo.modificaCrtDupaID,'1', '', '', '')
    
class TestCaseRepositoryCartiCuFisiere(unittest.TestCase):
    '''
    un nou tip de data pentru testele repo-ului de carti cu fisiere
    '''
    def setUp(self):
        self.golesteFisier("teste_carti_unitest.txt")
        carti = {}
        self.__repo = file_repo_crt(carti, "teste_carti_unitest.txt")
        crt = carte('1','Ugly Love', 'O carte despre iubire', 'Colleen Hoover')
        self.__repo.adauga_carte(crt)
        crt = carte('2', 'Engima Otiliei', 'O carte despre mturizare', 'George Calinescu')
        self.__repo.adauga_carte(crt)
        crt = carte('', '', '', '')
        self.__validator = validator_crt(crt)
    
    def golesteFisier(self, cale):
        with open(cale, "w") as f:
            f.write("")
            
    def teste_adaugaCarte(self):
        self.assertEqual(self.__repo.lungimeListaCarti(), 2)
        crt = carte('3', 'Un barbat pe nume Ove', 'O carte despre un batran', 'Fredrick Backman')
        self.__repo.adauga_carte(crt)
        self.assertEqual(self.__repo.lungimeListaCarti(), 3)
    
    def teste_VerificareDuplicatedID(self):
        crt = carte('1', 'Un barbat pe nume Ove', 'O carte despre un batran', 'Fredrick Backman')
        self.assertRaises(ValueError, self.__repo.verificaIDcrt, crt)
    
    def teste_ValidatorCrt(self):
        self.assertRaises(ValueError, self.__validator.valideaza_crt)
    
    def teste_GetALL(self):
        self.assertEqual(len(self.__repo.getAll()), 2)
    
    def teste_Stergere(self):
        self.__repo.stergeCrtDupaID('1')
        self.assertEqual(self.__repo.lungimeListaCarti(), 1)
        self.assertRaises(ValueError, self.__repo.stergeCrtDupaID, '3')
    def teste_Cautare(self):
        self.assertTrue(self.__repo.cautaCrtDupaID('1').getIdCrt() == '1' and self.__repo.cautaCrtDupaID('1').getTitluCrt() == 'Ugly Love' and self.__repo.cautaCrtDupaID('1').getDescCrt() == 'O carte despre iubire' and self.__repo.cautaCrtDupaID('1').getAutorCrt() == 'Colleen Hoover') 
        self.assertRaises(ValueError, self.__repo.cautaCrtDupaID, '3')
        
    def teste_Modificare(self):
        self.__repo.modificaCrtDupaID('1', 'Acolo unde canta racii', 'O carte despre o fetita', 'Delia Owens') 
        self.assertTrue(self.__repo.cautaCrtDupaID('1').getIdCrt() == '1' and self.__repo.cautaCrtDupaID('1').getTitluCrt() == 'Acolo unde canta racii' and self.__repo.cautaCrtDupaID('1').getDescCrt() == 'O carte despre o fetita' and self.__repo.cautaCrtDupaID('1').getAutorCrt() == 'Delia Owens')
        self.assertRaises(ValueError, self.__repo.modificaCrtDupaID,'3', 'Titlu', 'Descriere', 'Autor')
        self.assertRaises(ValueError, self.__repo.modificaCrtDupaID,'1', '', '', '')
    
if __name__ == '__main__':
    unittest.main()
'''
Created on 12 nov. 2022

@author: stefa
'''
from presentation.ui import userInterface
from teste import ruleaza_teste
from business.service_carti import carte_controller
from business.service_clienti import client_controller
from business.service_inchirieri import inc_controller
from teste_controller_carti_unitest import TestCaseCartiControllerCuFisiere, TestCaseCartiControllerFaraFisiere
from teste_controller_clienti_unitest import TestCaseClientiControllerCuFisiere, TestCaseClientiControllerFaraFisiere
from teste_controller_inchirieri_unitest import TestCaseControllerInchirieri, TestCaseControllerInchirieriCuFisiere
from teste_domain_carti import TestCaseDomainCarti
from teste_domain_clienti import TestCaseDomainClienti
from teste_domain_inchirieri import TestCaseDomainInchirieri
from teste_repo_carti_unitest import TestCaseRepositoryCartiCuFisiere, TestCaseRepositoryCartiFaraFisiere
from teste_repo_clienti_unitest import TestCaseRepositoryClientiFaraFisiere, TestCaseRepositoryClientiFaraFisiere
from teste_repo_inchirieri import TestCaseRepositoryInchirieri, TestCaseRepositoryInchirieriCuFisiere
from teste_service_inchirieri_unitest import TestCaseServiceInchirieriCuFisiere, TestCaseServiceInchirieriFaraFisiere

if __name__ == '__main__':
    # teste = ruleaza_teste()
    # teste.ruleaza_toate_testele()
    
    carti = {}
    clienti = {}
    inchirieri = []
    
    ui = userInterface()
    ui.printDecision()
    dec = ui.getDecizie()
    executacrt = carte_controller(carti, dec, "carti.txt")
    executaclt = client_controller(clienti, dec, "clienti.txt")
    executainc = inc_controller(carti, clienti, inchirieri, dec, "carti.txt", "clienti.txt", "inchirieri.txt")
    ui.run(executacrt, executaclt, executainc)

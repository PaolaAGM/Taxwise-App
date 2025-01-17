import sys
import os
sys.path.append(f"{os.path.dirname(os.path.dirname(__file__))}")

from dao.ITaxBrack_dao import ITaxBrackDao as DAOTax
from controllers.TaxCalculator import TaxCalculator as calculator



class UI:
    def __init__(self):
        
        self.DAO = DAOTax()
        self.calculator = calculator(self.DAO)
        self.run()

    def run(self):

        print(" Bienvenue au TAXAWISE ")

        while True:
            ans = input("Étes vous: \n 1. Contribuable \n 2. Agent fiscal\n Entrer l'option 1 ou 2: ")
            if ans.isnumeric() and int(ans) == 1:
                while True:
                    print("NOTE: TaxWise est juste pour les personne qui vivent au Canada")
                    
                    amount=input("Entrez votre revenue annuel: ")
                    if amount.isnumeric() == False:
                        print("Veillez selectionner une option valide (1 ou 2).")
                        continue
                    province = input(" Vous residez à quelle provice: \n 1. Québec  \n 2. Ontario\n Entrer l'option 1 ou 2: ")
                    if province.isnumeric() and int(province) == 1:
                        # taxFederal = self.calculator.CalculateTax(int(amount), "Federal")
                        taxFederal, taxProvince = self.calculator.CalculateTax(int(amount), "Québec")
                        print(f"Le montant total à payer est: \nTax Federal -> {taxFederal}\nTax Province -> {taxProvince}")
                        break
                    elif province.isnumeric() and int(province) == 2:
                        # taxFederal = self.calculator.CalculateTax(int(amount), "Federal")
                        taxFederal, taxProvince = self.calculator.CalculateTax(int(amount), "Ontario")
                        print(f"Le montant total à payer est: \nTax Federal -> {taxFederal}\nTax Province -> {taxProvince}")
                        break
                    else:
                        print("Veillez selectionner une option valide (1 ou 2).")
                break
            elif ans.isnumeric() and int(ans) == 2:
                print("Vous aimeriez avoir accès à une liste complète des tranches d'imposition de quelle province: ")
                choixProvince = input(" 1. Québec  \n 2. Ontario\n 3. Canada \n Entrer l'option 1, 2, ou 3: ")
                if choixProvince.isnumeric() and int(choixProvince) == 1:
                        province = self.DAO.findAllBrackets("Québec")
                        print("La liste des tranches d'imposition de la province de Québec est:")
                        for i, bracket in enumerate(province):
                            print(f"{i+1} Min: {bracket.getMin()} Max: {bracket.getMax()} Tax Rate: {bracket.getRate()}")
                        break
                elif choixProvince.isnumeric() and int(choixProvince) == 2:
                        province = self.DAO.findAllBrackets("Ontario")
                        print("La liste des tranches d'imposition de la province d'Ontario est:")
                        for i, bracket in enumerate(province):
                            print(f"{i+1} Min: {bracket.getMin()} Max: {bracket.getMax()} Tax Rate: {bracket.getRate()}")
                        break
                elif choixProvince.isnumeric() and int(choixProvince) == 3:
                        province = self.DAO.findAllBrackets("Federal")
                        print("La liste des tranches d'imposition Federal:")
                        for i, bracket in enumerate(province):
                            print(f"{i+1} Min: {bracket.getMin()} Max: {bracket.getMax()} Tax Rate: {bracket.getRate()}")
                        break                                    
                else:
                        print("Veillez selectionner une option valide (1, 2 ou 3).")
                break
            else:
                print("Veillez selectionner une option valide (1 ou 2).")


main = UI()

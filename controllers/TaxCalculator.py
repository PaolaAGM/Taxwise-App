from models.TaxAuthority import TaxAuthority as authority

class TaxCalculator:

    def __init__(self, dao):
        self.__dao = dao


    def CalculateTax(self, amount:float, authority: str):
       # tax_free_threshold = next((auth for auth in self.__dao.__repository.getAuthorities() if auth.getLabel() == authority), None)
        taxFreeThresHold = self.__dao.findTaxFreeThreshold(authority)
        amount = amount - taxFreeThresHold
        bracketsProvince = self.__dao.findAllBracketsProvince(authority, amount)
        bracketsFederal = self.__dao.findAllBracketsProvince("Federal", amount)
        taxProvince = 0 
        taxFederal = 0
        for bracket in bracketsProvince:
            taxProvince += (bracket.getMax() - bracket.getMin()) * bracket.getRate()
        for bracket in bracketsFederal:
            taxFederal += (bracket.getMax() - bracket.getMin()) * bracket.getRate()

        return taxFederal, taxProvince







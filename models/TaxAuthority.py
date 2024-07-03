from models.TaxBracket import TaxBracket

class TaxAuthority:

    def __init__(self, label:str, tax_free_threshold:float):

        self.__label = label
        self.__taxFreeThreshold = tax_free_threshold
        self.__tax_brackets = []

    def getLabel(self):
        return self.__label
    
    def getTaxFree_threshold(self):
        return self.__taxFreeThreshold
    
    def getTaxBrackets(self):
        return self.__tax_brackets
    
    def setTaxBrackets(self,brackets):
        self.__tax_brackets = brackets


    





        

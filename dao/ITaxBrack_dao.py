from models.TaxAuthority import TaxAuthority as authority
from models.TaxBracket  import TaxBracket as bracket
from data.inMemoryRepository import inMemoryRepository as repository
from typing import List
import sys



class ITaxBrackDao():

    def __init__(self):
        self.__repository = repository()
     
    def findAllBrackets(self, authority:str):
        for auth in self.__repository.getAuthorities():
            if auth.getLabel() == authority:
                return auth.getTaxBrackets()
            
    def  findTaxFreeThreshold(self, authority:str):
        for auth in self.__repository.getAuthorities():
            if auth.getLabel() == authority:
                return auth.getTaxFree_threshold()
        return None
    
    def findAllBracketsProvince(self, authority:str, amount:float) -> List[bracket]:
        applicableBrackets = []
        for auth in self.__repository.getAuthorities():
            if auth.getLabel() == authority:
                applicableBrackets = self.findBracketAuthority(auth.getTaxBrackets(), amount)
                break
        return applicableBrackets
        
   
    def findBracketAuthority(self, authorityBrackets, amount):
        applicableBrackets = []
        for bracket in authorityBrackets:
            if amount < bracket.getMax():
                bracket.setMax(amount)
                applicableBrackets.append(bracket)
                break
            else:
                applicableBrackets.append(bracket)
        
        return applicableBrackets

        
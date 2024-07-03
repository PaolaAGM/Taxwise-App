class TaxBracket:

    def __init__(self, min:float, max:float, tax_rate:float ):

        self.__min = min
        self.__max = max
        self.__taxRate = tax_rate

    def getMin(self):
        return self.__min

    def getMax(self):
        return self.__max

    def setMax(self,income):
        self.__max=income

    def getRate(self):
        return self.__taxRate


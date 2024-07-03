from models.TaxAuthority import TaxAuthority as authority
from models.TaxBracket import TaxBracket as bracket


class inMemoryRepository:

    def __init__ (self):

        self.__authorities = []

        federal = authority("Federal", 14398)
        ontario = authority("Ontario", 17000)
        quebec = authority("Québec", 53357)

        self.__authorities.extend([federal,quebec,ontario])

        self.data_tax_canada()
        self.data_tax_quebec()
        self.data_tax_ontario()

    def getAuthorities(self):
        return self.__authorities

    def data_tax_canada(self):
        self.__authorities[0].setTaxBrackets([
            bracket(0, 53358,0.15),
            bracket(53359, 106717, 0.205),
            bracket(106718, 165430, 0.26),
            bracket(165431, 235675, 0.29),
            bracket(235676, float('inf'), 0.33)
        ])

    def data_tax_quebec(self):
        self.__authorities[1].setTaxBrackets([
            bracket(0, 51780, 0.14),
            bracket(51781, 103545, 0.19),
            bracket(103546, 126000, 0.24),
            bracket(126001, float('inf'), 0.255),
        ])

    def data_tax_ontario(self):
        self.__authorities[2].setTaxBrackets([
            bracket(0, 51446, 0.05),
            bracket(51447, 102894, 0.095),
            bracket(102895, 150000,0.111),
            bracket(150001 , 220000,0.121),
            bracket(220000, float('inf'), 0.136)
        ])







    

        
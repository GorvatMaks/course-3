#створи клас Converter
#запити 2 числа - курс та суму
#створи об'єкт класу Converter
#реалізуй вибір виду обміну

class Converter:
    def __init__(self,kyrs,money):
        self.kyrsdolar = kyrs
        self.kyrsmoney = money
    
    def uah_to_usd(self):
        resalt = self.kyrsmoney/self.kyrsdolar 
        return resalt
    
    def usd_to_uah(self):
        resalt = self.kyrsdolar/self.kyrsmoney 
        return resalt

kyrs = int(input("Долар "))
money = int(input("Сума "))

Convekt = Converter(kyrs,money)

vubir = int(input("1-долар у грн/ 2-грн у долар 2"))
if vubir ==1:
    print(Convekt.usd_to_uah())
else:
    print(Convekt.uah_to_usd())
"""Question - Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type. """


class Flower:
    def __init__(self,name,n_petals,price):
        self._name=name
        self.n_petals=n_petals
        self._price=price
    
    def get_name(self):
        return self._name
    
    def get_n_petals(self):
        return self._n_petals
    
    def get_price(self):
        return self._price
if __name__ =="__main__":
     flower=Flower("sentosa",4,500)
     print(flower.get_name())

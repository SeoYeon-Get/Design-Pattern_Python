from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta): #다이어그램(p.484) AbstractFactory 
    
    @abstractmethod
    def createVegPizza(self): #createProduct()
        pass
    
    @abstractmethod
    def createNonVegPizza(self): #createAnotherProduct()
        pass

class IndianPizzaFactory(PizzaFactory): #ConcreteFactory1
    
    def createVegPizza(self):
        return DeluxVeggiePizza()
    
    def createNonVegPizza(self):
        return ChickenPizza()

class USPizzaFactory(PizzaFactory): #ConcreteFactory2
    
    def createVegPizza(self):
        return MexicanVegPizza()
    
    def createNonVegPizza(self):
        return HamPizza()

class VegPizza(metaclass=ABCMeta):  #AbstractProduct1
    
    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegPizza(metaclass=ABCMeta): #AbstractProduct2
    
    @abstractmethod
    def serve(self, VegPizza):
        pass

class DeluxVeggiePizza(VegPizza):  #ConcreteProduct
    
    def prepare(self):
        print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza): #ConcreteProduct
    
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):#ConcreteProduct
    
    def prepare(self):
        print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):#ConcreteProduct
    
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)

class PizzaStore: #Client 이런 객체가 여러개 가능.
    
    def __init__(self):
        pass
    
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()
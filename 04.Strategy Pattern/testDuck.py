#자바 Strategy Patternd의 예시 코드를 파이썬으로 코딩하였음.

import abc 

class Duck(metaclass=abc.ABCMeta):
    #__metaclass__ = ABCmeta
    
    def __init__(self):
       self.fly_behavior = FlyBehavior

    @abc.abstractmethod
    def display(self):
        pass
    
    def performFly(self):
        self.fly_behavior.fly()

    def setFlyBehavior(self, fb):
        self.fly_behavior = fb
 
class MallardDuck(Duck):
  def __init__ (self):
    self.fly_behavior = FlyNoway()    
 
  def display(self):
    print("Mallard duck")
 
 
class FlyBehavior(metaclass = abc.ABCMeta):
  @abc.abstractmethod
  def fly(self):
    pass
 
class FlyWithWings(FlyBehavior):
  def fly(self):
    print("Fly with wings")
 
class FlyNoway(FlyBehavior):
  def fly(self):
    print("Fly no way")


def main():
    mallad_duck = MallardDuck()
        
    print("### MALLAD DUCK ###")
    mallad_duck.display()
    mallad_duck.performFly()


    mallad_duck1 = MallardDuck()
        
    print("### MALLAD DUCK ###")
    mallad_duck1.display()
    mallad_duck1.setFlyBehavior(FlyNoway())

if __name__ == '__main__':
    main()
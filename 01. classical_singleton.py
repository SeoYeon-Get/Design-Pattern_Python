class Singleton(object):
     
    def __new__(cls):
       if not hasattr(cls, 'instance'):
         cls.instance = super(Singleton, cls).__new__(cls) # __new__ 메서드를 오버라이드(재정의)하여 객체 생성을 제어함
       return cls.instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)

# __new__ 메서드 : 인스턴스의 스토리지를 할당하는 메소드. __init__ 메소드를 호출함.
# __init__ 메소드는 생성자 메소드이지만, 인스턴스의 스토리지를 할당하지는 않음

class MyInt(type):
    
    def __call__(cls, *args, **kwargs):
        print("***** Here's My int *****", args, kwargs)        
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)

# 파이썬의 특별한 __call__ 메서드는 이미 존재하는 클래스에 대해 객체를 생성해야 할 때 호출됩니다. 
# 이 코드에서 우리가 int(4,5) 내에서 int 클래스를 인스턴스화할 때 MyInt 메타클래스의 __call__ 메소드가 호출됩니다. 
# 이는 메타클래스가 이제 객체의 인스턴스화를 제어한다는 것을 의미합니다. 
# 메타클래스는 클래스 생성 및 개체 인스턴스화에 대해 더 많은 제어 권한을 가지므로 싱글톤을 생성하는 데 사용할 수 있습니다. 

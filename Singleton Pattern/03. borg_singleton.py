class Borg:
    __shared_state = {"이름":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ += self.__shared_state
        pass

b = Borg()
b1 = Borg()
b1.x = 4

print("Borg Object 'b': ", b)  ## b and b1 are distinct objects
print("Borg Object 'b1': ", b1)
print("Object State 'b':", b.__dict__) ## b and b1 share same state
print("Object State 'b1':", b1.__dict__)

# #인스턴스 생성 내부동작
#  __new__, __init__, __call__
# 어떤 클래스의 인스턴스가 생성되는 과정을 이해하기 위해서는 __new__, __init__, __call__ 에 대해서 알아야한다.
# __new__ : 클래스 인스턴스를 생성 (메모리 할당)
# __init__ : 생성된 인스턴스 초기화
# __call__ : 인스턴스 실행
# 흔히들, __init__ 이 생성자라고 생각하는데, 아니다. 생성은 __new__에서 한다. __init__에서는 생성된 인스턴스를 초기화를 하는 것이다.
# 대부분의 경우, 인스턴스의 생성 그 자체에는 관여하지 않기 때문에 해당 메스드를 재사용하지 않는다. 
# 반면에, 개발자가 구현하고자하는 내용에 따라 초기화해줘야하는 변수들은 다양하므로 __init__ 메소드는 재사용하는 경우가 많다. 때문에, 
# __init__이 생성자라고 착각하는 경우가 많은데, 사실은 그렇지 않은 것이다.

# 그러니까, 굳이 순서를 따지자면, __new__ -> __init__ -> __call__ 순이 되는 것이다. *



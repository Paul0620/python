#설계도
class Car():
  def __init__(self, *args, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black") #key, value
    self.price = kwargs.get("price", "$20")

  #__str__의 재정의(override)
  def __str__(self):
    return f"Car with {self.wheels} wheels"

#extend(확장) or inherit(상속)
class Convertible(Car):

  #Car class의 init을 아래걸로 대체했기때문에 출력할 수 없음
  def __init__(self, **kwargs):
    #super함수를 통해 부모클래스 init을 가져옴
    super().__init__(**kwargs) 
    self.time = kwargs.get("time", 10)

  def take_off(self):
    return "taking off"

  def __str__(self):
    return f"Car with no roof"


class Something(Convertible):
  pass

#dir - class안에있는 모든것들을 리스트로 보여줌
#print(dir(Car))

#__str__ - method이며 class의 instance 출력, String으로 보고싶다
porche = Convertible(color="green", price="$40")
#print(porche.color, porche.price) #porche.__str__()을 자동으로 호출
print(porche.color)






"""
  #method - class안에 들어있는 function
  #파이썬은 모든 함수를 하나의 argument랑 함께 사용 - self
  def start(self): #보통 self로 선언 or 너맘대로 선언
    print(self.doors)
    print("I started")


#파이썬은 method를 호출할 때 그 method의 instance를 첫번째 argument로 사용
porche = Car() #Car이름의 class로 만든 Instance(결과물)
porche.color = "Red Sexy Red"
porche.start()
"""
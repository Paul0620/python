#funtion 만드는 방법(정의)
def say_hello():
  print("hello")
  print("bye")
  #들여쓰기를 잘해야함
#print("bye") def보다 안쪽에 들여쓰지 않는다면 에러발생

say_hello()
print("=============================")
print()

def say_hello(who):
  print("hello", who)

#위 say_hello(arg) arg를 who라고 선언했기 때문에 저 자리에 맞는 값을 넣어줘야함 
say_hello("Nicolas")
print("=============================")
print()


#arg를 두개 선언했으니 그에 맞게 함수를 불러올 때 arg 2개 선언해주어야함
def plus(a, b):
  print(a + b)

plus(2, 5)

#초기값을 설정해 준다면 하나의 arg만 넣어줘도 가능
def minus(a, b=0):
  print(a - b)

minus(2)
minus(2, 5)
print("=============================")
print()

def say_hello(name="anonymous"):
  print("hello", name)

say_hello()
say_hello("nico")
print("=============================")
print()

def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b
  print("qjdwd", True) #리턴 아래는 출력되지 않음 왜냐면 리턴을 하는 순간 거기서 funtion은 종료되어버림

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)
print("=============================")
print()

def minus(a, b):
  return a - b

result = minus(b=30, a=1)
print(result)

#변수를 포함시켜서 리턴해보기
def say_hello(name, age, are_from, fav_food):
  return f"Hello {name} you are {age} you are from {are_from} you like {fav_food}"

#arg순서 위치에 맞춰 return 문장에 값이 들어감
hello = say_hello(name="nico", age="12", fav_food="colombia", are_from="kimchi")
print(hello)

print("=============================")
print()

#type
a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None #파이썬에만 있음

#sequence type(열거형 타입)
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

#리스트의 순서는 0부터 시작하기 때문에 3번째 "Web"를 출력하고 싶다면 [2]로
#len()이란? 리스트의 길이(갯수)
#.append()란? 변수하나를 리스트에 추가
days.append("Sat")
days.reverse() #순서 거꾸로


#Tuple 튜플 - 아무도 변경할 수 없는 시퀀스(배열)을 만들고 싶을때 ()로 감싸서 만든다
days2 = ("Mon", "Tue", "Wed", "Thur", "Fri")

#Dicts 사전 - {}로 감싼다
nico = {
  "name" : "Nico",
  "age" : 29,
  "korean" : True,
  "fav_food" : ["Kimchi", "Sashimi"]
}
#print(nico["name"])
#print(nico)
#사전에 데이터 추가
nico["handsome"] = True
#print(nico)


#Functions print
"""
age = "18"
print(type(age))
#str로 입력한 18을 숫자 18로 변환
n_age = int(age)
print(type(n_age))

def say_hello():
  print("hello")
  print("bye")

say_hello()
"""

#Function Arguments - input
"""
def say_hello(who):
  print("hello", who)
#who를 채워주지 않으면 에러발생
say_hello("Nicolas")

def plus(a, b):
  print(a + b)

def minus(a, b=0): #b에 기본값 설정
  print(a - b)

plus(2, 5)
minus(2)
"""

#Returns
"""
def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b
  #return 아래에 무언가를 집어넣어도 이 함수는 return을 받는 순간 종료되기 때문에 그 뒤에 것들은 실행되지 않는다
  print("sdkskdjs")

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)
"""

#Keyworded Arguments
"""def plus(a, b):
  return a - b

result = plus(b=30, a=1)
print(result)"""

"""def say_hello(name, age, are_from, fav_food):
  return f"Hello {name} you are {age} you are from {are_from} you like {fav_food}"

hello = say_hello(age="12", name="nico", fav_food="kimchi", are_from="colombia")
print(hello)"""


#code Challenge
while True:
  a, b = list(input().split())
  try:
    a = int(a)
    b = int(b)
  except:
    print("숫자만 입력해 주세요!")
    continue

  cal = input()
  if cal == '+':
    print(a, cal, b, "=", a+b)
  elif cal == '-':
    print(a, cal, b, "=", a-b)
  elif cal == '*':
    print(a, cal, b, "=", a*b)
  elif cal == '/':
    print(a, cal, b, "=", a/b)
  elif cal == '**':
    print(a, cal, b, "=", a**b)
  elif cal == '%':
    print(a, cal, b, "=", a%b)
  else :
    print("올바른 수식을 넣어 주세요!")

#Conditionals part One
"""def plus(a, b):
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return None"""

#print(plus(12, 1.2))

#if else and or
"""def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you cant drink")
  elif age == 18:
    print("you are new to this")
  elif age > 20 and age < 25:
    print("you are still kind of young")
  else:
    print("enjoy your drink")

age_check(19)"""

#for in
days = {"Mon", "Tue", "Wed", "Thu", "Fri"}

"""for day in days:
  if day is "Wed":
    break
  else:
    print(day)"""

#문자도 배열이라 한글자씩 출력가능
"""for letter in "Nicolas":
  print(letter)
"""


#Modules
"""#import math
from math import ceil
from math import fsum as sexy_sum

#ceil 올림
print(ceil(1.2))

#fabs 절대값
print(sexy_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))"""




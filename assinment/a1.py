"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

#리스트안에 찾는 값이 있는지 확인
def is_on_list(days, day):
  return day in days
    
#리스트 안에 원하는 인덱스값 불러오기
def get_x(days, item):
  return days[item]

#리스트에 값 추가하기
def add_x(days, day):
  return days.append(day)

#리스트에서 값 제거하기
def remove_x(days, day):
  return days.remove(day)


# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you cant drink")
  elif age == 18 or age == 19:
    print("you are new to this!!")
  elif age > 20 and age < 25:
    print("you are still kind of young")
  else:
    print("enjoy your drink")

age_check(19)

print("================================================")
print()

days = ("Mon", "Tue", "Wed", "Thu", "Fri") #튜플 ()로 씌움

for day in days:
  if day is "Wed":
    break
  else:
    print(day)

for letter in "nicolas":
  print(letter)

print("================================================")
print()

#모듈
from math import fsum as sexy_sum

#print(ceil(1.2))
print(sexy_sum([1,2,3,4,5,6,7]))




import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
ccc_list = soup.find("table", {"class":"table table-bordered downloads tablesorter"})
arr = []
numname = {}
nations = {}
cnt = 0 
conde_one = None

print("Welcome to CurrencyConvert PRO 2000.\n")

#<td>태그제거하고 arr에 담기
for i in soup.find_all("td"):
  temp = str(i).lstrip("<td>").rstrip("</td>")
  arr.append(temp)

#번호 key, 나라이름이 value인 dict와 나라이름이 key, 통화, 코드, 넘버가 value인 dict 만들기
for i in range(0, len(arr), 4):
  value = []
  if arr[i+1] == "No universal currency":
    continue
  numname[cnt] = arr[i]
  value.append(arr[i])
  value.append(arr[i+1])
  value.append(arr[i+2])
  value.append(arr[i+3])
  nations[cnt] = value
  cnt += 1

#번호와 나라 리스트 출력
for j in numname.keys():
  print(f"# {j} {numname[j]}")
    
#가지고 있는 돈의 국가코드 찾기
while 1:
  try:
    print("\nWhere ar you from? Choose a country by number.")
    choice = int(input("#: "))
    if 0 <= choice <= 264:
      info = nations[choice]
      print(f"{info[0]}\n")
      code_one = info[2]
      break
    else:
      print("Choose a number from the list.")
      continue
  except:
    print("That wasn't a number.")
    continue

#환전 하고싶은 나라의 국가코드 찾기
while 1:   
  try:
    print("Now choose another country.")
    choice = int(input("#: "))
    if 0 <= choice <= 264:  
      info = nations[choice]
      print(f"{info[0]}\n")
      code_two = info[2]
      break
    else:
      print("Choose a number from the list.")
      continue
  except:
    print("That wasn't a number.\n")
    continue

#환전금액 계산 후 출력
while 1:
  try:
    print(f"\nHow many {code_one} do you want to convert to {code_two}?")
    money = float(input())
    target = f"https://wise.com/gb/currency-converter/{code_one}-to-{code_two}-rate?amount={money}"
    take = requests.get(target)
    soup = BeautifulSoup(take.text, "html.parser")
    currency = soup.find("span", {"class": "text-success"})
    temp = float(str(currency.string))
    calculator = money * temp
    cal_f = format_currency(calculator, code_two, locale="ko_KR")
    money_f = f"{money:0,.2f}"
    print(f"{code_one} {money_f} is {cal_f}")
    break
      
  except:
    print("That wasn't a number.")
    continue
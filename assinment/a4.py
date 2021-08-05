import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
ccc_list = soup.find("table", {"class":"table table-bordered downloads tablesorter"})
arr = []
numname = {}
nations = {}
cnt = 0 

print("Hello! Plase choose select a country by number:")

#<td>태그제거하고 arr에 담기
for i in soup.find_all("td"):
    temp = str(i).lstrip("<td>").rstrip("</td>")
    arr.append(temp)

#번호 key, 나라이름이 value인 dict와 번호 key, 나라이름, 통화, 코드, 넘버가 value인 dict 만들기
for i in range(0, len(arr), 4):
    value = []
    if arr[i+1] == "No universal currency":
        continue
    numname[cnt] = arr[i]
    value.append(arr[i+1])
    value.append(arr[i+2])
    value.append(arr[i+3])
    nations[arr[i]] = value
    cnt += 1

#번호와 나라 리스트 출력
for j in numname.keys():
    print(f"# {j} {numname[j]}")
    
#입력 값에 대한 검사
while 1:
    try:
        choice = int(input("#:"))
        if 0 <= choice <= 264:
            name = numname[choice]
            info = nations[name]
            print(f"The currency code is {info[1]}.")
            break
        else:
            print("Choose a number from the list.")
            continue
    except:
        print("That wasn't a number.")
        continue
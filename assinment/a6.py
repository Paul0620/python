import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


#메인페이지에서 기업 공고모음 목록 주소 가져오기
result = requests.get(alba_url)
soup = BeautifulSoup(result.text, "html.parser")
box = soup.find("div", {"id": "MainSuperBrand"})
co_links = []
company = []
main_info = {}

#메인 페이지 회사 주소
for href in box.find_all("a", {"class": "goodsBox-info"}):
  co_links.append(href.get("href"))
    
#메인 페이지 회사 이름
for co in box.find_all("span", {"class": "company"}):
  if "채용관" not in co.text:
    company.append(co.text)
        
#주소와 회사 이름 dict
for i in range(len(co_links)):
  value = []
  value.append(company[i])
  main_info[co_links[i]] = value

#co_links에서 주소 가져오기
for link in co_links:
  count = 0
  url = f"{link}"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")

  #공고 페이지 리스트 갯수
  for result in soup.find("tbody").find_all("tr"):
    if result.find("td", {"class": "local"}) in result:
      count += 1

  #공고 정보 리스트
  jobs = []
  for i in range(count):
    place = soup.find_all("td", {"class": "local"})[i].text
    place = place.replace(u"\xa0", u" ")
    title = soup.find_all("span", {"class": "company"})[i].text
    time = soup.find_all("td", {"class": "data"})[i].text
    pay = soup.find_all("td", {"class": "pay"})[i].text
    date = soup.find_all("td", {"class": "regDate last"})[i].text
    job = {
      "place": place,
      "title": title,
      "time": time,
      "pay": pay,
      "date": date
    }
    jobs.append(job)


    #파일 csv로 저장
    file = open(f"(주){main_info[link]}.csv", encoding="utf-8", mode="w") #파일생성
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
      writer.writerow(list(job.values()))

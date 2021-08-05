#파이썬 라이브러리 reqeusts, BeautifulSoup
#requests - 해당 url의 자료를 추출할 수 있는 라이브러리
#BeautifulSoup - HTML이나 XML에서 데이터를 추출하는 라이브러리 parser를 이용해 찾고자 하는 데이터의 위치를 찾아 내어 값을 추출하는


import requests
from bs4 import BeautifulSoup

LIMIT = 50
#주소에 대한 변수 선언
URL = f"https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"
#URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  #requests를 통해 원하는 url를 가져옴
  result = requests.get(URL)
  #BeautifulSoup를 이용하여 text형식으로 출력
  soup = BeautifulSoup(result.text, "html.parser")
  #div태그에 클래스 이름이 pagination인 자료를 찾아 담는다
  pagination = soup.find("div", {"class":"pagination"})

  #찾은 자료중 li태그를 사용하는 자료들을 찾아 담는다
  links = pagination.find_all('li')
  #pages 배열에 li로 찾은 자료중 span태크를 가지고 있는 자료들을 담는다
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string)) #태그를 제외한 문자를 숫자로 출력
  #print(pages[:-1]) 맨 뒤에서 바로 앞자료까지만 출력
  #print(pages[0:3]) #0번째부터 3번째까지 출력

  max_page = pages[-1] 
  
  return max_page

def extract_job(html):
  title = html.find("h2",{"class": "jobTitle"})
  title_anchor = title.find("span")
  if title_anchor is not None:
    title = title_anchor.string

  company = html.find("span", {"class": "companyName"})
  company_anchor = company.find("a")
  if company_anchor is not None:
    company = company_anchor.string
  else:
    company = company.string
  return {'title': title, 'company': company}


def extract_indeed_jobs(last_page):
  jobs = []

  #for page in range(last_page): #자동출력
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser") 
  results = soup.find_all("a", {"class": "tapItem"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs
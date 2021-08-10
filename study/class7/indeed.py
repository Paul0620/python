import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})
  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))
    max_page = pages[-1]
  return max_page


def extract_job(html):
  #회사 공고 제목
  jobTitle = html.find("h2", {"class": "jobTitle"})
  title = jobTitle.find("span").string
  if title == "new":
    title = jobTitle.find_all("span")[1].string
  #회사 이름, 위치, 링크주소
  company = html.find("span", {"class": "companyName"})
  if company != None:
    company = company.string
      
  company_location = html.find("div", {"class": "company_location"})
  location = company_location.find("div").string
  job_link = html['data-jk']
  
  return {
    'title': title, 
    'company': company, 
    'location': location,
    'link': f"https://kr.indeed.com/viewjob?jk={job_link}"
  }


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping Indeed: page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a", {"class": "resultWithShelf"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
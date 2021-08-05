import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

#게시물 정보 가져오기
def extract_job(html):
  title = html.find("span", {"class": "title"}).string
  company = html.find("span", {"class": "company"}).string
  link = html.find_all("a")[1].get("href")
  return {
    "title": title, 
    "company": company, 
    "link": f"https://weworkremotely.com/{link}"
  }

#페이지에 있는 모든 게시물 가져오기
def extract_jobs(url):
  jobs = []
  result = requests.get(url, headers = headers)
  soup = BeautifulSoup(result.text, "html.parser")
  section = soup.find_all("section", {"class": "jobs"})
  for sec in section:
    results = sec.find_all("li")
    for result in results:
      if result != sec.find("li", {"class": "view-all"}):
        job = extract_job(result)
        jobs.append(job)
  return jobs

#검색 대상 검색 리스트 가져와서 결과값 내보내기
def get_work_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_jobs(url)
  return jobs
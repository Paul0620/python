import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

#게시물 정보 가져오기
def extract_job(html):
  title = html.find("h2", {"itemprop": "title"}).string
  company = html.find("h3", {"itemprop": "name"}).string
  link = html.find("a", {"class": "preventLink"}).get("href")
  return {
    "title": title, 
    "company": company, 
    "link": f"https://remoteok.io{link}"
  }

#페이지에 있는 모든 게시물 가져오기
def extract_jobs(url):
  jobs = []
  result = requests.get(url, headers = headers)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("tr", {"class": "remoteok-original"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs

#검색 대상 검색 리스트 가져와서 결과값 내보내기
def get_remote_jobs(word):
  url = f"https://remoteok.io/remote-dev+{word}-jobs"
  jobs = extract_jobs(url)
  return jobs
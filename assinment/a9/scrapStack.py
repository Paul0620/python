import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

#페이지 수 계산
def get_last_page(url):
  result = requests.get(url, headers = headers)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  last_page = pages[-2].get_text()
  return int(last_page)

#게시물 정보 가져오기
def extract_job(html):
  title = html.find("a", {"class": "s-link"}).string
  if html.find("h3", {"class": "fc-black-700"}).find("span").string is not None:
    company = html.find("h3", {"class": "fc-black-700"}).find("span").string.strip()
  else:
    company = html.find("h3", {"class": "fc-black-700"}).find("span").text.split("\n")[0]
  link = html.find("a", {"class": "s-link"}).get("href")
  return {
    "title": title, 
    "company": company, 
    "link": f"https://stackoverflow.com/{link}"
  }

#페이지에 있는 모든 게시물 가져오기
def extract_jobs(last_page, url):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

#검색 대상 검색 리스트 가져와서 결과값 내보내기
def get_stack_jobs(word):
  url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs
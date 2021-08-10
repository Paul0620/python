import csv

def save_to_file(jobs):
  file = open("jobs.csv", encoding = "utf-8", mode="w") #파일 생성
  writer = csv.writer(file) #변수에 파일명 저장
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return
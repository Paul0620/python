import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w") #파일 생성
  writer = csv.writer(file) #변수에 파일명 저장
  writer.writerow(["Title", "Company", "Link"])
  for job in jobs:
    for job in job:
      writer.writerow(list(job.values()))
  return
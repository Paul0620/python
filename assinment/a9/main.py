from flask import Flask, render_template, request, redirect, send_file
from exporter import save_to_file
from scrapRemote import get_remote_jobs
from scrapStack import get_stack_jobs
from scrapWork import get_work_jobs

"""
These are the URLs that will give you remote jobs for the word 'python'
Good luck!
"""

#웹 프레임워크 선언
app = Flask("Scrapper")
#검색 자료를 담아줄 db선언
db = {}

#메인페이지
@app.route("/")
def home():
  return render_template("home.html")

#검색 후 링크 리스트 페이지
@app.route("/read")
def read():
  word = request.args.get("word")
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = [get_remote_jobs(word), get_stack_jobs(word), get_work_jobs(word)]
      #한번 검색한걸 또 오래걸려서 가져올 필요없게 DB에 담아두기
      db[word] = jobs 
  else:
    return redirect("/")
  #return에서 담은 word를 출력
  return render_template(
    "read.html", 
    searchingBy=word, 
    resultsNumber=len(jobs[0]+jobs[1]+jobs[2]),
    jobs = jobs
  )

#파일 csv 저장 
@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    if not word:
      #강제 예외처리 구문
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file(
      "jobs.csv",
      mimetype = 'csv', 
      as_attachment=True, 
      attachment_filename = 'jobs.csv'
    )
  except:
    return redirect("/")

#서버 구축
app.run(host = "0.0.0.0")
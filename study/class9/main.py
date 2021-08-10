from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

#앱을 만들기 위한 코드
app = Flask("SuperScrapper")

#fakeDB
db = {}

#메인에 보여줄 내용 출력
@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  #word 변수에 request로 입력한 값을 담음 
  word = request.args.get("word")
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      #한번 검색한걸 또 오래걸려서 가져올 필요없게 DB에 담아두기
      db[word] = jobs 
  else:
    return redirect("/")
  #return에서 담은 word를 출력
  return render_template(
    "report.html", 
    searchingBy=word, 
    resultsNumber=len(jobs),
    jobs = jobs
  )

"""
#위에서 실행시킨 주소 뒤에 /contact를 추가하면 출력
@app.route("/<username>")
#a = "hello" @은 바로 아래있는 함수만 찾음, 변수는 찾지 않음
def patato(username):
  return f"Hello {username} how are you doing"
"""

@app.route("/export")
def export():
  try:
    word =request.args.get("word")
    if not word:
      #강제 예외처리 구문
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")
  
#웹사이트에서 볼수있는 서버 구축
#Replit을 사용해서 주소설정을 0.0.0.0으로
app.run(host="0.0.0.0") 


import requests, re
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""
subreddits = [
  "javascript",
  "reactjs",
  "reactnative",
  "programming",
  "css",
  "golang",
  "flutter",
  "rust",
  "django"
]

app = Flask("DayEleven")

#메인 페이지
@app.route("/")
def home():
  return render_template("home.html", subreddits=subreddits)

#리스트 페이지
@app.route("/read")
def list():
  #체크한 단어 뽑아서 리스트로 정리
  sub = str(request.args.get).replace("<bound method TypeConversionDict.get of ImmutableMultiDict([(","").replace(", 'on'","").replace(")])>","").replace("(","").replace(")","").replace("'","")
  sub_list = []
  for i in sub.split(','):
    i = i.replace(" ","")
    sub_list.append(i)

  post = []
  #리스트로 만든 체크단어 url에 넣어 자료 가져오기
  for word in sub_list:
    url = f"https://www.reddit.com/r/{word}/top/?t=month"
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")

    #게시글 제목, 투표수, 링크 가져오고, 체크단어 딕셔너리로 모은 뒤 post에 리스트로 담기
    for i in soup.find_all("div", {"class": "_1oQyIsiPHYt6nx7VOmd1sz"}):   
      promoted = i.find("span", {"class": "_2oEYZXchPfHwcf9mTMGMg8 V0WjfoF5BV7_qbExmbmeR"})
      if promoted is None:
        title = i.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"}).string
        vote = i.find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"}).string
        if 'k' in vote:
          vote = int(re.sub(r'[^0-9]', '', vote)) * 1000
        else:
          vote = int(vote)
        if i.find("a", {"class": "SQnoC3ObvgnGjWt90zD9Z"}) is not None:
            link = i.find("a", {"class": "SQnoC3ObvgnGjWt90zD9Z"}).get("href")
        sub = f"{word}"
        post.append({"title": title, "vote": vote, "link": link, "sub": sub})
  
  post = sorted(post, key=lambda x:x['vote'], reverse=True)
  reddits = post
  return render_template(
    "read.html",
    sub_list = sub_list,
    reddits = reddits
  )

app.run(host="0.0.0.0")
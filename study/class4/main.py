import requests

indeed_resul = requests.get("https://www.indeed.com/jobs?q=python&limit50")

print(indeed_resul.text)
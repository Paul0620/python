import requests

print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check.(separated by comma)")

while True:
  url = list(input().split(','))

  for i in range(len(url)):
    url[i] = url[i].strip().lower()
    if url[i].find('.') != -1:
      if not url[i].startswith("http"):
        url[i] = "http://" + url[i]

  for j in url:
    if j.find('.') == -1:
      print(j + " is not valid URL.")
      continue 
    try:
      request = requests.get(j)
      if request.status_code == 200:
        print(j + " is up!")
        continue
    except:
      print(j + " is down!")
      continue

  check = 0  
  while(1):
    answer = input("Do you want to start over? y/n ")
    if answer == 'y':
      check = 1
      break
    elif answer == 'n':
      break
    else:
      print("That's not vaild answer")
      continue

  if check:
    continue
  else:
    break
    

"""
import os
import requests

def restart():
  answer = str(input("Do you want to start over? y/n ")).lower()
  if answer == "y" or answer =="n":
    if answer == "n":
        print("k. bye!")
        return
    elif answer == "y":
      main()
  else:
    print("That's not a valid answer")
    restart()


def main():
  os.system('clear')
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "is not a valid URL.")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        request = requests.get(url)
        if request.status_code == 200:
          print(url,"is up!")
        else:
          print(url, "is down!")
      except:
          print(url, "is down!")
  restart()


main()
"""

 
  




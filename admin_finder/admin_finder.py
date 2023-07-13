import requests

from termcolor import colored
print("""
   _       _           _           ___ _           _
  /_\   __| |_ __ ___ (_)_ __     / __(_)_ __   __| | ___ _ __
 //_\\ / _` | '_ ` _ \| | '_ \   / _\ | | '_ \ / _` |/ _ \ '__|
/  _  \ (_| | | | | | | | | | | / /   | | | | | (_| |  __/ |
\_/ \_/\__,_|_| |_| |_|_|_| |_| \/    |_|_| |_|\__,_|\___|_|
""")
url = input("Enter url : ")
pages = ['about','admin','login']
for i in pages:
  url2 = (f"{url}/{i}")
  req = requests.post(url2)
  a = req.status_code
  if a == 404:
    print(colored(f"Page not found >> {a} >>> {url2}",'red'))
  else:
    print(colored(f"Page found >> {url2}",'green'))

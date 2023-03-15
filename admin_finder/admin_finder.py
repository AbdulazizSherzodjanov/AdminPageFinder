import requests
# file1 = open('admin_pages.txt', 'r')
# Lines = file1.readlines()
from termcolor import colored
print("""
   _       _           _           ___ _           _
  /_\   __| |_ __ ___ (_)_ __     / __(_)_ __   __| | ___ _ __
 //_\\ / _` | '_ ` _ \| | '_ \   / _\ | | '_ \ / _` |/ _ \ '__|
/  _  \ (_| | | | | | | | | | | / /   | | | | | (_| |  __/ |
\_/ \_/\__,_|_| |_| |_|_|_| |_| \/    |_|_| |_|\__,_|\___|_|
""")
url = input("Urlni kiriting : ")
pagelar = ['about','admin','login']
for i in pagelar:
  url2 = (f"{url}/{i}")
  req = requests.post(url2)
  a = req.status_code
  if a == 404:
    print(colored(f"Sahifa topilmadi >> {a} >>> {url2}",'red'))
  else:
    print(colored(f"Sahifa topildi >> {url2}",'green'))

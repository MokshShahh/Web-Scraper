import requests
a=requests.get("https://quotes.toscrape.com/")
print(a.text)
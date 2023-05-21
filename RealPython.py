from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import mechanicalsoup

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)
htmlByte = page.read()
html = htmlByte.decode("utf-8")
obj = bs(html,"html.parser")
print(obj)
#print(obj.get_text())
imgtag = obj.find_all("img")
print(imgtag)


url = "http://olympus.realpython.org/login"
browser = mechanicalsoup.Browser()
webpage = browser.get(url)
loginHtml = webpage.soup

loginForm = loginHtml.select("form")[0]
print(loginForm)
username = loginForm.select("input")[0]["value"]= "zeus"
print(username)
password = loginForm.select("input")[1]["value"]= "ThunderDude"
print(password)
profilePage = browser.submit(loginForm,webpage.url)
print(profilePage.url)
#loginForm.select(0)
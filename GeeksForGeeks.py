import requests
from bs4 import BeautifulSoup

request = requests.get(
    "https://www.geeksforgeeks.org/python-programming-language/"
)


# print("-------------------Content>",request.content)
# print("-------------------encoding>",request.encoding)
# print("-------------------headers>",request.headers)
# print("-------------------request>",request)
# print("-------------------url,statuscode>",request.url,request.status_code)

prettierObj = BeautifulSoup(request.content,'html.parser')
# print(prettierObj.prettify())
print(prettierObj.title)
print(prettierObj.img)
print(prettierObj.img.name)
print(prettierObj.img.parent.name)


find = prettierObj.find_all("p")
print(type(find), len(find))
for i in find:
    print("---",i.text)

findById = prettierObj.find("div",id="secondary")
print(len(findById))
for id in findById:
    print(id.text)

findByHref = prettierObj.find_all("a")
print(len(findByHref))
for link in findByHref:
    print(link.get("href"))

imageList = list()
findImgAltSelect = prettierObj.select("img")
findImgAltFindAll = prettierObj.find_all("img")
print(len(findImgAltSelect),findImgAltSelect)
print(len(findImgAltFindAll),findImgAltFindAll)

for image in findImgAltSelect:
    imageList.append({"imageUrl" : image.get("src"),"imageAlt": image.get("alt")})

print(len(imageList),imageList)

URL = 'https://www.geeksforgeeks.org/page/1/'

req = requests.get(URL)
soup = BeautifulSoup(req.text, 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})

print(len(titles),titles)








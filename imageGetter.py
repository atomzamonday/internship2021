import requests
from bs4 import BeautifulSoup

url = "https://theinternship.io/"
data = requests.get(url)

soup = BeautifulSoup(data.text,'html.parser')
description = soup.find_all("span",{"class":"list-company"})
image = soup.find_all("img",{"class":"center-logos"})
descriptionList = []
logoPicList = []
result = []
logo_url  = []
n = 0
for i in description:
  descriptionList.append(i.text)

for i in image:
  logoPicList.append(i.get('src'))
  n = n+1

for i in range(n):
  result.append(logoPicList[i]+":"+descriptionList[i])
    
result.sort(key=len, reverse=True) 

for line in result:
  Type = line.split(":")
  logo_url.append(Type[0])

if __name__ == '__main__':
  print (*logo_url,sep="\n")
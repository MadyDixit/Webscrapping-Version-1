import bs4
import requests

x = input("Enter the Website(Not include https://):=")
x = "https://"+x
res = requests.get(x)
print("Entered Full Website is :", res.url)
soup = bs4.BeautifulSoup(res.text,'lxml')
for link in soup.find_all('a',href = True):
    print(link['href'])
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("humanist_homepage.htm"), features="html.parser")

print(soup.prettify())
links = soup.find_all('a')

for link in links:
    if 'Volume' in link.get_text():
        print(link)
    


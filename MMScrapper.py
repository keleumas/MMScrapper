import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.mm2.acidcave.net/bestiariusz.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'}

html_page = requests.get(url, headers=headers)
bestiariusz = BeautifulSoup(html_page.content, 'lxml')

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['DOS', 'Genesis', 'JSNES', 'Nazwa', 'PŻ', 'KP', 'OB', 'PR','ODP','Il','Atk','Spec'])

content=bestiariusz.find_all('tbody', class_='')[0].find_all('tr')

stworzenie=['0', '0' ,'0','0', '0' ,'0','0', '0' ,'0','0','0']
stworzenia=[]

for beast in range(0,2):    #Żeby zescrapować wszystko po prostu użyj w range len(content)
    for i in range(0,3):    #Źródła obrazków
        pic_src=content[beast].find_all('img')[i].attrs['src']
        stworzenie[i]=pic_src
    for i in range (3,11):
        remaining_data=content[beast].find_all('td')[i].get_text()
        stworzenie[i]=remaining_data

    stworzenia.append(stworzenie)
    csv_writer.writerow(stworzenia[beast])   

csv_file.close()
print('Koniec!')

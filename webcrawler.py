import requests
from bs4 import BeautifulSoup

def crawler(maxpage):
    page= 1
    while page <= maxpage:
        url= 'https://www.flipkart.com/search?q=mobiles+under+15000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_7_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_7_na_na_na&as-pos=4&as-type=RECENT&suggestionId=mobiles+under+15000&requestId=316ca22d-bdd6-4b94-83f6-95d56e9d877f&as-backfill=on' + str(page)
        data= requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
        plaintext= data.text
        soup= BeautifulSoup(plaintext , features= "html.parser")
        for link in soup.findAll('a', {'class': ''}):
            href= 'https://www.flipkart.com/' + link.get('href')
            title= link.string
            print(title)
            print(href)

            page +=1

crawler(2)




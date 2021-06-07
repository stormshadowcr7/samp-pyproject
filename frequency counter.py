import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    wordlist=[]
    source= requests.get(url, headers={'User-Agent':'Mozilla/5.0'}) .text
    soup= BeautifulSoup(source, features="html.parser")
    data= soup.findAll('a', {'class': '_4rR01T'})
    for revdata in data:
        content= revdata.string
        words= content.lower().split()
        for eachword in words:
            wordlist.append(eachword)
            print(eachword)


def dict(wordlist):
    count={}
    for words in wordlist:
        if words in count:
            count[words]= +1
        else:
            count[words]= 1
    for key,value in sorted(count.items, key= operator.itemgetter(1)):
        print(key,value)

start("https://www.flipkart.com/search?q=mobiles+under+15000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+15000&requestId=316ca22d-bdd6-4b94-83f6-95d56e9d877f&as-backfill=on")
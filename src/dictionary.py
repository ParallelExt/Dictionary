import requests
from bs4 import BeautifulSoup

URL = "https://www.merriam-webster.com"
DICT = "/browse/dictionary"

# Function to extract all the alphabets in the dictionary
def browseDict():
    page = requests.get(URL+DICT)
    soup = BeautifulSoup(page.content, 'html.parser')
    alphalinks = soup.find('div', class_='alphalinks').find_all('a')
    for alpha in alphalinks:
        link = URL + alpha.get('href')
        getPage(link)

def getPage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    getWords(page, soup)
    link = soup.find('div', class_='archives').find('li', class_='next').find('a').get('href')
    if link == 'javascript: void(0)':
        return
    getPage(URL + link)
    

def getWords(page, soup):
    words = soup.find('div', class_='entries').find_all('a')
    for word in words:
        print(word.text, end='\n')
        #link = URL + word.get('href')
        #getMeaning(link)

def getMeaning(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    

# Main Code

browseDict()
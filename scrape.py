import requests
from bs4 import BeautifulSoup
import time
import random
import json

PAGES_TO_SCRAPE = 4

def scrape(URL, pages):
    articles = {}
    for i in range(pages):
        seconds = random.randint(2,7)
        time.sleep(seconds)
        if i == 0:
            continue
        else:
            url = URL + '?p=' + str(i)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        index = 0
        for item in soup.findAll('a','storylink'):
            title = item.text
            link = item.get('href')

            articles[index] = {
                'title': title.lower(),
                'link': link
            }
            index += 1

    return articles

'''
This will go through each item in the dictionary and determine if any of the keywords
that were specified are contained in the strings. Stores it in file named 'output.txt'
'''
def parseItems(dict, words):
    articles = []
    for item in dict:
        if any(strings in dict[item]['title'] for strings in words):
            articles.append([dict[item]['title'],dict[item]['link']])

    output = open('output.json', 'w')

    for line in articles:
        try:
            title = str(line[0]) + '  '
            link = str(line[1])
            data = {title : link}
            json.dump(data, output)
        except:
            print("Exception Occurred")

'''
Method will parse the 'info.txt' file and store all the words 
that you would like to have scraped from hacker-news
'''
def parseFile(file):
    f = open(file, 'r')
    words = []
    for line in f:
        text = line.lower()
        words.append(text.rstrip())

    return words


def main():
    words = parseFile('info.txt')
    URL = 'https://news.ycombinator.com/news'
    newsArticles = scrape(URL,PAGES_TO_SCRAPE)
    parseItems(newsArticles, words)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:46:32 2020

@author: Owner
"""


from bs4 import BeautifulSoup
import requests

headers = {
    'authority': 'www.basketballireland.ie',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://www.basketballireland.ie/results/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'PHPSESSID=rpaa3nb7dvr1alv983ullspii5; _ga=GA1.2.114077442.1585943096; _gid=GA1.2.115454754.1585943096; _gat_gtag_UA_122572824_6=1',
}

def get_page_contents():
    response = requests.get('https://www.basketballireland.ie/league/144935/', headers=headers)
    return response.content

def convert_to_soup(content):
    return BeautifulSoup(content, features="html.parser")

def process_data(soup):
    print(soup.title.string) # gets rid of the html code at beginning
#to print the title as set in webpage name
    print(soup.h2.string) # prints the subheading without the html code 

    #print('Team, PLD, W, L, PF, PA, PD, PTS', end='') 
    colHeads = soup.find_all('th')

    for colHead in colHeads:
        print(colHead.text, end=',')

    cells = soup.find_all('td')

    for cell in cells:
        for content in cell.contents:
            value = str(content).strip().replace('\n', '')
            if len(value) == 0:
                print('"0"', end=',')
            elif value[0].lower() in 'abcdefghijklmnopqrstuvwxyz<':
                print('\n' + value, end=',')
            else:
                print('"' + value + '"', end=',')


def main():
    contents = get_page_contents()
    soup = convert_to_soup(contents)
    process_data(soup)


if __name__ == '__main__':
    main()


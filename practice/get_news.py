#!/usr/bin/python3
"""
    Just a routine practice: Get all the news from the 3 consecutive pages from https://news.python.sc/,
                             and then it puts all the news in a dictionary with its news_id as an identifier.
"""
import requests
from bs4 import BeautifulSoup
import json

pages = []
news = {}
news_id = 0
base_url = 'https://news.python.sc/?p={}'


# Parse and append all pages into a list
def get_all_pages():
    for page in range(0, 3):
        # Get each one of the pages from the base_url website.
        new_page = requests.get(base_url.format(page))
        # Parse each page to html before append to the list
        html_soup = BeautifulSoup(new_page.content, 'html.parser')
        pages.append(html_soup)
    return pages


# Get the title and url from all the news, and add into the news dictionary
def get_all_news(pages, news_id):
    for page in pages:
        news_title = page.find_all(class_='title')
        for current_news in news_title:
            news_id = news_id + 1
            title = current_news.find('a').get_text()
            href = current_news.find('a').get('href')
            news.update({news_id: [title, href]})
    return news


if __name__ == '__main__':
    all_pages = get_all_pages()
    all_news = get_all_news(all_pages, news_id)
    # Use json for a better presentation of the output
    print(json.dumps(all_news, sort_keys=True, indent=6))

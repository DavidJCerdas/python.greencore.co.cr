#!/usr/bin/python3
"""
    Just a routine practice: Get all the articles from 18 consecutive pages from https://enterprisersproject.com/,
                             and put them in a list, this to practice recursion and Web Scraping.
"""
import requests
from bs4 import BeautifulSoup
import json

pages = []
all_articles = []
page_number = 1
base_url = 'https://enterprisersproject.com/tags/devops?page={}/'


# Parse and append all pages into a list
def get_all_pages(page_number):
    # Parse each page to html before append to the list
    new_page = requests.get(base_url.format(page_number))
    print(f"Getting the data from page {page_number}...")
    if new_page.status_code == 200 and page_number < 18:
        # Parse each page to html before append to the list
        html_soup = BeautifulSoup(new_page.content, 'html.parser')
        pages.append(html_soup)
        get_all_pages(page_number + 1)
    return pages


# Get the title and url from all the news, and add into the news dictionary
def get_all_news(pages, all_articles):
    for page in pages:
        articles = page.find(class_='view-content').find_all('h2')
        for article in articles:
            title = article.get_text().replace('\n', '')
            url = article.find('a').get('href')
            all_articles.append((title, 'https://enterprisersproject.com/' + url))
    return all_articles


if __name__ == '__main__':
    all_pages = get_all_pages(page_number)
    all_news = get_all_news(all_pages, all_articles)
    # Use json for a better presentation of the output
    print(json.dumps(all_news, sort_keys=True, indent=3))

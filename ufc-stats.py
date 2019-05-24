from bs4 import BeautifulSoup
import lxml
import re
import requests

start_page = 'http://ufcstats.com/statistics/events/completed?page=all'
event_links = []

# Scrapes and parses the table on start_page. Saves links to a list.
def getLinks(url):
    response = requests.get(start_page)
    # Downloads entire HTML file.
    soup = BeautifulSoup(response.content, 'lxml')
    # Cuts out everything but the table.
    table = soup.findAll('table')[0]
    # Iterates through the table and appends all links to a list.
    for link in table.findAll('a', attrs={'href': re.compile("^http://")}):
        event_links.append(link.get('href'))
    # The first link in the table is for an event that hasn't happened yet.
    # Delete this item from our list.
    event_links.pop(0)

def main():
    getLinks(start_page)
    print(event_links)

if __name__ == "__main__":
    main()

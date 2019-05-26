from bs4 import BeautifulSoup
import lxml
import pandas as pd
import re
import requests

start_page = 'http://ufcstats.com/statistics/events/completed?page=all'
# List of links to each event TEST ONLY ONE
urls = ['http://ufcstats.com/event-details/6b8f28da9a483049']
# Scraped is stored stored here before going into data frame
keys = ['W/L','NAME','STR','TD','SUB','PASS','WEIGHTCLASS','METHOD','TECHNIQUE',
        'ROUND','TIME']
stats = []

# Scrapes all event links from start_page into list "url"
def getLinks(url):
    r = requests.get(url)
    # Downloads entire HTML file.
    soup = BeautifulSoup(r.content, 'lxml')
    # Cuts out everything but the table.
    table = soup.findAll('table')[0]
    # Iterates through the table and appends all links to a list.
    for link in table.findAll('a', attrs={'href': re.compile("^http://")}):
        urls.append(link.get('href'))
    # The first link in the table is for an event that hasn't happened yet.
    # Delete this item from our list.
    urls.pop(0)

# Opens an event link and scrapes each fight into dictionary "stats"
def getFightStats(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    rows = soup.find("tbody").findAll("tr")
    for row in rows:
        w = dict()
        l = dict()
        # Winner stats
        w['W/L'] = "W"
        w['NAME'] = row.findAll("td")[1].findAll("a")[0].text.strip()
        w['STR'] = row.findAll("td")[2].findAll("p")[0].text.strip()
        w['TD'] = row.findAll("td")[3].findAll("p")[0].text.strip()
        w['SUB'] = row.findAll("td")[4].findAll("p")[0].text.strip()
        w['PASS'] = row.findAll("td")[5].findAll("p")[0].text.strip()
        w['WEIGHTCLASS'] = row.findAll("td")[6].find("p").text.strip()
        w['METHOD'] = row.findAll("td")[7].findAll("p")[0].text.strip()
        w['TECHNIQUE'] = row.findAll("td")[7].findAll("p")[1].text.strip()
        w['ROUND'] = row.findAll("td")[8].find("p").text.strip()
        w['TIME'] = row.findAll("td")[9].find("p").text.strip()
        stats.append(w)
        # Loser stats
        l['W/L'] = "L"
        l['NAME'] = row.findAll("td")[1].findAll("a")[1].text.strip()
        l['STR'] = row.findAll("td")[2].findAll("p")[1].text.strip()
        l['TD'] = row.findAll("td")[3].findAll("p")[1].text.strip()
        l['SUB'] = row.findAll("td")[4].findAll("p")[1].text.strip()
        l['PASS'] = row.findAll("td")[5].findAll("p")[1].text.strip()
        l['WEIGHTCLASS'] = row.findAll("td")[6].find("p").text.strip()
        l['METHOD'] = row.findAll("td")[7].find("p").text.strip()
        l['TECHNIQUE'] = row.findAll("td")[7].findAll("p")[1].text.strip()
        l['ROUND'] = row.findAll("td")[8].find("p").text.strip()
        l['TIME'] = row.findAll("td")[9].find("p").text.strip()
        stats.append(l)

def main():
    for url in urls:
        getFightStats(url)
    # Append to dataframe
    df = pd.DataFrame(data = stats, columns = keys)
    print(df)


if __name__ == "__main__":
    main()

from bs4 import BeautifulSoup
from copy import deepcopy
import json
import lxml
import pandas as pd
import re
import requests
from time import sleep
from tqdm import tqdm

# List of all completed events
start_page = 'http://ufcstats.com/statistics/events/completed?page=all'
# Links of each individual event obtained from start_page
urls = []
# Data from each individual event is stored here as a dictionary
data = []

# Scrapes each event link from the start_page
def getLinks(url):
    r = requests.get(url)
    # Downloads HTML file
    soup = BeautifulSoup(r.content, 'lxml')
    # Focus is on the table
    table = soup.findAll('table')[0]
    # Iterates through the table and appends all links to a list
    for link in table.findAll('a', attrs={'href': re.compile("^http://")}):
        urls.append(link.get('href'))
    # The first link in the table is for an event that hasn't happened yet.
    # Delete this item from our list.
    urls.pop(0)

# Opens an event link and scrapes each fight into dictionary "data"
def getFightStats(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    # Focus on each row of the table, one fight, two fighters
    rows = soup.find("tbody").findAll("tr")
    # Focus on event metadata
    event_details = soup.findAll("li", "b-list__box-list-item")
    # Deletes tag that includes "Title:" from event metadata
    for event in event_details:
        event.i.decompose()

    # For each fight, gets data on both fighters and saves to dictionary "data"
    for row in rows:
        w = dict()
        l = dict()
        # Fight metadata
        w['EVENT'] = l['EVENT'] = soup.find("h2").text.strip()
        w['DATE'] = l['DATE'] = event_details[0].text.strip()
        w['LOCATION'] = l['LOCATION'] = event_details[1].text.strip()
        w['ATTENDANCE'] = l['ATTENDANCE'] = event_details[2].text.strip()
        # Winner stats
        w['WL'] = "W"
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
        data.append(w)
        # Loser stats
        l['WL'] = "L"
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
        data.append(l)

def main():
    getLinks(start_page)
    # Iterate though each event and get data
    # Sleep f(x) prevents accidental DoS attack
    for url in tqdm(urls):
        getFightStats(url)
        sleep(10)

    # Store data as JSON
    with open('eventstats.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()

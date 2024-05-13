import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

humanist_urls = ["https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/", "https://humanist.kdl.kcl.ac.uk/Archives/Current/"]
volume_dfs = []

for url in humanist_urls:
    print(f"Getting volumes from {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all('a')
    # loop through each volume link
    for link in links:
        if link['href'].endswith('.txt'):
            print(f"Getting volume from {url + link['href']}")
            page_soup = BeautifulSoup(requests.get(url + link['href']).text, "html.parser")
            text = page_soup.get_text()
            volume_link = url + link['href']
            dates = link['href'].split('.')[1]
            data_dict = {'volume_text': text, 'volume_link': volume_link, 'volume_dates': dates}
            volume_dfs.append(data_dict)

# Convert list of dictionaries into a DataFrame
humanist_vols = pd.DataFrame(volume_dfs)

# Randomly select 100 rows
sample_vols = humanist_vols.sample(100)
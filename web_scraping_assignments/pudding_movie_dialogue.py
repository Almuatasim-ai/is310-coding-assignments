from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# Open the file and parse it with BeautifulSoup
df = pd.read_csv('cleaned_pudding_data.csv')

# Find all the 'a' tags (links) in the document
links = df['link']

# Open the CSV file to write into
with open('pudding_dialogues.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['Link', 'Dialogue Text'])
    
    # Loop through the links
    for link in links:
        # If the link href contains "Dialogues", it's a dialogue link
       response = requests.get(link)
       if response.status_code != 200:
            continue
        # Construct the full URL by appending the href to the base URL
       dialogue_soup = BeautifulSoup(response.text, "html.parser")
       dialogue_soup.prettify()
       script = dialogue_soup.get_text()[:1000]
            # Write the link text and the parsed text to the CSV file
       writer.writerow([link,script])    
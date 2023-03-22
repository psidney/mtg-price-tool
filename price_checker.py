import requests
from bs4 import BeautifulSoup
import csv
import json
from datetime import datetime

f = open('set_details/list.txt','r')

sets = f.read().split('\n')

for set_name in sets:
    set_json = json.load(open('set_details/' + set_name + '.json','r'))
    set_url = set_json[0]['set_details']['mtggoldfish_uri']
    set_abbreviation = set_json[0]['set_details']['abbreviation']
    set_trims = set_json[0]['set_details']['trims']


    # make a GET request to the URL
    response = requests.get(set_url)
    #print(response.content)
    # parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    for table in soup.find_all('table'):
        print(table.get('class'))

    # find the table element containing the card data
    table = soup.find('table', class_='card-container-table')
    # print(table)
    # create a list to store the card data
    cards = []

    # loop through each row in the table
    i = 0
    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')

        if i!=0:
            card_trim = ""
            card_number = columns[0].text.strip() or 0
            card_name = columns[1].text.strip()
            if "Foil" in card_name:
                card_trim += "Foil"
                card_name = card_name.replace('Foil','')
            for card_trim_to_check in set_trims:
                if card_trim_to_check in card_name:
                    if card_trim == "":
                        card_trim += card_trim_to_check
                    else:
                        card_trim += " " + card_trim_to_check
                    card_name = card_name.replace(card_trim_to_check+" ","")
                    card_name = card_name.replace(card_trim_to_check,"")
            card_price = columns[4].text.strip().replace(' ','').replace('�','')[2:] or '0.00'
            card_price = '$' + card_price
            if card_trim == '':
                card_trim = "Regular"
            print(f"{card_number} - {card_name} ({card_trim})- {card_price}")
            cards.append([card_number, card_name, card_trim, card_price])
        i+=1
    # write the card data to a CSV file
    with open('daily_output/' + set_abbreviation + '_' + datetime.today().strftime('%Y-%m-%d') +  '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Number','Name', 'Price'])
        writer.writerows(cards)
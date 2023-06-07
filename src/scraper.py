from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import os
import json
import csv

class booking:
    def __init__(self, headers):
        # Constructor for the Booking class
        key = ['hotel_name','room_rate','price','location','checkin_date','checkout_date']
        self._url = 'https://www.booking.com/searchresults.it.html'
        self._headers = headers
        self.data = []
        print('Object booking created')
        
    
    def set(self, destination, checkin, checkout, num_adults, num_children, num_rooms=1,
            sb_travel_purpose='leisure', nflt='privacy_type%3D3', order='review_score_and_price'):
        # Set the parameters for the search
        self.destination = destination
        self.checkin = checkin
        self.checkout = checkout
        self.num_adults = num_adults
        self.num_rooms = num_rooms
        self.num_children = num_children
        self.sb_travel_purpose = sb_travel_purpose
        self.nflt = nflt
        self.order = order
        print('Parameters setted')


    def init_set(self):
        # Initialize the parameters for the HTTP request
        self.params = {
            'ss': self.destination,
            'checkin': self.checkin,
            'checkout': self.checkout,
            'group_adults': self.num_adults,
            'no_rooms': self.num_rooms,
            'group_children': self.num_children,
            'sb_travel_purpose': self.sb_travel_purpose,
            'nflt': self.nflt,
            'order': self.order,
        }
        print('Parameters initialized')


    def get_data(self):
        # Get hotel data
        page = 0

        while page <= 200:
            self.params['offset'] = page
            response = requests.get(self._url, params=self.params, headers=self._headers)
            soup = BeautifulSoup(response.content, "lxml")
            lists = soup.select(".d20f4628d0")

            if len(lists) == 0:
                break

            for item in lists:
                
                try:
                    location = item.find('span', {'class': 'f4bd0794db b4273d69aa'}).text
                    
                except:
                    location = 'null'
                    
                if location in [self.destination, 'null']:
                    try:
                        hotel = item.find("div", {"class": "fcab3ed991 a23c043802"}).text
                        
                    except:
                        hotel = 'null'
                        

                    try:
                        room_rate = item.find("div", {"class": "b5cd09854e d10a6220b4"}).get_text()
                        
                    except:
                        room_rate = 'null'
                        

                    try:
                        price = item.find("span", {"class": "fcab3ed991 fbd1d3018c e729ed5ab6"}).get_text()
                        
                    except:
                        price = 'null'
                        

                    try:
                        location = item.find('span', {'class': 'f4bd0794db b4273d69aa'}).text
                        
                    except:
                        location = 'null'
                        
                    
                    self.data.append({
                        'hotel_name': hotel,
                        'room_rate': room_rate,
                        'price': price,
                        'location': location,
                        'checkin_date': self.params['checkin'],
                        'checkout_date': self.params['checkout']
                    })

            page += 25
        
        print('The datas has been collected')    


    def save(self,extension,filename):
        # Get the absolute path of the 'output' folder
        folder_path = os.path.abspath(os.path.join(os.getcwd(),'output'))
        
        # Combine the folder path with the file name to create the full file path
        filepath = os.path.join(folder_path, filename)
        
        if extension == '.xlxs':  # If the extension is .xlxs
            df = pd.DataFrame(self.data)
            df.to_excel(filepath) # Save the data to an Excel file

        elif extension == '.json': # If the extension is .json
            with open(filepath, 'w') as file:
                json.dump(self.data, file) # Save the data to a JSON file

        elif extension == '.csv': # If the extension is .csv
            fieldnames = self.data[0].keys()
            with open(filepath, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.data)  # Save the data to a CSV file 
        
        else: # If the extension is not supported
            print('ERROR: extension not supported')
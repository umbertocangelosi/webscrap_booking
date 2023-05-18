from bs4 import BeautifulSoup # Import for Beautiful Soup
import requests # Import for requests
import lxml # Import for lxml parser

class booking:
    def __init__(self,headers):
        print('Object booking created')
        self._url='https://www.booking.com/searchresults.it.html'
        self._headers=headers

    def set(self,
            destinazione,
            checkin,
            checkout,
            n_adulti,
            n_bambini,
            no_rooms=1,
            sb_travel_purpose='leisure',
            nflt='privacy_typen',
            order='review_score_and_price'
            ):
        self.destinazione = destinazione
        self.checkin=checkin
        self.checkout=checkout
        self.n_adulti=n_adulti
        self.no_rooms=no_rooms
        self.n_bambini=n_bambini
        self.sb_travel_purpose=sb_travel_purpose
        self.nflt=nflt
        self.order=order
        
    def init_set(self):
        self.params={
        'ss': self.destinazione,
        'checkin': self.checkin,
        'checkout': self.checkout,
        'group_adults': self.n_adulti,
        'no_rooms': self.no_rooms,
        'group_children': self.n_bambini,
        'sb_travel_purpose': self.sb_travel_purpose,
        'nflt':self.nflt,
        'order':self.nflt,
        }  

    def get_data(self):
        data = []
        page = 0
    
        while page <= 150:
            # Add the current page to the parameters
            self.params['offset'] = page
            response = requests.get(self._url, params=self.params,headers=self._headers)
            # Make it a soup
            soup = BeautifulSoup(response.content,"lxml")

            lists = soup.select(".d20f4628d0")
                
            if len(lists) == 0:
                break    
            
            for lista in lists:
                
                try:
                    hotel = lista.find("div", {"class":"fcab3ed991 a23c043802"}).text
                    print(hotel)
                except:
                    hotel='null'
                    print(hotel)    
                        #soup.find("span", {"class": "real number", "data-value": True})['data-value']
                        #room_rate = list.find('div', class_='b5cd09854e d10a6220b4')['aria-label']
                try:    
                    room_rate = lista.find("div", {"class":"b5cd09854e d10a6220b4"}).get_text()
                    print(room_rate)
                except:
                    room_rate='null'
                    print(room_rate)    

                try:    
                    price = lista.find("span", {"class":"fcab3ed991 fbd1d3018c e729ed5ab6"}).get_text()
                    print(price)
                except:
                    price='null'
                    print('price')


                try:
                    locazione= lista.find('span',{'class':'f4bd0794db b4273d69aa'}).text 
                    print(locazione)
                except:
                    locazione = 'null'
                    print(locazione)  
                print('\n\n-------\n\n') 
                data.append({
                    'nome hotel': hotel,
                    'punteggio': room_rate,
                    'prezzo': price,
                    'locazione':locazione,
                    'checkin': params['checkin'],
                    'checkout':params['checkout'],
                    'prezzo_a_notte': (price/2), 
                }) 
            page += 25           
        return data
            
        

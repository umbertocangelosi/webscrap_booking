from bs4 import BeautifulSoup # Import for Beautiful Soup
import requests # Import for requests
import lxml # Import for lxml parser

import datetime

page= 0
#IMPORTANT: Change dates to future dates, otherwise it won't work
checkin_date = '2023-11-20'
checkout_date = '2023-11-23'
adults='2'
data = []
Location='Isola delle Femmine'
while page < 50:
    url = f"https://www.booking.com/searchresults.it.html?label=it-5Srxg0e1twJI_ryrey2UnQS410629570307%253Apl%253Ata%253Ap1%253Ap22.563.000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-65526620%253Alp1008588%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YVcLb15uXY9drDRMbmnr9EE&sid=d123ec92b198e0067986157876480a9b&aid=376372&no_rooms=1&srpvid=d8dc8786331902ec&highlighted_hotels=7711258&checkin={checkin_date}&redirected=1&city=-119364&hlrd=with_av&group_adults={adults}&source=hotel&group_children=0&checkout={checkout_date}&keep_landing=1&nflt=privacy_type%3D3%3Bht_id%3D201%3Bht_id%3D220%3Bht_id%3D213&offset={page}"
    #url = f"https://www.booking.com/searchresults.en-gb.html?aid=318615&label=New_English_EN_USD_27026936425-5WQxik%2A5vqjOdJbH0vs4ggS217290507247%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi2642648920%3Atidsa-302962658775%3Alp9069783%3Ali%3Adec%3Adm&sid=6ffc8b26c9bbcc341461e4b1a20a470c&tmpl=searchresults&checkin=2022-08-23&checkout=2022-08-24&class_interval=1&dest_id=20079110&dest_type=city&dtdisc=0&group_adults=1&group_children=0&highlighted_hotels=580015&inac=0&index_postcard=0&label_click=undef&nflt=%3Bht_id%3D204&no_rooms=1&offset=0&postcard=0&raw_dest_type=city&room1=A&sb_price_type=total&sb_travel_purpose=leisure&shw_aparth=1&slp_r_match=0&src=searchresults&srpvid=dabe52a917840104&ss=Las%20Vegas&ss_all=0&ssb=empty&sshis=0&ssne=Las%20Vegas&ssne_untouched=Las%20Vegas&changed_currency=1&selected_currency=USD&offset={page}"
    page = page + 25

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # Make it a soup
    soup = BeautifulSoup(response.content,"lxml")

    lists = soup.select(".d20f4628d0")
    lists2 = soup.select(".c8305f6688")
    results = soup.find_all('div', class_="a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942")
            
    print(len(lists)) 
        
    
    for lista in lists:
        
        location=lista.find('span',{'class':'f4bd0794db b4273d69aa'}).text
        if location==Location:
        

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
                'Nome hotel': hotel,
                'Punteggio': room_rate,
                'Prezzo': price,
                'Locazione':locazione
            }) 
            
            
                
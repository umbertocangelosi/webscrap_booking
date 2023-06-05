
from datetime import datetime, timedelta

def generator(book,start,end,delta,destination,num_adults,num_children):

    checkin = datetime.strptime(start,'%Y-%m-%d')
    ending = datetime.strptime(end,'%Y-%m-%d')
    checkout = checkin + timedelta(days=delta)
    finish = ending - timedelta(days=delta)
    
    while checkin <=finish:
        book.set(destination, checkin=checkin, checkout=checkout, num_adults=num_adults, num_children=num_children)
        book.init_set()
        book.get_data()

        checkin += timedelta(days=1)
        checkout += timedelta(days=1)

    

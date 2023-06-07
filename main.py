import pandas as pd

from src.scraper import booking


user_agent = input('hello! insert your user-agent, you can search it typing on google <what is my user agent?>\n')

holidays = booking({'User-Agent':user_agent})

# Set the parameters for the booking search
location = input('insert the location for your holidays\n') 
checkin_= input('insert the checkin date\n')
checkout_= input('insert the checkout date\n')
adults_= input('insert the number of adults\n')
childrens_= input('insert the number of childrens\n')

holidays.set(location, checkin_, checkout_, adults_, childrens_)

# Initialize the parameters for the HTTP request
holidays.init_set()

# Get the hotel data
holidays.get_data()
# Create a pandas DataFrame from the retrieved data

df = pd.DataFrame(holidays.data)
print(df)
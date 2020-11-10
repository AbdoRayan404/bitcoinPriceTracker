import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup

arg1 = 'https://www.coindesk.com/price/bitcoin' #the website that i will scrape to get the bitcoin price
previousPrice = 0 #price to compare to know if the bitcoin price go up or down NOTE:it will change when u run the code

while True:
    request = requests.get(arg1) #var to send GET request to the website
    soup = BeautifulSoup(request.content, 'html5lib') #variable for BeautifulSoup to read the content of the GET request
    textprice = soup.find("div", {"class":"price-large"}).text #filter the GET request to get the price and put it into a variable
    percent = soup.find('span', {'class':'percent-value-text'}).text #Future Feature ;)
    striped_price = textprice.strip('$') #this will delete the Dollar sign from the price and put it into variable names striped_price
    replaced_price = striped_price.replace(",", "") #this will delete the ',' sign from the striped_price var and put it into replaced_price variable
    price = float(replaced_price) #this will turn the replaced_price variable to float and put the result into variable called price
    now = datetime.now() #this will use module datetime to get the time now and put the result into variable called now
    current_time = now.strftime("%H:%M:%S") #this will make the time form Hours:Minutes:Seconds and put the result into var called current_time
    if previousPrice == price:
        print('[-]', price,'\033[39m' + 'time: ' + current_time) #u want me to comment that too?! -_-
    elif previousPrice < price:
        print('\033[31m' + '[!]', price,'\033[39m' + 'time: ' + current_time)
    else: print('\033[32m' + '[@]', price, '\033[39m' + 'time:' + current_time)
    previousPrice = price #this the last move in the while Loop and it will give the price to the previousPrice and when we start thw hile loop again the price will get a new value then compare it with the previousPrice to see if the bitcoin price go up or down
    time.sleep(180) #every 3 mins it will see the bitcoin price

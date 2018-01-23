
# coding: utf-8

# In[ ]:


import urllib2
from bs4 import BeautifulSoup

def get_list(weburl):
    page = urllib2.urlopen(weburl)
    soup = BeautifulSoup(page, 'html.parser')
    
    #a = soup.find("li", class_="article-list")
    a = soup.find_all("li", class_="article-list-item")
    result = list()
    for i in a:
        result.append(i.text.replace('\n', ''))
    return result[0]


# In[19]:


###
###telegram bot
###
import telegram
bottoken = '545920666:AAEKL-PLLWFOi5bdg7qt9k2tBl3uzJl98iU'
bot = telegram.Bot(token=bottoken)
def send_message_telegram(yourtext):
    #bot.sendMessage(chat_id='525952155'and'354080555', text=yourtext)
    bot.sendMessage(chat_id='-256092400', text=yourtext)#group id


# In[5]:


def check_different(old, url):
    new = get_list(url)
    topic = url.split('/')[-1].split('-', 1)[1]
    if old != new:
        old = new
        text = time.strftime("%m/%d, %I:%M:%S") + "\n*** News ***\n" + topic + ": " + new
        send_message_telegram(text)
        print(topic + "'s Message SENT!")
    else:
        print(time.strftime("%m/%d, %I:%M:%S") + " *** same *** " + topic)
    return old


# In[20]:


import time
url_intro = "https://support.binance.com/hc/en-us/sections/115000122291-Assets-Introduction"
url_listings = "https://support.binance.com/hc/en-us/sections/115000106672-New-Listings"
url_news = "https://support.binance.com/hc/en-us/sections/115000202591-Latest-News"
url = [url_intro, url_listings, url_news]
#old = get_token_list(url)
old = [None, None, None]
while True:
    for num in range(3):
        old[num] = check_different(old[num], url[num])
    time.sleep(100)


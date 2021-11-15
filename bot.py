# Slack Bot Import
##################
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import time

#####################
# Selenium Import
#####################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    'https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition-Video-Game-Consoles/987823383')

def isAvailable(driver):
    e = driver.find_element_by_css_selector('.justify-between > .flex-column > .pt2-m')
    return e.text

while True:
    driver.refresh()
    try:
        availability = isAvailable(driver)
        if availability == "Out of stock":
            text_to_send = availability
    except Exception as e:
            text_to_send = str(e)
    # if text == "Out of stock":
    #     # Do Nothing
    #     pass
    # else:
    #     # Ping me in slack
    env_path = Path('.')/'.env'
    load_dotenv(dotenv_path=env_path)
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    client.chat_postMessage(channel='#test', text=text_to_send)
    time.sleep(500)





    


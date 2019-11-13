from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import traceback
import re
import json
import time 

driver = webdriver.Chrome()
currentTab = 0;

def login():
    driver.get("https://www.omegle.com/")
    time.sleep(5)
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    return(
        driver.get('https://rebot.me/pt/dra-lena-analista')
    )

def extractBotMsg():
    allTextTyped = driver.find_element_by_xpath('//*[@id="answer"]').get_attribute("innerHTML");
    matchingRegex = re.compile('(<span>)([a-zA-ZçãáÉêéí0-9,.!_?\(\)\[\] ]+)(:<\/span>)([a-zA-ZçãáÉêéíó0-9,.!_? ]+)')
    matches = matchingRegex.findall(allTextTyped);
    return(
        matches[-1][3]
    )

def extractMsg(position=1):
    allTextTyped = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div[1]/div").get_attribute("innerHTML");
    matchingRegex = re.compile('(<div class="logitem"><p class="strangermsg"><strong class="msgsource">Stranger:<\/strong> <span class="notranslate">)([a-zA-ZçÉãáêéíó0-9,.!_? ]+)(<\/span><\/p><\/div>)')
    matches = matchingRegex.findall(allTextTyped);
    return(
        matches[-1][position]
    )

def writeToBot(msg):
    driver.find_element_by_xpath('//*[@id="question"]').send_keys(msg);
    driver.find_element_by_xpath('//*[@id="question"]').send_keys(Keys.ENTER);
    time.sleep(1)

def writeToOmegle(msg):
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea').send_keys(msg);
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea').send_keys(Keys.ENTER);

def switchTabs():
    global currentTab;
    if(currentTab):
        driver.switch_to.window(driver.window_handles[0])
        currentTab = 0
    else:
        driver.switch_to.window(driver.window_handles[1])
        currentTab = 1

def run():
    while(1):
        try:
            atual = extractMsg()
            switchTabs()
            writeToBot(atual)
            bot = extractBotMsg()
            if bot.strip().lower() == "h":
                bot = "m"
            switchTabs()
            writeToOmegle(bot)
            input("Aperte qualquer tecla para continuar..")
        except:
            pass

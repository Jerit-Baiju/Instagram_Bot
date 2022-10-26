import os
import time

import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import root
from basic import out, sub

mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}

TIMEOUT = 10

user = sub('enter the username')

def run(user):
    out('setting options')
    options = webdriver.Firefox()
    #options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    out('opening chrome')
    bot = webdriver.Chrome(options=options)
    bot.set_window_size(600, 1000)
    bot.get('https://www.instagram.com/accounts/login/')
    out('entering username')
    # username
    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))
    elem.send_keys(root.insta_username)

    out('entering password')
    # password
    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))
    elem.send_keys(root.insta_password)

    out('logining')
    # login button
    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))
    elem.click()

    out('skiping session')

    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/section/main/div/div/section/div/button')))
    elem.click()

    out('skiping notifications')
  
    elem = WebDriverWait(bot, TIMEOUT).until(
    EC.presence_of_element_located((
    By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))
    elem.click()

    out(f'redirecting to https://www.instgram.com/{user}')
    bot.get(f'https://www.instgram.com/{user}')

    out('advanced tools')

    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div/div[2]/button[3]')))
    elem.click()

    out('proceeding link')

    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="proceed-link"]')))
    elem.click()

    out('Getting info')

    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/section/main/div/div[1]/span')))
    out(f'Name : {elem.text}')

    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/div')))
    out(f'Bio : {elem.text}')

    elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[1]/div/span')))
    out(f'Posts : {elem.text}')
    
    try:
        elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
        By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[2]/a/div/span')))
        out(f'followers : {elem.text}')


        elem = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
        By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[3]/a/div/span')))
        out(f'following : {elem.text}')

    except:
        out('private account')

    bot.execute_script("window.scrollTo(0, 4000);")
    images = bot.find_elements(By.TAG_NAME, value='img')
    images = [image.get_attribute('src') for image in images]
    images = images[:-2]
    out('Number of scraped images: ' + str(len(images)))

    if len(images) != 0:
        path = os.getcwd()
        path = os.path.join(path, 'Photos/'+user+'/')
        os.mkdir(path)
        out(path)
        counter = 0

        for image in images:
            save_as = os.path.join(path, f'{user}_{str(counter)}.jpg')
            wget.download(image, save_as)
            counter += 1
        bot.quit()
    else:
        bot.quit()

run(user)
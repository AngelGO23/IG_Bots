from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


username = input("Username: ")
password = input("Password: ")
searchTag = input("Cual hashtag quieres darle like? ")
try:

    n = int(input("Cuantos Post quieres darle like? "))
except:
    print("Creo que eso no es un numero. Tal vez lo estas escribiendo en letras?")
    quit()



path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)


driver.get("https://www.instagram.com/")



try:
    print("finding username text box")
    username_tb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    print('found username text box')
    username_tb.send_keys(username)
    print('searching for password text box')
    password_tb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_tb.send_keys(password)
    password_tb.send_keys(Keys.RETURN)
    print('found password text box')

except:
    print('Not found: username, password, pic, or profile')
    driver.quit()

try:
    print('Finding search box')
    searchBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']"))
    )
    print("Writing search text")
    searchBox.send_keys("#" + searchTag)
    time.sleep(2)
    searchBox.send_keys(Keys.RETURN)
    searchBox.send_keys(Keys.RETURN)
    print("Finding first post")
    fpost = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_9AhH0"))
    )
    print('Clicking first post')
    fpost.click()
    print('showing first post')


except:
    print("Cannot find: Search box or enter search")


time.sleep(1)

likeCount = 0
try:

    for i in range(0, n):
        likeCount += 1
        print("Buscando Like ", likeCount )
        like = WebDriverWait(driver, 15).until(
               EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Like']"))
        )
        print("presionando Like")
        like.click()
        print("Buscando Next")
        nextPost = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH,"//a[text()='Next']"))
        )
        print("Presionando Next")
        nextPost.click()
    print("Todos los posts se les dio Like")
except TimeoutException:
    print("Either their aren't that many post for the requiered amount or you have to load more photos")




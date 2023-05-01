from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class main:
    
    driver = webdriver.Chrome(executable_path=r"C:\Chrome\chromedriver.exe")
    # Opens the website
    driver.get("https://www.mlb.com/play/login")

    # Gets email, password, and login button
    email_box = driver.find_element("id", "email")
    pw_box = driver.find_element("id", "password")

    log_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/form/div[3]/button')
    # Enter credentials and login
    username = input("Username: ")
    password = input("Password: ")
    email_box.send_keys(username)
    pw_box.send_keys(password)
    log_button.click()

    # clicks beat the streak gamemode
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div/div/ul/li[1]/a'))
    )
    element.click()

    # clicks the make a pick button
    mkpick = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div.css-pzmxj4 > div.css-6sda7d > div.css-4ea9de > div.css-wlkz8l'))
    )
    mkpick.click()

    # clicks the first suggested player
    # this is temporary, once it works, work on ML to make the best possible pick for the day
    player = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div.css-pzmxj4 > div.css-6sda7d > div.css-ulv7fr > div > div.css-1niqsri > div > div:nth-child(1)'))
    )
    player.click()

    # Unable to click the last button, possibly in iframe or DOM?
    confirm = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, ''))
    )
    confirm.click()



if __name__ == "__main__":
    main()

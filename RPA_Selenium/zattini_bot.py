from time import sleep
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium import webdriver
import time


def auto_driver():
    chromedriver_autoinstaller.install()
    chrome_options = Options()
    chrome_options.add_argument("-headless")
    return webdriver.Chrome(options=chrome_options)


def rpa(json_data):
    driver = auto_driver()

    driver.get("https://www.cea.com.br/login")

    sleep(1)
    driver.find_element_by_xpath('//*[@id="L_email"]').send_keys(json_data['email'])
    sleep(1)
    driver.find_element_by_xpath('//*[@id="L_senha"]').send_keys(json_data['password'])
    driver.find_element_by_xpath('//*[@id="enviar"]').click()

    sleep(2)
    driver.get('https://www.cea.com.br/checkout#/cart')
    sleep(2)

    texto = driver.find_element_by_xpath('//*[@id="cartLoadedDiv"]/div[1]/h2').text

    driver.close()
    driver.quit()

    return {"status": (True, False)['sua sacola está vazia' in texto]}


if __name__ == '__main__':
    dicio = {
        "email": "ericksonlopes20@gmail.com",
        "password": ""
    }

    print(rpa(dicio))

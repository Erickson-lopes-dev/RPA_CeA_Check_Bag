from time import sleep
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium import webdriver
import time
import platform
import os


def auto_driver():
    chromedriver_autoinstaller.install()
    chrome_options = Options()
    chrome_options.add_argument("-headless")
    return webdriver.Chrome(options=chrome_options)


def pl_driver():
    op_system = platform.system()
    # print(OP_SYSTEM)

    if op_system.lower() == 'windows':
        chromedriver_autoinstaller.install()

    # Create a folder to recieve your donwloads
    try:
        os.mkdir(os.path.dirname(os.path.realpath(__file__)) + '//data')
    except:
        pass

    folder = os.path.dirname(os.path.realpath(__file__)) + '/data'  # Set Google Options
    options = webdriver.ChromeOptions()

    # Define donwload settings
    prefs = {''
             # Set a specific folder to download files from selenium ( Default is download folder )
             "download.default_directory": r"%s" % folder,
             "download.prompt_for_download": False,
             "download.directory_upgrade": True
             }

    options.add_experimental_option('prefs', prefs)
    options.add_argument("--headless")  # This option hide the browser... to see the browser comment this line
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # Remove selenium logs on console ( More clean! )
    options.add_argument('--log-level=3')
    # Chose the webdriver according with your system

    if op_system.lower() == 'windows':
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome(executable_path='chromedriver', options=options)

    return driver


def rpa(json_data):
    driver = pl_driver()

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

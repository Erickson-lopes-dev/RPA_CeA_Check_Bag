from time import sleep
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium import webdriver
import os


def selenoid_remote_connection():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "89.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)

    return driver


def heroku_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


def auto_driver():
    chromedriver_autoinstaller.install()
    chrome_options = Options()

    chrome_options.add_argument("-headless")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(options=chrome_options)


def rpa(json_data):
    try:
        driver = heroku_driver()

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

    except Exception as error:
        return {'status': f"ERRo {str(error)} {str(type(error))}"}

    else:
        return {"status": (True, False)['sua sacola está vazia' in texto]}

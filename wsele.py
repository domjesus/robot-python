from pathlib import Path
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from robot import list, ler_csv

from time import sleep

# folder_path = str(Path(__file__).parents[0])


def acessa(driver):
    driver.get("http://localhost:8000/")
    sleep(2)
    driver.get("http://localhost:8000/users_alt_siape")


def pega_dados(driver, siape):
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(siape)

    search_button = driver.find_element(
        By.CSS_SELECTOR, "#app > div > div > div > div.box-body > div > div > div > form > input:nth-child(4)")
    search_button.click()


siapes = ler_csv()

# print(siapes)


def test_chrome_session():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    acessa(driver)

    # driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(0.5)
    # link = driver.find_element(
    #     By.CSS_SELECTOR, "#navbar-collapse > ul > li.dropdown.open > ul > li:nth-child(22) > ul > li:nth-child(3)")
    # link.click()
    for siape in siapes:
        pega_dados(driver, siape.zfill(7))

        # sleep(3)

        chk_button_solicita = driver.find_element(
            By.XPATH, "//*[@id='app']/div/div/div[2]/div/form/div[2]/div/div[20]/input[3]")

        chk_button_pontuacao = driver.find_element(
            By.XPATH, "//*[@id='app']/div/div/div[2]/div/form/div[2]/div/div[12]/input[1]")

        checked_bs = chk_button_solicita.get_attribute('checked')
        checked_po = chk_button_pontuacao.get_attribute('checked')

        # altera somente se não tiver checado
        if(checked_bs and checked_po):
            pass
        elif(not checked_bs and not checked_po):
            chk_button_solicita.click()
            chk_button_pontuacao.click()
        elif(not checked_bs):
            chk_button_solicita.click()
        elif(not checked_po):
            chk_button_pontuacao.click()

        submit_button = driver.find_element(
            By.CSS_SELECTOR, "#app > div > div > div.box-body > div > form > div.form-group.col-sm-12 > input")

        submit_button.click()

        # browser.find_element_by_xpath(
        #     ".//*[@id='C179003030-ORNL_DAAC-box']").get_attribute('checked')

        # acessa(driver)
        # pega_dados(driver, siape)

    sleep(10)

    driver.quit()


test_chrome_session()
# for siape in siapes:
# print(siape.zfill(7))

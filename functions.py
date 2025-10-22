import time
from config import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_click(driver, SELECTOR, time=10):
    '''ESPERAR O ELEMENTO SER GERADO E CLICAR NELE'''
    wait_element_click1 = WebDriverWait(driver, time).until(EC.presence_of_element_located(
    (
        By.XPATH, SELECTOR
    ))).click()
    return wait_element_click1

def select_year(driver, SELECTORS):
    '''ESCOLHER O MÊS/ANO'''
    driver.find_element(By.XPATH, SELECTORS['dropdown_year']).click()
    options_data = driver.find_elements(By.XPATH, SELECTORS['options_year'])
    return options_data[0].find_elements(By.CSS_SELECTOR, 'li')

def select_marca(driver, SELECTORS, indice):
    '''ESCOLHER MARCA'''
    wait_element_click2 = WebDriverWait(driver, WAIT_TIMEOUT).until(EC.presence_of_element_located(
    (
        By.XPATH, SELECTORS['dropdown_marca']
    ))).click()

    options_marca = driver.find_elements(By.XPATH, SELECTORS['options_marca'])
    var_list_marca = options_marca[0].find_elements(By.CSS_SELECTOR, 'li') 
    var_list_marca[indice].click()

def select_model(driver, SELECTORS):
    '''ESCOLHER MODELO'''
    driver.find_element(By.XPATH, SELECTORS['dropdown_modelo']).click()
    options_model = driver.find_elements(By.XPATH, SELECTORS['options_modelo'])
    return options_model[0].find_elements(By.CSS_SELECTOR, 'li')

def select_year_models(driver, SELECTORS):
    '''ESCOLHER O ANO/MODELO'''
    driver.find_element(By.XPATH, SELECTORS['dropdown_ano_modelo']).click()
    options_year = driver.find_elements(By.XPATH, SELECTORS['options_ano_modelo'])
    return options_year[0].find_elements(By.CSS_SELECTOR, 'li')

def move_screen(driver, times):
    for _ in range(0, times):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)

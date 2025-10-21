## IMPORTAÇÕES WEBDRIVER E SELENIUM
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

##  UTILITÁRIOS QUE AJUDARÃO NO PROJETO
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

## CONFIGURAÇÕES
from config import *

## CONFIGURAÇÃO E INSTALAÇÃO AUTOMÁTICA DO SERVIÇO
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://veiculos.fipe.org.br")
driver.maximize_window()

## SOLICITAR ENTRADA DO USUÁRIO
try:
    MARCA_INDEX = int(input("Digite o índice da marca: "))
except:
    MARCA_INDEX = MARCA_INDEX  # Usa valor padrão se input falhar

## PASSO 01: CLICAR NA DIV DE MOTOS
wait_element_click1 = WebDriverWait(driver, WAIT_TIMEOUT).until(EC.presence_of_element_located(
    (
        By.XPATH, SELECTORS['menu_motos']
    )
)).click()

motos = {}
number_moto = 0

time.sleep(SHORT_DELAY) 

def select_year():
    driver.find_element(By.XPATH, SELECTORS['dropdown_year']).click()
    options_data = driver.find_elements(By.XPATH, SELECTORS['options_year'])
    return options_data[0].find_elements(By.CSS_SELECTOR, 'li')

def select_marca(indice):
    wait_element_click2 = WebDriverWait(driver, WAIT_TIMEOUT).until(EC.presence_of_element_located(
    (
        By.XPATH, SELECTORS['dropdown_marca']
    ))).click()

    options_marca = driver.find_elements(By.XPATH, SELECTORS['options_marca'])
    var_list_marca = options_marca[0].find_elements(By.CSS_SELECTOR, 'li') 
    var_list_marca[indice].click()

def select_model():
    driver.find_element(By.XPATH, SELECTORS['dropdown_modelo']).click()
    options_model = driver.find_elements(By.XPATH, SELECTORS['options_modelo'])
    return options_model[0].find_elements(By.CSS_SELECTOR, 'li')

def select_year_models():
    driver.find_element(By.XPATH, SELECTORS['dropdown_ano_modelo']).click()
    options_year = driver.find_elements(By.XPATH, SELECTORS['options_ano_modelo'])
    return options_year[0].find_elements(By.CSS_SELECTOR, 'li')

## SCROLL RENDER 
def move_screen(times):
    for _ in range(0, times):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)

################################################################################

## PASSO 02: ESCOLHER O MÊS/ANO
var_list_year = select_year() 

for year in range(MAX_YEARS_TO_PROCESS): 
    var_list_year[year].click()

    ## PASSO 03.1: ESCOLHER MARCA
    select_marca(MARCA_INDEX) 

    ## PASSO 03.2: ESCOLHER MODELO
    var_list_model = select_model()

    for model in range(0, len(var_list_model)):
        print(45*'*' + f' Modelo: {model} ' + 45*'*')
        var_list_model[model].click()
        var_list_year_models = select_year_models()

        for year_models in range(0, len(var_list_year_models)):
            ## PASSO 04: ESCOLHER O ANO/MODELO
            var_list_year_models[year_models].click()
            
            ## PASSO 05: CLICAR EM PESQUISAR
            time.sleep(SHORT_DELAY)
            driver.find_element(By.LINK_TEXT, 'Pesquisar').click()

            ## PASSO 06: CRIAR DICIONÁRIO
            tabela = driver.find_elements(By.XPATH, SELECTORS['tabela_resultados'])
            var_linha_dic = tabela[0].find_elements(By.CSS_SELECTOR, 'td')
            moto = {}

            for item in range(0, len(var_linha_dic)-1, 2):
                moto[var_linha_dic[item].text] = var_linha_dic[item+1].text

            motos[number_moto] = moto
            print(f'Moto:{motos[number_moto]}')
            print(15*'-')
    
            number_moto += 1

            time.sleep(SHORT_DELAY)
            move_screen(SCROLL_TIMES)
            time.sleep(SHORT_DELAY)

            var_list_year_models = select_year_models()
        
        move_screen(SCROLL_RESET_TIMES)
        select_marca(MARCA_INDEX+1)
        time.sleep(SHORT_DELAY)
        select_marca(MARCA_INDEX)
        var_list_model = select_model()

    move_screen(SCROLL_RESET_TIMES)
    time.sleep(SHORT_DELAY)
    select_marca(MARCA_INDEX+1)
    var_list_year = select_year()

driver.close() 

with open("Motos.json", "w", encoding="utf-8") as f:
    json.dump(motos, f, ensure_ascii=False, indent=2)

print(f"Arquivo final salvo! Total de {len(motos)} motos")
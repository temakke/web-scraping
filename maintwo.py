## IMPORTAÇÕES WEBDRIVER E SELENIUM
import time
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

## ARQUIVOS DE CONFIGURAÇÃO E FUNÇÕES
from config import *
from functions import *

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

wait_and_click(driver, SELECTORS['menu_motos'])

var_list_year = select_year(driver, SELECTORS) 

for year in range(MAX_YEARS_TO_PROCESS): 
    var_list_year[year].click()

    select_marca(driver, SELECTORS, MARCA_INDEX) 

    var_list_model = select_model(driver, SELECTORS)

    for model in range(0, len(var_list_model)):
        print(45*'*' + f' Modelo: {model} ' + 45*'*')
        var_list_model[model].click()
        var_list_year_models = select_year_models(driver, SELECTORS)

        for year_models in range(0, len(var_list_year_models)):
            var_list_year_models[year_models].click()
                
            ## CLICAR EM PESQUISAR
            time.sleep(SHORT_DELAY)
            driver.find_element(By.LINK_TEXT, 'Pesquisar').click()

            ## CRIAR DICIONÁRIO
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
            move_screen(driver, SCROLL_TIMES)
            time.sleep(SHORT_DELAY)

            var_list_year_models = select_year_models(driver, SELECTORS)
            
        move_screen(driver, SCROLL_RESET_TIMES)
        select_marca(driver, SELECTORS, MARCA_INDEX+1)
        time.sleep(SHORT_DELAY)

        select_marca(driver, SELECTORS, MARCA_INDEX)
        var_list_model = select_model(driver, SELECTORS)

    move_screen(driver, SCROLL_RESET_TIMES)
    time.sleep(SHORT_DELAY)
    select_marca(driver, SELECTORS, MARCA_INDEX+1)
    var_list_year = select_year(driver, SELECTORS)

driver.close() 

with open("Motos.json", "w", encoding="utf-8") as f:
    json.dump(motos, f, ensure_ascii=False, indent=2)

print(f"Arquivo final salvo! Total de {len(motos)} motos")
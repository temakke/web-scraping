"""
Configurações centralizadas do projeto FIPE Scraper
"""

# Configurações de tempo
WAIT_TIMEOUT = 10
SHORT_DELAY = 1
LONG_DELAY = 2

# Configurações de scraping
MAX_YEARS_TO_PROCESS = 1
MARCA_INDEX = 2
BACKUP_INTERVAL = 5

# Configurações de navegação
SCROLL_TIMES = 3
SCROLL_RESET_TIMES = 7

#

motos = {}
number_moto = 0


# Seletores XPATH
SELECTORS = {
    'menu_motos': '//*[@id="front"]/div[1]/div[2]/ul/li[3]/a/div[2]',
    'dropdown_year': '//*[@id="selectTabelaReferenciamoto_chosen"]/a/div/b',
    'dropdown_marca': '//*[@id="selectMarcamoto_chosen"]/a/div/b',
    'dropdown_modelo': '//*[@id="selectAnoModelomoto_chosen"]/a/div/b',
    'dropdown_ano_modelo': '//*[@id="selectAnomoto_chosen"]/a/div/b',
    'options_year': '//*[@id="selectTabelaReferenciamoto_chosen"]/div/ul',
    'options_marca': '//*[@id="selectMarcamoto_chosen"]/div/ul',
    'options_modelo': '//*[@id="selectAnoModelomoto_chosen"]/div/ul',
    'options_ano_modelo': '//*[@id="selectAnomoto_chosen"]/div/ul',
    'tabela_resultados': '//*[@id="resultadoConsultamotoFiltros"]/table/tbody'
}
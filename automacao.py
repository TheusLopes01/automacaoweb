from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
navegador.get('https://hashtagtreinamentos.activehosted.com/f/2475')
navegador.find_element('xpath', '/html/body/div/form/div[1]/div[2]/div/input').send_keys('matheus')


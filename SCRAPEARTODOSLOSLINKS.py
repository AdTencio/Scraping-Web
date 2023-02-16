#SCRAPING DE PAGINA MODIFICANDO FECHA
import pandas as pd
import csv
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup


pag_ligaarg = "https://competicionescabb.gesdeportiva.es/partidos.aspx?categoria=1094&titulos=no&clasificacion=cociente"
path = '/Users/Usuario/descargas/chromedriver'

driver = webdriver.Chrome(path)
driver.get(pag_ligaarg)
#Actualizar fecha
all_matches_button = driver.find_element("xpath", '//input[@id="TBFechaInicio"]')
all_matches_button.click()
all_matches_button.send_keys("05092022")
actualizar_data = driver.find_element("xpath", '//*[@id="BActualizar"]')
actualizar_data.click()
time.sleep(3)
#Fecha actualizada

soup = BeautifulSoup(driver.page_source, 'html.parser')
table_responsive = soup.find("div", class_="table-responsive")
links = table_responsive.find_all("a")
for link in links:
    print(link.get("href"))
    
print(links)

#Creamos un .csv con todos los links de los partidos.
with open('Scraping GES Liga Argentina\\links_partidos.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(links)

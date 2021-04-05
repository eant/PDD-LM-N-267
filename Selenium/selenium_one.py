#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:55:10 2021

@author: smessina
"""

from selenium import webdriver

# driver = webdriver.Chrome("./chromedriver.exe") # <- Para Windows...

driver = webdriver.Chrome("./chromedriver")

driver.get("https://es.wikipedia.org/wiki/MacOS#Versiones")

# Acá voy a codear magia araña

tabla = driver.find_element_by_class_name('wikitable')

filas = tabla.find_elements_by_tag_name('tr')

macos_csv = "Versión	,Nombre en código,Anuncio,Presentación,Versión más reciente\n"

for i in range(1, len(filas) ):
    valores = filas[i].find_elements_by_tag_name('td')
    #print( valores[1].text )
    macos_csv += valores[0].text +','+ valores[1].text +','+ valores[2].text +','+ valores[3].text +','+ valores[4].text +'\n'


print( macos_csv )

driver.quit()
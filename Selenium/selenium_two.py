#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:13:19 2021

@author: smessina
"""
import random
from time import sleep
from selenium import webdriver

#driver = webdriver.Chrome("./chromedriver")

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome("./chromedriver", options=op)

driver.get('https://www.olx.com.ar/libros-y-revistas_c860')

#sleep( random.uniform(8.0, 10.0) )

#script_js = "window.setTimeout(function(){ document.querySelector('[data-aut-id=\"btnLoadMore\"]').click() }, 3000)"

# Aguardar hasta que se carguen 3 tandas de productos...
for i in range(3):
    
    try:
        sleep( random.uniform(8.0, 10.0) )
        
        driver.execute("document.querySelector('[data-aut-id=\"btnLoadMore\"]').click()")
        
        sleep( random.uniform(8.0, 10.0) )
    except:
        break

# Explorar el total de productos cargados..  
items = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

# Recorrer y mostrar la info de cada producto extraido...
for item in items:
    print('Titulo:')
    title = item.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]')
    
    print(title.text)

driver.quit()
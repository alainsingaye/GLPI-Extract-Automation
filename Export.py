from selenium import webdriver

import time

import logging

# Ce sont les logger pour les logs
logger = logging.getLogger('logs')
logger.setLevel(logging.DEBUG)

# C'est la console handler and le niveau pour le debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Le formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# L'ajout du formatter to ch
ch.setFormatter(formatter)

# Ajout ch du logger
logger.addHandler(ch)

# Script permettant de Faire un Export de la base de GLPI des ordinateurs. Par Alain Singaye le 11/0/20 version 2.1

# Le dossier dans lequel sera saugarder l'export.
download_dir = r"C:\Users\alain.singaye\Documents\GLPI"
chrome_options = webdriver.ChromeOptions()
path = r'C:/bin/chromedriver.exe'
preferences = {"download.default_directory": download_dir ,
               "directory_upgrade": True,
               "safebrowsing.enabled": True,
               "plugins.always_open_pdf_externally": True
                    }
chrome_options.add_experimental_option("prefs", preferences)
chrome = webdriver.Chrome(path, chrome_options=chrome_options)

#Permet de se rendre sur le site.

#Try et Except permet de recouvrir des erreurs
try:

    chrome.get("http://glpi.ad.kellydeli.net/glpi/index.php?noAUTO=1")

except:
    logger.error("connection to website unsuccessful")
else:
    logger.info("connection was successful")

# Le script rentre les identifiant et les mots de passes

try:

    chrome.find_element_by_xpath("//input[@id = 'login_name']").send_keys( "alain.singaye" )
    chrome.find_element_by_xpath("//input[@id = 'login_password']").send_keys( "H3XsBgueqV8yaRRM" )

except:

    logger.error('problem while logging in')

else:

    logger.info('logged in')

# Clique sur le bouton
submit_button = chrome.find_element_by_xpath('//input[@type="submit"]')
submit_button.click()

#Cliquez sur ordinateurs

submit_button = chrome.find_element_by_xpath("//a[@id= 'menu_all_button'] ")
submit_button.click()

#Pour laisser du temps entre les pages
time.sleep(2)

# Permet à l'utilisateur de faire un choix sur son Export
choix = input("Que voulez vous executer, Ordinateur ou Téléphones?")

try:

    if choix == 'Ordinateur':

        submit_button = chrome.find_element_by_xpath("//a[contains(text(),'Ordinateurs')]")
        submit_button.click()

except:

   logger.error('Export unsuccessful')

else:
    logger.info('Export successful')

try:

    if choix == 'Téléphones':




            submit_button = chrome.find_element_by_xpath('//*[@id="show_all_menu"]/table[1]/tbody/tr[10]/td/a')
            submit_button.click()

except:

    logger.error('Export unsuccessful ')

else:

    logger.info('Export was successful')

#Cliquez sur le bouton export
submit_button = chrome.find_element_by_xpath('//input[@name="export"]')
submit_button.click()






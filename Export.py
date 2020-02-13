# Script permettant de Faire un Export de la base de GLPI des ordinateurs. Par Alain Singaye le 21/01/20 version 2.4

from selenium import webdriver

import time

import logging

#Fonction pour chercher le site internet
def access_to_website(url):
    chrome.get(url)
    
logging.basicConfig(filename= r"C://your//directory//path//filename.txt",
                    format= '%(asctime)s  - %(levelname)s - %(message)s',
                    datefmt= '%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG
                    )





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

# Le dossier dans lequel sera saugarder l'export.
download_dir = r"C:\Users\username\Directory\Filename"
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

    access_to_website("your GLPI site")

except:
   print(logger.error("website unreachable"))

else:
    logger.info("connection was successful")

# Le script rentre les identifiant et les mots de passes

chrome.find_element_by_xpath("//input[@id = 'login_name']").send_keys("username" )
chrome.find_element_by_xpath("//input[@id = 'login_password']").send_keys( "password" )


# Clique sur le bouton
submit_button = chrome.find_element_by_xpath('//input[@type="submit"]')
submit_button.click()

try:
    chrome.find_element_by_xpath('//*[@id="c_ssmenu2"]/ul/li[1]/a')
except:
    logger.error('not logged in')

else:
    logger.info('logged in')

#Cliquez sur ordinateurs

submit_button = chrome.find_element_by_xpath("//a[@id= 'menu_all_button'] ")
submit_button.click()

#Pour laisser du temps entre les pages
time.sleep(2)

# Permet à l'utilisateur de faire un choix sur son Export
choix = input("Que voulez vous executer, Ordinateurs ou Téléphones?")

#try:

try:
    if choix == 'Ordinateurs':
            submit_button = chrome.find_element_by_xpath("//a[contains(text(),'Ordinateurs')]")
            submit_button.click()
            submit_button = chrome.find_element_by_xpath('//input[@name="export"]')
            submit_button.click()
    elif choix == 'Téléphones':
            submit_button = chrome.find_element_by_xpath('//*[@id="show_all_menu"]/table[1]/tbody/tr[10]/td/a')
            submit_button.click()

            #Cliquez sur le bouton export
            submit_button = chrome.find_element_by_xpath('//input[@name="export"]')
            submit_button.click()


except Exception as exception:
   logger.error('Export unsuccessful')
   logger.error(exception)

else:
    logger.info('Export Successful')




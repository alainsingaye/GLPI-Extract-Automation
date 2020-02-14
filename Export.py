# Script permettant de Faire un Export de la base de GLPI des ordinateurs. Par Alain Singaye le 21/01/20 version 2.7

from selenium import webdriver

import time

import logging

#Pour la rotation des Logs
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

path = r"C://Users//alain.singaye//Documents//GLPI//Logs"



#Fonction pour chercher le site internet
def access_to_website(url):
    chrome.get(url)





# Permet d'enregistrer les logs dans un fichier et de faire La rotation

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotation_handler = TimedRotatingFileHandler(filename=r"C://Users//alain.singaye//Documents//GLPI//Logs//log.txt", when='M', interval=3)
rotation_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(rotation_handler)
logger.setLevel(logging.DEBUG)


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

    access_to_website("http://glpi.ad.kellydeli.net/glpi/index.php?noAUTO=1")

except:
   logger.error("website unreachable")


else:
    logger.info("connection was successful")

# Le script rentre les identifiant et les mots de passes

chrome.find_element_by_xpath("//input[@id = 'login_name']").send_keys("alain.singaye")
chrome.find_element_by_xpath("//input[@id = 'login_password']").send_keys("H3XsBgueqV8yaRRM")


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




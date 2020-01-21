# Script permettant de Faire un Export. Par Alain Singaye le 21/01/20 version 2.0

#Exporter le driver selenium

from selenium import webdriver

# Exporter time pour qu'il est du temps entres les actions
import time


# Permet de se rendre sur le site internet et d'effectuer le téléchargement en PDF

download_dir = r"C:\Paht\to\Your\Directory"
chrome_options = webdriver.ChromeOptions()
path = r'C:/bin/chromedriver.exe'
preferences = {"download.default_directory": download_dir ,
               "directory_upgrade": True,
               "safebrowsing.enabled": True,
               "plugins.always_open_pdf_externally": True
                    }
chrome_options.add_experimental_option("prefs", preferences)
chrome = webdriver.Chrome(path, chrome_options=chrome_options)
chrome.get("your GlPI website")

# Le script rentre les identifiant et les mots de passes
chrome.find_element_by_xpath("//input[@id = 'login_name']").send_keys( "your username" )
chrome.find_element_by_xpath("//input[@id = 'login_password']").send_keys( "your password" )



# Clique sur le bouton
submit_button = chrome.find_element_by_xpath('//input[@type="submit"]')
submit_button.click()

#Cliquez sur ordinateurs

submit_button = chrome.find_element_by_xpath("//a[@id= 'menu_all_button'] ")
submit_button.click()

#Pour laisser du temps entre les pages
time.sleep(2)

submit_button = chrome.find_element_by_xpath("//a[contains(text(),'Ordinateurs')]")
submit_button.click()
#Cliquez sur le bouton export
submit_button = chrome.find_element_by_xpath('//input[@name="export"]')
submit_button.click()

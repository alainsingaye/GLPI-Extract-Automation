# Script permettant de Faire un Export de la base de GLPI des ordinateurs. Par Alain Singaye le 18/02/20 version 2.8

from selenium import webdriver

#permet l'envoi de mail en utilisant le smpt
import smtplib, ssl

from email.message import EmailMessage

#Pour mettre du temps entre les executation des tâches
import time

#Pour la création des loggins
import logging

#Pour la rotation des Logs
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


#Fonction pour chercher le site internet
def access_to_website(url):
    chrome.get(url)

#Pour envoyer un mail après l'export
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




# Permet d'enregistrer les logs dans un fichier et de faire La rotation

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotation_handler = TimedRotatingFileHandler(filename=r"C://Users//alain.singaye//Documents//GLPI//Logs//log.txt", when='H', interval=5)
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

    access_to_website("Votre site GLPI")

except:
   logger.error("website unreachable")


else:
    logger.info("connection was successful")

# Le script rentre les identifiant et les mots de passes

chrome.find_element_by_xpath("//input[@id = 'login_name']").send_keys("username")
chrome.find_element_by_xpath("//input[@id = 'login_password']").send_keys("password")


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
choix = input("Quel export voulez vous faire?")

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
    elif choix == 'Logiciels':
            submit_button = chrome.find_element_by_xpath('//*[@id="show_all_menu"]/table[1]/tbody/tr[4]/td/a')
            submit_button.click()
    elif choix == 'Périphériques':
            submit_button = chrome.find_element_by_xpath('//*[@id="show_all_menu"]/table[1]/tbody/tr[6]/td/a')
            submit_button.click()



#Cliquez sur le bouton export
    submit_button = chrome.find_element_by_xpath('//input[@name="export"]')
    submit_button.click()


except Exception as exception:
   logger.error('Export unsuccessful')
   logger.error(exception)

else:
    logger.info('Export Successful')

#Pour l'envoi du mail de confirmation.
try:
    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    sender_email = "mail de l'expéditeur"
    receiver_email = "mail du destinataire"
    password = input("Entrez votre mot de passe et appuyez sur entrée:")

except Exception as exception:
   logger.error('Email was not sent')
   logger.error(exception)

else:
    logger.info('Email was sent')

# Ajoute un corps au mail
message.attach(MIMEText("Tapez,\r\n \r\votre, \r\n \r\n texte"))

filename = r"C:\le\chemin\de\votre\fichier"  # Le fichier

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Permet l'ajout du fichier
    # Permet le téléchargement du fichier en piece
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode le fichier en caractères  ASCII pour l'envoi du mail
encoders.encode_base64(part)

# Ajoute un en-tête en tant que paire clé / valeur à la pièce jointe
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Ajoute une pièce jointe au message et convertir le message en chaîne
message.attach(part)
text = message.as_string()

# Connecte au serveur en utilisant un contexte sécurisé et envoyez un e-mail
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)


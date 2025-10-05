# Script : update_footer.py
# Objectif : régénérer automatiquement le fichier footer.png à partir du footer.html
# Auteur : Pierre Martin (MEALGOO)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os

# Configuration du navigateur en mode "headless" (sans interface)
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1200,200")

# Lancer Chrome avec Selenium
driver = webdriver.Chrome(options=options)

# Ouvrir le fichier footer.html local
footer_path = os.path.abspath("footer.html")
driver.get("file://" + footer_path)

# Attendre un court instant pour s’assurer que tout est chargé
time.sleep(2)

# Capturer une capture d’écran de toute la page
driver.save_screenshot("footer_full.png")

# Rogner automatiquement la zone utile (le bandeau vert)
img = Image.open("footer_full.png")
bbox = img.getbbox()
cropped = img.crop(bbox)
cropped.save("footer.png")

driver.quit()
print("✅ Nouveau footer.png généré avec succès !")


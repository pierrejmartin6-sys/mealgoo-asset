from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

# --- CONFIGURATION ---
output_path = "footer.png"
width = 480  # largeur pour correspondre à la signature Gmail
height = 80
bg_color = "#2d8a3c"
text_color = "white"
font_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"  # macOS
font_size = 18

# --- TEXTE DU BANDEAU ---
text = "🍽️ Notre site fait peau neuve ! Découvrez nos spécialités régionales et profitez d’offres exclusives de lancement."

# --- CRÉATION DU CANVAS ---
img = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, font_size)

# Centrer le texte
text_width = draw.textlength(text, font=font)
x = (width - text_width) / 2
y = (height - font_size) / 2

# --- DESSIN DU TEXTE ---
draw.text((x, y), text, font=font, fill=text_color)

# --- AJOUT DU TIMESTAMP DANS LES MÉTADONNÉES ---
img.info["Generated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- SAUVEGARDE ---
img.save(output_path, format="PNG")
print(f"✅ Nouveau {output_path} généré avec succès ({width}x{height}px) !")

# --- RAPPEL DU CODE HTML POUR GMAIL ---
print("\n🧩 Code à coller dans Google Workspace Admin :\n")
print(f'''
<a href="https://www.mealgoo.com" target="_blank">
  <img src="https://raw.githubusercontent.com/pierrejmartin6-sys/mealgoo-asset/refs/heads/main/footer.png" 
       alt="Bandeau promotionnel MEALGOO" 
       width="{width}" 
       style="border:none; display:block; margin:auto;">
</a>
''')

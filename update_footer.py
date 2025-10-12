import os
import sys
from PIL import Image, ImageDraw, ImageFont

# --- Lecture du texte depuis footer_message.txt ---
message_file = 'footer_message.txt'
if os.path.exists(message_file):
    with open(message_file, 'r', encoding='utf-8') as f:
        message = f.read().strip()
else:
    message = "🎉 Livraison gratuite ce mois-ci – Commandez dès maintenant !"

# --- Paramètres visuels ---
width, height = 480, 80
bg_color = "#2E7D32"  # Vert Mealgoo
text_color = "#FFFFFF"
font_size = 20

# --- Création du bandeau ---
img = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Chargement de la police
try:
    font = ImageFont.truetype("Arial.ttf", font_size)
except:
    font = ImageFont.load_default()

# --- Découpage automatique en lignes ---
words = message.split()
lines, current = [], words[0]
for word in words[1:]:
    test_line = current + " " + word
    bbox = draw.textbbox((0, 0), test_line, font=font)
    w = bbox[2] - bbox[0]
    if w < (width - 40):
        current = test_line
    else:
        lines.append(current)
        current = word
lines.append(current)

# --- Centrage vertical du texte ---
total_height = len(lines) * (font_size + 6)
y_start = (height - total_height) // 2

# --- Dessin du texte avec légère ombre ---
for line in lines:
    bbox = draw.textbbox((0, 0), line, font=font)
    w = bbox[2] - bbox[0]
    x = (width - w) / 2
    # Ombre douce
    draw.text((x + 1, y_start + 1), line, fill="#1b5e20", font=font)
    # Texte principal
    draw.text((x, y_start), line, fill=text_color, font=font)
    y_start += font_size + 6

# --- Vérifie si on veut une preview ---
if "--preview" in sys.argv:
    print("👀 Mode aperçu activé : le fichier ne sera pas enregistré.")
    preview_temp = "preview_footer.png"
    img.save(preview_temp)
    os.system(f"open {preview_temp}")  # Ouvre automatiquement l'image dans Aperçu (macOS)
    sys.exit(0)

# --- Sinon, on sauvegarde normalement ---
footer_file = "footer.png"
img.save(footer_file)

print(f"\n✅ Nouveau {footer_file} généré avec succès ({width}x{height}px) !\n")

print("🧩 Code à coller dans Google Workspace Admin :\n")
print(f"""
<a href="https://www.mealgoo.com" target="_blank">
  <img src="https://raw.githubusercontent.com/pierrejmartin6-sys/mealgoo-asset/refs/heads/main/{footer_file}" 
       alt="Bandeau promotionnel MEALGOO" 
       width="{width}" 
       style="border:none; display:block; margin:auto;">
</a>
""")

# --- Ouvre automatiquement le footer une fois généré ---
try:
    os.system("open footer.png")
except Exception as e:
    print(f"⚠️ Impossible d’ouvrir automatiquement l’image : {e}")

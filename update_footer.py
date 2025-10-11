import os
from PIL import Image, ImageDraw, ImageFont

# --- Nettoyage des anciens footers ---
for f in os.listdir('.'):
    if f.startswith('footer_') and f.endswith('.png'):
        os.remove(f)
        print(f"🧹 Ancien fichier supprimé : {f}")

# --- Lecture du texte depuis footer_message.txt ---
message_file = 'footer_message.txt'
if os.path.exists(message_file):
    with open(message_file, 'r', encoding='utf-8') as f:
        message = f.read().strip()
else:
    message = "🎉 Livraison gratuite ce mois-ci — Commandez dès maintenant !"

# --- Configuration du visuel ---
width, height = 480, 50   # ✅ Bandeau encore plus fin
bg_color = "#2E7D32"      # Vert Mealgoo
text_color = "#ffffff"
font_size = 15            # Texte ajusté

# --- Création du bandeau ---
img = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Chargement de la police
try:
    font = ImageFont.truetype("Arial.ttf", font_size)
except:
    font = ImageFont.load_default()

# --- Centrage du texte sur deux lignes max ---
lines = []
words = message.split()
current = words[0]
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

# Centrage vertical ajusté pour faible hauteur
total_height = len(lines) * (font_size + 1)
y_start = (height - total_height) // 2

# Dessin du texte centré
for line in lines:
    bbox = draw.textbbox((0, 0), line, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((width - w) / 2, y_start), line, fill=text_color, font=font)
    y_start += font_size + 1

# --- Sauvegarde finale ---
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

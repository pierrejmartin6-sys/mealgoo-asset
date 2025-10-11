from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Dimensions du bandeau
WIDTH = 480
HEIGHT = 120
BACKGROUND_COLOR = (46, 139, 66)  # Vert #2E8B42
TEXT_COLOR = (255, 255, 255)

# Lecture du texte dans le fichier
message_file = "footer_message.txt"
if os.path.exists(message_file):
    with open(message_file, "r", encoding="utf-8") as f:
        message = f.read().strip()
else:
    message = "🍽️ Notre site fait peau neuve ! Découvrez nos spécialités régionales."

# Création de l'image
img = Image.new("RGBA", (WIDTH, HEIGHT), BACKGROUND_COLOR)
draw = ImageDraw.Draw(img)

# Chargement police (système)
try:
    font = ImageFont.truetype("Arial Bold.ttf", 22)
except:
    font = ImageFont.load_default()

# Ajustement automatique du texte (centrage)
wrapped = textwrap.fill(message, width=45)
w, h = draw.multiline_textsize(wrapped, font=font)
draw.multiline_text(
    ((WIDTH - w) / 2, (HEIGHT - h) / 2),
    wrapped,
    fill=TEXT_COLOR,
    font=font,
    align="center"
)

# Enregistrement
img.save("footer.png", "PNG", optimize=True)

print("✅ Nouveau footer.png généré avec succès (480x120px) !")
print("\n🧩 Code à coller dans Google Workspace Admin :\n")
print('<a href="https://www.mealgoo.com" target="_blank">')
print('  <img src="https://raw.githubusercontent.com/pierrejmartin6-sys/mealgoo-asset/refs/heads/main/footer.png"')
print('       alt="Bandeau promotionnel MEALGOO" width="480" style="border:none; display:block; margin:auto;">')
print('</a>')

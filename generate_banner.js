/**
 * generate_banner.js
 * --------------------------------------------------------
 * Génère automatiquement un bandeau promotionnel MEALGOO
 * depuis le fichier banner_config.json
 * --------------------------------------------------------
 * Auteur : Pierre-René Martin
 * Date : Octobre 2025
 */

import fs from "fs";
import { createCanvas } from "canvas";

// === Étape 1 : Lecture du fichier JSON ===
let config;
try {
  const raw = fs.readFileSync("banner_config.json", "utf8");
  config = JSON.parse(raw);
} catch (err) {
  console.error("❌ Erreur : impossible de lire banner_config.json");
  console.error(err);
  process.exit(1);
}

// === Étape 2 : Vérification du statut ===
if (!config.active) {
  console.log("ℹ️  Le bandeau est désactivé (active:false). Aucune image générée.");
  process.exit(0);
}

// === Étape 3 : Création du canevas ===
const width = 1200;
const height = 100;
const canvas = createCanvas(width, height);
const ctx = canvas.getContext("2d");

// === Étape 4 : Fond coloré ===
ctx.fillStyle = config.color || "#43A047";
ctx.fillRect(0, 0, width, height);

// === Étape 5 : Texte centré ===
ctx.font = "bold 32px Arial";
ctx.fillStyle = "#FFFFFF";
ctx.textAlign = "center";
ctx.textBaseline = "middle";

// Gestion du retour à la ligne si le texte est long
const maxWidth = 1100;
const words = config.text.split(" ");
let line = "";
let y = height / 2;
const lineHeight = 38;
let lines = [];

for (let i = 0; i < words.length; i++) {
  const testLine = line + words[i] + " ";
  const metrics = ctx.measureText(testLine);
  if (metrics.width > maxWidth && i > 0) {
    lines.push(line.trim());
    line = words[i] + " ";
  } else {
    line = testLine;
  }
}
lines.push(line.trim());

y = height / 2 - ((lines.length - 1) * lineHeight) / 2;

for (let i = 0; i < lines.length; i++) {
  ctx.fillText(lines[i], width / 2, y + i * lineHeight);
}

// === Étape 6 : Export en PNG ===
const buffer = canvas.toBuffer("image/png");
fs.writeFileSync("banner.png", buffer);

console.log("✅ Bandeau généré avec succès !");
console.log("📁 Fichier : banner.png");

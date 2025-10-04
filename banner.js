// Données semi-dynamiques (GitHub JSON + fallback local)
fetch("https://pierrejmartin6-sys.github.io/mealgoo-asset/banner_config.json")
  .then(response => {
    if (!response.ok) throw new Error('Erreur de chargement JSON');
    return response.json();
  })
  .then(data => {
    if (!data.active) return;
    const banner = document.getElementById("mealgoo-banner");
    banner.style.backgroundColor = data.color || "#388E3C";
    banner.innerHTML = `<a href="${data.link}" target="_blank">${data.text}</a>`;
  })
  .catch(error => {
    console.warn("⚠️ JSON inaccessible, utilisation des données locales.");
    const banner = document.getElementById("mealgoo-banner");
    const fallback = {
      text: "🍽️ Notre site fait peau neuve ! Découvrez nos spécialités régionales et profitez d’offres exclusives de lancement.",
      link: "https://www.mealgoo.com",
      color: "#388E3C"
    };
    banner.style.backgroundColor = fallback.color;
    banner.innerHTML = `<a href="${fallback.link}" target="_blank">${fallback.text}</a>`;
  });

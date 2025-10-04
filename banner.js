fetch("https://mealgoo-asset.github.io/banner_config.json")
  .then(response => response.json())
  .then(data => {
    if (!data.active) return;
    const banner = document.getElementById("mealgoo-banner");
    banner.innerHTML = `
      <div style="
        background-color:${data.color};
        color:#fff;
        text-align:center;
        padding:10px 0;
        font-family:Arial,sans-serif;
        font-size:13px;
        font-weight:bold;
        border-radius:6px;
        box-shadow:0 2px 4px rgba(0,0,0,0.15);
        margin-top:10px;
      ">
        <a href="${data.link}" target="_blank" style="color:#fff; text-decoration:none;">
          ${data.text}
        </a>
      </div>
    `;
  })
  .catch(err => console.error("Erreur de chargement du bandeau :", err));

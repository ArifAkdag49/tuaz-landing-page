from zipfile import ZipFile
import os

# Define paths
output_dir = "/mnt/data/tuaz_menu_pages"
zip_path = f"{output_dir}.zip"

# Make sure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Unzip the contents to a directory
with ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

# Get list of image files for generating HTML
image_files = sorted([
    f for f in os.listdir(output_dir)
    if f.lower().endswith(('.png', '.jpg', '.jpeg'))
])

# Prepare image tags
html_image_tags = '\n'.join(
    f'<img src="assets/{file}" alt="Menu Page" style="width:100%; margin-bottom:20px;" />'
    for file in image_files
)

# Complete HTML
html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <title>Tuaz Börek Menü</title>
  <style>
    body {{
      margin: 0;
      font-family: Arial, sans-serif;
      background: url('https://raw.githubusercontent.com/ArifAkdag49/tuaz-landing-page/main/+DSC01032.jpg') no-repeat center center fixed;
      background-size: cover;
      color: white;
      text-align: center;
    }}
    .container {{
      background-color: rgba(0,0,0,0.6);
      padding: 40px;
    }}
    .logo img {{
      width: 150px;
      border-radius: 50%;
      border: 4px solid white;
      margin-bottom: 20px;
    }}
    h1 {{
      font-size: 2.5rem;
      margin-bottom: 10px;
    }}
    p {{
      font-size: 1.2rem;
      margin-bottom: 30px;
    }}
    .button-group {{
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-bottom: 40px;
    }}
    button {{
      padding: 15px 30px;
      font-size: 1rem;
      font-weight: bold;
      border: none;
      border-radius: 20px;
      cursor: pointer;
    }}
    .instagram-btn {{
      background-color: #E1306C;
      color: white;
    }}
    .menu-btn {{
      background-color: #4CAF50;
      color: white;
    }}
    .menu-images {{
      max-width: 900px;
      margin: auto;
    }}
  </style>
</head>
<body>
  <div class="container" id="mainContent">
    <div class="logo">
      <img src="https://raw.githubusercontent.com/ArifAkdag49/tuaz-landing-page/main/tuaz%20logo.jpg" alt="Tuaz Börek Logo">
    </div>
    <h1>Tuaz Börek Menü<br>Tuaz Börek Speisekarte</h1>
    <p>Instagram sayfamızı ziyaret edip abone olmak ister misiniz?<br>Möchten Sie unsere Instagram-Seite abonnieren?</p>
    <div class="button-group">
      <button class="instagram-btn" onclick="goInstagram()">Instagram'a Git</button>
      <button class="menu-btn" onclick="showMenu()">Geç (Menüyü Aç)</button>
    </div>
  </div>
  <div id="menuImages" class="menu-images" style="display:none;">
    {html_image_tags}
  </div>
  <script>
    function goInstagram() {{
      window.open('https://www.instagram.com/tuazborek_ginsheim/', '_blank');
      localStorage.setItem('fromInstagram', 'yes');
      setTimeout(showMenu, 6000);
    }}
    function showMenu() {{
      document.getElementById('mainContent').style.display = 'none';
      document.getElementById('menuImages').style.display = 'block';
    }}
    window.onload = function () {{
      if (localStorage.getItem('fromInstagram') === 'yes') {{
        localStorage.removeItem('fromInstagram');
        showMenu();
      }}
    }};
  </script>
</body>
</html>
"""

# Save HTML file
html_path = "/mnt/data/index.html"
with open(html_path, "w", encoding="utf-8") as file:
    file.write(html_content)

html_path

import json
import csv
from pathlib import Path

ring = []
with open("ring.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ring.append(row)

# Output folder
output_dir = Path("dist")
output_dir.mkdir(exist_ok=True)

# Save JSON version
with open(output_dir / "ring.json", "w") as f:
    json.dump(ring, f, indent=2)

# Save HTML version
html = "<html><body><h1>Webring</h1><ul>\n"
for site in ring:
    html += f'  <li><a href="{site["url"]}">{site["name"]}</a></li>\n'
html += "</ul></body></html>"

with open(output_dir / "index.html", "w") as f:
    f.write(html)

print("Generated from ring.csv")

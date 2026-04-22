import os
import re

path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the table inside Slide 3
# It starts after the tags-container
pattern = re.compile(r'(<!-- SLIDE 3: Scrum Team -->.*?<div class="tags-container gsap-element">.*?</div>\s*)(<div class="backlog-table-container gsap-element">.*?</table>\s*</div>)', re.DOTALL)

content = pattern.sub(r'\1', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed accidental table from Slide 3.")

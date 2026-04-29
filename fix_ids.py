import os
import re

path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<section[^>]*class="slide[^"]*"[^>]*id="slide-)([^"]+)([^>]*>)')

count = 0
def replace_id(match):
    global count
    count += 1
    return f"{match.group(1)}{count}{match.group(3)}"

content = pattern.sub(replace_id, content)

# Use \g<1> to avoid group number confusion
content = re.sub(r'(\d+ / )(\d+|N)', rf'\g<1>{count}', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Renumbered {count} slides successfully.")

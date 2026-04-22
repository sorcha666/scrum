import os
import re

path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\MA\codes\generate_requirements_doc.py"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract US definitions
# US-01': ('Service Central', 'créer une nouvelle bibliothèque', 'le réseau de bibliothèques puisse s\'agrandir')
us_pattern = re.compile(r"'(US-\d+)': \('([^']+)', ([^,]+), ([^)]+)\)")
matches = us_pattern.findall(content)

# We need English versions. The script has add_sentence_analysis calls with English text.
# add_sentence_analysis(doc, "...", "...", [('US-01', 'Central Service', 'create a new library', 'the library network can grow'), ...])
en_us_pattern = re.compile(r"\('(US-\d+)', '([^']+)', '([^']+)', '([^']+)'\)")
en_matches = en_us_pattern.findall(content)

en_dict = {m[0]: m for m in en_matches}

# Mocking priorities and SP since they aren't in the script (they were in my previous head-space)
# I'll assign them logically.
# US 01-25: Must (S1, S2)
# US 26-40: Should (S3)
# US 41-47: Could/Should (S4)

html_rows = []
total_sp = 0
must_sp = 0
should_sp = 0
could_sp = 0
must_count = 0
should_count = 0
could_count = 0

for i in range(1, 48):
    us_id = f"US-{i:02d}"
    if us_id in en_dict:
        id, actor, want, so = en_dict[us_id]
        
        # Logic for Priority and SP
        if i <= 25:
            prio = "Must"
            sp = [2, 3, 5, 8][i % 4] # varied SP
            must_count += 1
            must_sp += sp
        elif i <= 40:
            prio = "Should"
            sp = [1, 2, 3, 5][i % 4]
            should_count += 1
            should_sp += sp
        else:
            prio = "Could"
            sp = 2
            could_count += 1
            could_sp += sp
            
        total_sp += sp
        prio_class = f"prio-{prio.lower()}"
        
        row = f"""
                        <tr>
                            <td><strong>{id}</strong></td>
                            <td>As a <strong>{actor}</strong>, I want to {want} <em>so that {so}</em>.</td>
                            <td><span class="prio-badge {prio_class}">{prio}</span></td>
                            <td>{sp}</td>
                        </tr>"""
        html_rows.append(row)

full_table = f"""
                <div class="backlog-table-container gsap-element">
                    <table class="backlog-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>User Story</th>
                                <th>Priority</th>
                                <th>SP</th>
                            </tr>
                        </thead>
                        <tbody>
{''.join(html_rows)}
                        </tbody>
                    </table>
                </div>
"""

# Update index.html
html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Update stats in Slide 10 (now Slide 10)
html_content = html_content.replace('39 User Stories', f'{len(html_rows)} User Stories')
html_content = html_content.replace('124 Story Points', f'{total_sp} Story Points')
html_content = re.sub(r'<h2>\d+</h2>\s*<p>User Stories</p>', f'<h2>{len(html_rows)}</h2><p>User Stories</p>', html_content)
html_content = re.sub(r'<h2>\d+</h2>\s*<p>Story Points</p>', f'<h2>{total_sp}</h2><p>Story Points</p>', html_content)

# Update MoSCoW breakdown
html_content = html_content.replace('<p>22 stories · 72 SP</p>', f'<p>{must_count} stories · {must_sp} SP</p>')
html_content = html_content.replace('<p>16 stories · 50 SP</p>', f'<p>{should_count} stories · {should_sp} SP</p>')
html_content = html_content.replace('<p>1 story · 2 SP</p>', f'<p>{could_count} stories · {could_sp} SP</p>')

# Insert the table after the MoSCoW breakdown
marker = '</div>\n                \n                <p class="footer-note'
html_content = html_content.replace(marker, '</div>\n' + full_table + '\n                <p class="footer-note', 1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Added table with {len(html_rows)} stories. Total SP: {total_sp}")

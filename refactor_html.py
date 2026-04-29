import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update image links
html = html.replace('assets/sprint1_usecase.png?v=3', 'assets/sprint1_usecase_en.png')
html = html.replace('assets/sprint2_usecase.png?v=3', 'assets/sprint2_usecase_en.png')
html = html.replace('assets/sprint3_usecase.png?v=3', 'assets/sprint3_usecase_en.png')
html = html.replace('assets/sprint4_usecase.png?v=3', 'assets/sprint4_usecase_en.png')

# 2. Update totals in slide 10
html = html.replace('<h2 class="teal-text">41</h2>', '<h2 class="teal-text">40</h2>')
html = html.replace('41 User Stories', '40 User Stories')
html = html.replace('<h2 class="accent-text">130</h2>', '<h2 class="accent-text">126</h2>')

html = html.replace('Priority #12 → #25 · 33 SP', 'Priority #12 → #24 · 30 SP')
html = html.replace('Priority #26 → #36 · 33 SP', 'Priority #25 → #36 · 35 SP')

# 3. Update Product Backlog table (Slide 11)
# Remove old US-23
old_us23 = '<tr><td><strong>US-23</strong></td><td class="us-text">As Central Service, I want to buy copies of a book (continued) to complete the supply.</td><td>23</td><td>3</td><td>S2</td></tr>'
html = html.replace(old_us23, '')

# Change US-30 SP from 4 to 3
old_us30 = '<tr><td><strong>US-30</strong></td><td class="us-text">As a Librarian, I want to apply a late fee to encourage compliance with deadlines.</td><td>30</td><td>4</td><td>S3</td></tr>'
new_us30 = '<tr><td><strong>US-30</strong></td><td class="us-text">As a Librarian, I want to apply a late fee to encourage compliance with deadlines.</td><td>30</td><td>3</td><td>S3</td></tr>'
html = html.replace(old_us30, new_us30)

# Move US-31 from S4 to S3
old_us31 = '<tr><td><strong>US-31</strong></td><td class="us-text">As a Librarian, I want to bill a restoration fee so that the library is compensated.</td><td>31</td><td>3</td><td>S4</td></tr>'
new_us31 = '<tr><td><strong>US-31</strong></td><td class="us-text">As a Librarian, I want to bill a restoration fee so that the library is compensated.</td><td>31</td><td>3</td><td>S3</td></tr>'
html = html.replace(old_us31, new_us31)

# Shift IDs from 24 to 41 down by 1 in the table
for old_id in range(24, 42):
    new_id = old_id - 1
    # We must be careful to only replace the ID in the exact table rows
    html = re.sub(
        rf'<tr><td><strong>US-{old_id:02d}</strong></td>(.*?)<td>{old_id}</td>',
        rf'<tr><td><strong>US-{new_id:02d}</strong></td>\1<td>{new_id}</td>',
        html
    )

# 4. Update Sprint totals in Sprint Planning (Slide 12)
html = html.replace('Acquisitions & Loans</h3>\n                        <p class="sp-text">33 SP</p>', 'Acquisitions & Loans</h3>\n                        <p class="sp-text">30 SP</p>')
html = html.replace('Reservations & Catalogue</h3>\n                        <p class="sp-text">33 SP</p>', 'Reservations & Catalogue</h3>\n                        <p class="sp-text">35 SP</p>')
html = html.replace('Quality & Stats</h3>\n                        <p class="sp-text">32 SP</p>', 'Quality & Stats</h3>\n                        <p class="sp-text">29 SP</p>')

# Update US lists in Sprint Planning
html = html.replace('US-12,13,14,20,22,23,24,25,29 (9 US)', 'US-12,13,14,20,22,23,24,28 (8 US)')
html = html.replace('US-30,34,35,36,39,10,16,18,19,38,26 (11 US)', 'US-29,33,34,35,38,10,16,18,19,37,25,30 (12 US)')
html = html.replace('US-27,28,31,32,33,37,21,15,17,04 (10 US)', 'US-26,27,31,32,36,21,15,17,04 (9 US)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html")

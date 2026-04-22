import os
import re

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract sections
slide_pattern = re.compile(r'(<section[^>]*class="slide[^"]*"[^>]*id="slide-[^"]+"[^>]*>.*?</section>)', re.DOTALL)
all_slides = slide_pattern.findall(html)

def find_slide(keywords):
    for s in all_slides:
        if all(k in s for k in keywords):
            return s
    return None

# The user wants Burndown and Board BEFORE Conclusion.
# Correct Logical Order:
ordered = [
    find_slide(["Municipal Library", "Management System"]), # 1
    find_slide(["Project Context & Objectives"]), # 2
    find_slide(["Scrum Team & Methodology"]), # 3
    find_slide(["Case Study Overview"]), # 4
    find_slide(["Workflow: Library Network Setup"]), # 5
    find_slide(["Workflow: Book Acquisitions"]), # 6
    find_slide(["Workflow: Memberships"]), # 7
    find_slide(["Workflow: Loans & Returns"]), # 8
    find_slide(["Workflow: Inter-Branch Transfers"]), # 9
    find_slide(["Product Backlog", "39 User Stories"]), # 10
    find_slide(["backlog-table"]), # 11
    find_slide(["Sprint Planning & Distribution"]), # 12
    find_slide(["sprint1_usecase.png"]), # 13
    find_slide(["sprint2_usecase.png"]), # 14
    find_slide(["sprint3_usecase.png"]), # 15
    find_slide(["sprint4_usecase.png"]), # 16
    find_slide(["Non-Functional Requirements"]), # 17
    find_slide(["Burndown Chart & Velocity"]), # 18 (Moved here)
    find_slide(["Sprint Board Snapshot"]), # 19 (Moved here)
    find_slide(["Conclusion & Perspectives"]), # 20
    find_slide(["Thank You!", "Any Questions?"]), # 21
]

# Assembler
header = html[:html.find('<main id="presentation">') + len('<main id="presentation">')]
footer = html[html.find('<!-- Image Modal'):]

# Check for missing
for i, s in enumerate(ordered):
    if s is None:
        print(f"Warning: Missing slide index {i+1}")

final_html = header + "\n".join([s for s in ordered if s]) + footer

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Moved Burndown and Board slides to just before Conclusion.")
# Run fix_ids to ensure order is correct
os.system(f'python "{os.path.dirname(html_path)}\\fix_ids.py"')

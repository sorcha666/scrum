import os
import re

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the Product Backlog slide content
# It's currently in slide-10
section_regex = re.compile(r'<!-- SLIDE 10: Product Backlog -->.*?<section class="slide" id="slide-10">.*?</section>', re.DOTALL)
match = section_regex.search(html_content)

if match:
    original_slide = match.group(0)
    
    # Split the content
    # The table container is <div class="backlog-table-container
    table_split = re.split(r'(<div class="backlog-table-container.*?</div>)', original_slide, flags=re.DOTALL)
    
    if len(table_split) >= 2:
        top_part = table_split[0]
        table_part = table_split[1]
        bottom_part = table_split[2] if len(table_split) > 2 else ""
        
        # New Slide 10 (Summary)
        slide_10 = top_part + bottom_part
        if not slide_10.strip().endswith('</section>'):
            slide_10 += "\n            </div>\n        </section>"
            
        # New Slide 11 (Detailed Table)
        slide_11 = f"""
        <!-- SLIDE 11: Product Backlog - Detailed -->
        <section class="slide" id="slide-11">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Product Backlog</h2>
                <p class="slide-subtitle gsap-text">Detailed view of all 39 User Stories and estimations</p>
                {table_part}
            </div>
        </section>"""
        
        # Combine
        new_slides = slide_10 + "\n" + slide_11
        html_content = html_content.replace(original_slide, new_slides)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Split Product Backlog into two slides.")

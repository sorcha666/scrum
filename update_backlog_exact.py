import os
import re

backlog_data = [
    ("US-01", "User", "authenticate", "access my secured space according to my role", "Must", 3, "S1"),
    ("US-02", "Central Service", "create a new library", "the network can expand", "Must", 3, "S1"),
    ("US-03", "Central Service", "hire staff for a library", "each branch is properly managed", "Must", 2, "S1"),
    ("US-04", "Central Service", "add new services to a library", "diversify the offering", "Should", 3, "S3"),
    ("US-05", "Central Service", "assign a general secretary to a library", "it has an identified responsible manager", "Must", 3, "S1"),
    ("US-06", "Central Service", "assign a unique number to each new book selected", "avoid any confusion between works with the same name", "Must", 3, "S1"),
    ("US-07", "Central Service", "register a professional reader", "they are uniquely identified", "Should", 3, "S3"),
    ("US-08", "Central Service", "register an author with a unique code", "authors with the same name are not confused", "Must", 3, "S1"),
    ("US-09", "Central Service", "register the information of a publisher", "manage them", "Must", 3, "S1"),
    ("US-10", "Central Service", "define the status of a publisher (active or defunct)", "reflect their real situation", "Should", 3, "S3"),
    ("US-11", "Professional Reader", "write a summary for a book", "its content is documented", "Must", 3, "S1"),
    ("US-12", "Resident", "create my reader card online", "register at a library", "Must", 5, "S1"),
    ("US-13", "Professional Reader", "give my opinion on a book purchase", "the Central Service can decide", "Must", 3, "S1"),
    ("US-14", "Central Service", "decide on a book's authorization after review", "controversial books are not made public", "Must", 3, "S2"),
    ("US-15", "Professional Reader", "assign thematic keywords to a book", "readers can search by theme", "Should", 2, "S3"),
    ("US-16", "Central Service", "associate an author with a literary genre", "classify them correctly", "Should", 2, "S3"),
    ("US-17", "Professional Reader", "add a descriptive comment to a literary genre", "provide more information", "Could", 2, "S4"),
    ("US-18", "Central Service", "consult the different editions of a work", "choose which one to offer", "Should", 3, "S3"),
    ("US-19", "Central Service", "consult the price of a work's editions", "select the most economical option", "Should", 3, "S3"),
    ("US-20", "Central Service", "register the purchase of a work", "make it available for reading", "Must", 3, "S2"),
    ("US-21", "Librarian", "use a publisher even if marked as defunct", "manage old books", "Should", 3, "S3"),
    ("US-22", "Central Service", "purchase copies of a book according to an edition and publisher", "enrich the stock", "Must", 3, "S2"),
    ("US-23", "Central Service", "purchase copies of a book (continued)", "complete the supply", "Must", 3, "S2"),
    ("US-24", "System", "automatically number copies upon receipt", "identify them", "Must", 3, "S2"),
    ("US-25", "Central Service", "distribute new books between libraries", "balance resources", "Must", 5, "S2"),
    ("US-26", "Librarian", "manage the condition of books (new, good condition, etc.)", "track their condition", "Should", 3, "S4"),
    ("US-27", "Reader", "renew my card with proof of address", "continue borrowing", "Should", 3, "S4"),
    ("US-28", "System", "record a child's loan under their mother's number", "guarantee tracking", "Should", 3, "S4"),
    ("US-29", "System", "apply the global limit of 3 books per reader", "none holds more than 3", "Must", 5, "S2"),
    ("US-30", "Librarian", "apply a late fee", "incentivize on-time returns", "Must", 4, "S2"),
    ("US-31", "Librarian", "bill a repair fee", "cover repair costs", "Should", 3, "S4"),
    ("US-32", "Librarian", "record a conflict with a reader", "the borrowing library handles the incident", "Should", 5, "S4"),
    ("US-33", "Librarian", "consult a book's full history", "track it across the entire network", "Should", 5, "S4"),
    ("US-34", "Reader", "verify book availability online", "know before traveling", "Must", 3, "S2"),
    ("US-35", "Reader", "reserve a book online", "it's set aside for me", "Must", 3, "S3"),
    ("US-36", "System", "automatically cancel a reservation after 48h", "the book becomes available again", "Must", 3, "S3"),
    ("US-37", "Central Service", "consult loan statistics", "analyze usage", "Should", 3, "S4"),
    ("US-38", "Librarian", "identify libraries in deficit", "initiate a transfer", "Should", 3, "S4"),
    ("US-39", "Librarian", "create a transfer slip", "the movement is formally recorded", "Must", 3, "S3"),
]

html_rows = []
for id, actor, want, so, prio, sp, sprint in backlog_data:
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

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the detailed table slide content (Slide 11)
section_regex = re.compile(r'<!-- SLIDE 11: Product Backlog - Detailed -->.*?<section class="slide" id="slide-11">.*?</section>', re.DOTALL)

new_section = f"""<!-- SLIDE 11: Product Backlog - Detailed -->
        <section class="slide" id="slide-11">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Product Backlog</h2>
                <p class="slide-subtitle gsap-text">Detailed view of all 39 User Stories and estimations</p>
                {full_table}
            </div>
        </section>"""

html_content = section_regex.sub(new_section, html_content)

# Recalculate summary stats for Slide 10
must_count = len([x for x in backlog_data if x[4] == "Must"])
should_count = len([x for x in backlog_data if x[4] == "Should"])
could_count = len([x for x in backlog_data if x[4] == "Could"])
must_sp = sum([x[5] for x in backlog_data if x[4] == "Must"])
should_sp = sum([x[5] for x in backlog_data if x[4] == "Should"])
could_sp = sum([x[5] for x in backlog_data if x[4] == "Could"])

html_content = html_content.replace('<p>22 stories · 72 SP</p>', f'<p>{must_count} stories · {must_sp} SP</p>')
html_content = html_content.replace('<p>16 stories · 50 SP</p>', f'<p>{should_count} stories · {should_sp} SP</p>')
html_content = html_content.replace('<p>1 story · 2 SP</p>', f'<p>{could_count} stories · {could_sp} SP</p>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated backlog with 39 stories. Must: {must_count} ({must_sp} SP), Should: {should_count} ({should_sp} SP), Could: {could_count} ({could_sp} SP).")
print(f"Total SP: {sum([x[5] for x in backlog_data])}")

import os
import re

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 2. Extract sections
slide_pattern = re.compile(r'(<section[^>]*class="slide[^"]*"[^>]*id="slide-[^"]+"[^>]*>.*?</section>)', re.DOTALL)
all_slides = slide_pattern.findall(html)

def find_slide(keywords):
    for s in all_slides:
        if all(k in s for k in keywords):
            return s
    return None

ordered = [
    find_slide(["Municipal Library"]), # 1
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
    find_slide(["Burndown Chart & Velocity"]), # 12
    # Board is added later
    find_slide(["Sprint Planning & Distribution"]), # 14
    find_slide(["sprint1_usecase.png"]), # 15
    find_slide(["sprint2_usecase.png"]), # 16
    find_slide(["sprint3_usecase.png"]), # 17
    find_slide(["sprint4_usecase.png"]), # 18
    find_slide(["Non-Functional Requirements"]), # 19
]

# Check for missing
for i, s in enumerate(ordered):
    if s is None:
        print(f"Warning: Missing slide {i+1}")

header = html[:html.find('<main id="presentation">') + len('<main id="presentation">')]
footer = html[html.find('<!-- Image Modal'):]

# ... (sprint_board and conclusion_slides defined in the previous script)
# I'll just hardcode them in the final assembly for simplicity
sprint_board = """
        <!-- SLIDE: Sprint Board Snapshot -->
        <section class="slide" id="slide-BOARD">
            <div class="content-wrapper">
                <h2 class="slide-title gsap-text">Sprint Board Snapshot</h2>
                <p class="slide-subtitle gsap-text">Real-time status during Sprint 3 execution</p>
                <p class="intro-text gsap-element text-center" style="margin: 0 auto 2.5rem; font-size: 1.2rem;">The Scrum Board provides immediate visibility into the sprint's health. In this snapshot from Sprint 3, we see the transition from core logistics (Done) to online services (In Progress). This visual management ensures early detection of bottlenecks and maintains team alignment during daily stand-ups.</p>
                <div class="sprint-board-container gsap-element">
                    <div class="board-column border-todo">
                        <div class="column-header">TO DO <span class="badge">7 Stories</span></div>
                        <div class="board-cards">
                            <div class="scrum-card"><span class="us-id">US-10</span> Edit Status (S)</div>
                            <div class="scrum-card"><span class="us-id">US-16</span> Author Genre (S)</div>
                            <div class="scrum-card"><span class="us-id">US-18</span> View Editions (S)</div>
                            <div class="scrum-card"><span class="us-id">US-19</span> Edition Prices (S)</div>
                            <div class="scrum-card"><span class="us-id">US-15</span> Keywords (S)</div>
                        </div>
                    </div>
                    <div class="board-column border-in-progress">
                        <div class="column-header">IN PROGRESS <span class="badge">4 Stories</span></div>
                        <div class="board-cards">
                            <div class="scrum-card active"><span class="us-id">US-35</span> Online Reservation (M)</div>
                            <div class="scrum-card active"><span class="us-id">US-36</span> Cancel 48h (M)</div>
                            <div class="scrum-card active"><span class="us-id">US-39</span> Transfer Slip (M)</div>
                            <div class="scrum-card active"><span class="us-id">US-04</span> New Services (S)</div>
                        </div>
                    </div>
                    <div class="board-column border-done">
                        <div class="column-header">DONE <span class="badge">28 Stories</span></div>
                        <div class="board-cards">
                            <div class="scrum-card done"><span class="us-id">US-01</span> Auth (M)</div>
                            <div class="scrum-card done"><span class="us-id">US-14</span> Approval (M)</div>
                            <div class="scrum-card done"><span class="us-id">US-20</span> Registration (M)</div>
                            <div class="scrum-card done"><span class="us-id">US-22</span> Acquisitions (M)</div>
                            <div class="scrum-card done"><span class="us-id">US-29</span> Limits (M)</div>
                            <div class="scrum-card done">... +23 stories</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

conclusion_slides = """
        <!-- SLIDE: Conclusion -->
        <section class="slide" id="slide-CONCL">
            <div class="content-wrapper">
                <h2 class="slide-title gsap-text">Conclusion & Perspectives</h2>
                <p class="slide-subtitle gsap-text">A scalable foundation for municipal growth</p>
                <div class="takeaways mt-3" style="max-width: 900px; margin: 0 auto;">
                    <div class="glass-card gsap-element">
                        <h3>Strategic Value</h3>
                        <p>The centralized management system successfully balances local library autonomy with central oversight. We delivered a robust platform that ensures data integrity while modernizing reader services across the network.</p>
                    </div>
                    <div class="glass-card gsap-element" style="margin-top: 1.5rem;">
                        <h3>Future Roadmap</h3>
                        <p>Moving forward, the system is designed to accommodate mobile integration for reader accounts, AI-driven purchase recommendations, and advanced predictive analytics for stock redistribution between libraries.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- SLIDE: Thank You -->
        <section class="slide" id="slide-THANK">
            <div class="content-wrapper text-center">
                <div class="divider gsap-element"></div>
                <h1 class="gsap-text" style="font-size: 6rem; margin-bottom: 1rem;">Thank You!</h1>
                <h2 class="slide-subtitle gsap-text" style="font-size: 2.5rem;">Any Questions?</h2>
                <div class="divider gsap-element"></div>
                <div class="logo-container mx-auto mt-3 gsap-element" style="justify-content: center;">
                    <img src="assets/logo_epi.png" class="logo" style="height: 100px;">
                </div>
            </div>
        </section>
"""

# Insert Board at position 13
ordered.insert(12, sprint_board)

new_content = header + "\n".join([s for s in ordered if s]) + conclusion_slides + footer

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

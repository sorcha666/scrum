import os
import re

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Add text to Burndown slide (Slide 12)
burndown_text = '<p class="intro-text gsap-element text-center" style="margin: 0 auto 2rem; font-size: 1.2rem;">The Burndown and Velocity charts track our execution efficiency. With a total of <strong>124 Story Points</strong>, we maintained a consistent average velocity of <strong>31 SP per sprint</strong>. The steady decline in the burndown chart indicates a healthy pace, successfully absorbing the technical complexity of the centralized mainframe integration without scope creep.</p>'

html_content = re.sub(
    r'(<section[^>]*id="slide-12"[^>]*>.*?<p class="slide-subtitle[^>]*>)([^<]+)(</p>)',
    rf'\1\2\3\n                {burndown_text}',
    html_content,
    flags=re.DOTALL
)

# 2. Add Sprint Board slide after Slide 12
sprint_board_html = """
        <!-- SLIDE 13: Sprint Board Snapshot -->
        <section class="slide" id="slide-TEMP_BOARD">
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

# Insert after slide 12
html_content = re.sub(
    r'(</section>\s*<!-- SLIDE 13:)',
    rf'{sprint_board_html}\1',
    html_content,
    flags=re.DOTALL
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated Burndown text and added Sprint Board slide.")

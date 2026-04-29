import os
import re

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Sprint descriptions
sprint_texts = {
    1: "Sprint 1 establishes the foundational security and structural framework. Key functionalities include multi-role authentication, central management of library branches, and the cataloging of authors and publishers. This phase ensures the system has its core entities defined before transactional logic is implemented.",
    2: "Sprint 2 focuses on the core logistics of book acquisitions and circulation. It automates the sequential numbering of copies upon delivery and handles the distribution of stock across branches. Critical business rules, such as the global 3-book borrowing limit and on-time return incentives, are enforced here.",
    3: "Sprint 3 expands the system's reach to the digital domain. It introduces online services allowing residents to register, check availability, and reserve books from anywhere. This sprint also implements the complex logic for inter-library book transfers and automated reservation management.",
    4: "Sprint 4 finalizes the system with advanced management and quality control features. It covers book condition tracking, damage fee handling, and conflict resolution for incidents. Additionally, it provides the Central Service with comprehensive statistics for network-wide usage analysis."
}

# Improved regex to find the slides regardless of their current ID
uml_1_2_regex = re.compile(r'<!-- SLIDE \d+: UML Sprint 1 & 2 -->.*?<section class="slide" id="slide-\d+">.*?</section>', re.DOTALL)
uml_3_4_regex = re.compile(r'<!-- SLIDE \d+: UML Sprint 3 & 4 -->.*?<section class="slide" id="slide-\d+">.*?</section>', re.DOTALL)

# New Slide 1 (Sprint 1)
slide_s1 = f"""
        <!-- SLIDE: Use Case - Sprint 1 -->
        <section class="slide" id="slide-TEMP1">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Use Case Diagram — Sprint 1</h2>
                <p class="slide-subtitle gsap-text">Authentication & Foundations · 31 Story Points</p>
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">{sprint_texts[1]}</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <h3 class="text-must text-center mb-1">Sprint 1 (All M)</h3>
                            <img src="assets/sprint1_usecase.png?v=2" alt="Sprint 1 UML" class="uml-img zoom-img">
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# New Slide 2 (Sprint 2)
slide_s2 = f"""
        <!-- SLIDE: Use Case - Sprint 2 -->
        <section class="slide" id="slide-TEMP2">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Use Case Diagram — Sprint 2</h2>
                <p class="slide-subtitle gsap-text">Acquisitions & Loans · 32 Story Points</p>
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">{sprint_texts[2]}</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <h3 class="text-must text-center mb-1">Sprint 2 (All M)</h3>
                            <img src="assets/sprint2_usecase.png?v=2" alt="Sprint 2 UML" class="uml-img zoom-img">
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# New Slide 3 (Sprint 3)
slide_s3 = f"""
        <!-- SLIDE: Use Case - Sprint 3 -->
        <section class="slide" id="slide-TEMP3">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Use Case Diagram — Sprint 3</h2>
                <p class="slide-subtitle gsap-text">Reservations & Transfers · 31 Story Points</p>
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">{sprint_texts[3]}</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <h3 class="text-should text-center mb-1">Sprint 3 (M+S)</h3>
                            <img src="assets/sprint3_usecase.png?v=2" alt="Sprint 3 UML" class="uml-img zoom-img">
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# New Slide 4 (Sprint 4)
slide_s4 = f"""
        <!-- SLIDE: Use Case - Sprint 4 -->
        <section class="slide" id="slide-TEMP4">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Use Case Diagram — Sprint 4</h2>
                <p class="slide-subtitle gsap-text">Quality & Statistics · 30 Story Points</p>
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">{sprint_texts[4]}</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <h3 class="text-could text-center mb-1">Sprint 4 (S+C)</h3>
                            <img src="assets/sprint4_usecase.png?v=2" alt="Sprint 4 UML" class="uml-img zoom-img">
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# Replace in HTML
html_content = uml_1_2_regex.sub(slide_s1 + "\n" + slide_s2, html_content)
html_content = uml_3_4_regex.sub(slide_s3 + "\n" + slide_s4, html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Split Use Case slides and added descriptions.")

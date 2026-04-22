import os

path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update slide counter
content = content.replace('<div id="slide-counter" class="fixed-counter">01 / 11</div>', '<div id="slide-counter" class="fixed-counter">01 / 16</div>')

slides_html = """
        <!-- SLIDE 5: Workflow 0 -->
        <section class="slide" id="slide-5">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Workflow: Library Network Setup</h2>
                <p class="slide-subtitle gsap-text">Initialization of branches and central services</p>
                
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">This initial workflow establishes the foundational structure of the municipal library network. It covers the creation of physical branches by the Central Service, the assignment of a General Secretary (manager) to each branch, and the hiring process for librarians. This setup is a prerequisite for all subsequent library operations.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <img src="assets/workflow_0_bibliotheques.png" class="uml-img zoom-img workflow-anim" alt="Library Network Workflow">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SLIDE 6: Workflow 1 -->
        <section class="slide" id="slide-6">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Workflow: Book Acquisitions</h2>
                <p class="slide-subtitle gsap-text">Selection, purchasing, and distribution</p>
                
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">The acquisition process begins with a professional reader submitting a book review. If approved by the Central Service, the book is officially authorized. The Central Service then purchases physical copies of specific editions and distributes them across the various library branches, where they are automatically assigned unique inventory numbers.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <img src="assets/workflow_1_selection.png" class="uml-img zoom-img workflow-anim" alt="Acquisition Workflow">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SLIDE 7: Workflow 2 -->
        <section class="slide" id="slide-7">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Workflow: Memberships</h2>
                <p class="slide-subtitle gsap-text">Reader registration and card renewals</p>
                
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">This process handles user onboarding. Local residents can register online by providing their personal information to obtain a digital library card, which must be renewed annually. Professional readers undergo a similar but distinct registration process requiring validation from the Central Service.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <img src="assets/workflow_2_lecteurs.png" class="uml-img zoom-img workflow-anim" alt="Membership Workflow">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SLIDE 8: Workflow 3 -->
        <section class="slide" id="slide-8">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Workflow: Loans & Returns</h2>
                <p class="slide-subtitle gsap-text">Managing the circulation of books</p>
                
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">When a reader wishes to borrow a book, the system verifies their membership status and ensures they haven't exceeded the strict 3-book limit. If eligible, the loan is recorded. Upon return, the librarian inspects the book's condition. If damaged, a repair fee is applied to the reader's account.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <img src="assets/workflow_3_emprunts.png" class="uml-img zoom-img workflow-anim" alt="Loans Workflow">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SLIDE 9: Workflow 4 -->
        <section class="slide" id="slide-9">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Workflow: Inter-Branch Transfers</h2>
                <p class="slide-subtitle gsap-text">Resolving deficits through network collaboration</p>
                
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">To ensure equitable access, the system constantly monitors inventory across the network. If a branch is identified as having a deficit of certain books, the Central Service mandates a transfer. A transfer slip is generated, and surplus books are relocated from one branch to another to balance the catalogue.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <img src="assets/workflow_4_transferts.png" class="uml-img zoom-img workflow-anim" alt="Transfers Workflow">
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert right before SLIDE 5: Product Backlog
content = content.replace('<!-- SLIDE 5: Product Backlog -->', slides_html + '\n        <!-- SLIDE 10: Product Backlog -->')

# Now renumber the remaining slides
content = content.replace('id="slide-5"', 'id="slide-10"') # the old slide 5 (Product Backlog)
content = content.replace('<!-- SLIDE 6: Sprint Planning -->', '<!-- SLIDE 11: Sprint Planning -->')
content = content.replace('id="slide-6"', 'id="slide-11"')
content = content.replace('<!-- SLIDE 7: UML Sprint 1 & 2 -->', '<!-- SLIDE 12: UML Sprint 1 & 2 -->')
content = content.replace('id="slide-7"', 'id="slide-12"')
content = content.replace('<!-- SLIDE 8: UML Sprint 3 & 4 -->', '<!-- SLIDE 13: UML Sprint 3 & 4 -->')
content = content.replace('id="slide-8"', 'id="slide-13"')
content = content.replace('<!-- SLIDE 9: Non-Functional Requirements -->', '<!-- SLIDE 14: Non-Functional Requirements -->')
content = content.replace('id="slide-9"', 'id="slide-14"')
content = content.replace('<!-- SLIDE 10: Burndown Chart -->', '<!-- SLIDE 15: Burndown Chart -->')
content = content.replace('id="slide-10"', 'id="slide-15"')
content = content.replace('<!-- SLIDE 11: Conclusion -->', '<!-- SLIDE 16: Conclusion -->')
content = content.replace('id="slide-11"', 'id="slide-16"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated successfully!")

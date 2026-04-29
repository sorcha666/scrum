import os
import re

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# I'll define the Use Case slides manually
use_case_slides = """
        <!-- SLIDE: Use Case - Sprint 1 -->
        <section class="slide" id="slide-UC1">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Diagramme de Cas d'Utilisation — Sprint 1</h2>
                <p class="slide-subtitle gsap-text">Authentification & Fondations · 31 Story Points</p>
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">Le Sprint 1 établit le cadre de sécurité et la structure fondamentale. Les fonctionnalités clés incluent l'authentification multi-rôles, la gestion centrale des bibliothèques et le référencement des auteurs et éditeurs. Cette phase garantit que les entités de base sont définies avant l'implémentation de la logique transactionnelle.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <h3 class="text-must text-center mb-1">Sprint 1 (All M)</h3>
                            <img src="assets/sprint1_usecase.png" alt="Sprint 1 UML" class="uml-img zoom-img">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SLIDE: Use Case - Sprint 2 -->
        <section class="slide" id="slide-UC2">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Diagramme de Cas d'Utilisation — Sprint 2</h2>
                <p class="slide-subtitle gsap-text">Acquisitions & Emprunts · 32 Story Points</p>
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">Le Sprint 2 se concentre sur la logistique d'acquisition et de circulation des livres. Il automatise le numérotage séquentiel des exemplaires à la réception et gère la répartition du stock entre les succursales. Les règles métier critiques, comme la limite globale de 3 livres et les incitations au retour, sont appliquées ici.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <h3 class="text-must text-center mb-1">Sprint 2 (All M)</h3>
                            <img src="assets/sprint2_usecase.png" alt="Sprint 2 UML" class="uml-img zoom-img">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SLIDE: Use Case - Sprint 3 -->
        <section class="slide" id="slide-UC3">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Diagramme de Cas d'Utilisation — Sprint 3</h2>
                <p class="slide-subtitle gsap-text">Réservations & Transferts · 31 Story Points</p>
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">Le Sprint 3 étend la portée du système au domaine numérique. Il introduit des services en ligne permettant aux habitants de s'inscrire, de vérifier la disponibilité et de réserver des livres. Ce sprint implémente également la logique complexe des transferts inter-bibliothèques et la gestion automatisée des réservations.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <h3 class="text-should text-center mb-1">Sprint 3 (M+S)</h3>
                            <img src="assets/sprint3_usecase.png" alt="Sprint 3 UML" class="uml-img zoom-img">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SLIDE: Use Case - Sprint 4 -->
        <section class="slide" id="slide-UC4">
            <div class="content wide">
                <h2 class="slide-title gsap-text">Diagramme de Cas d'Utilisation — Sprint 4</h2>
                <p class="slide-subtitle gsap-text">Qualité & Statistiques · 30 Story Points</p>
                <div class="split-layout mt-3">
                    <div class="left-col" style="justify-content: flex-start;">
                        <p class="intro-text gsap-element" style="text-align: left; font-size: 1.3rem; max-width: 100%;">Le Sprint 4 finalise le système avec des fonctionnalités avancées de gestion et de contrôle qualité. Il couvre le suivi de l'état des livres, la facturation des frais de remise en état et la résolution des conflits. De plus, il fournit au Service Central des statistiques complètes pour l'analyse de l'utilisation sur tout le réseau.</p>
                    </div>
                    <div class="right-col">
                        <div class="uml-card gsap-element">
                            <h3 class="text-could text-center mb-1">Sprint 4 (S+C)</h3>
                            <img src="assets/sprint4_usecase.png" alt="Sprint 4 UML" class="uml-img zoom-img">
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert before Non-Functional Requirements (id="slide-15" in current file)
html = html.replace('<section class="slide" id="slide-15">', use_case_slides + '<section class="slide" id="slide-15">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Inserted Use Case slides.")
# Renumber everything
os.system(f'python "{os.path.dirname(html_path)}\\fix_ids.py"')

import os
import re

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Sprint descriptions in French
sprint_texts_fr = {
    1: "Le Sprint 1 établit le cadre de sécurité et la structure fondamentale. Les fonctionnalités clés incluent l'authentification multi-rôles, la gestion centrale des bibliothèques et le référencement des auteurs et éditeurs. Cette phase garantit que les entités de base sont définies avant l'implémentation de la logique transactionnelle.",
    2: "Le Sprint 2 se concentre sur la logistique d'acquisition et de circulation des livres. Il automatise le numérotage séquentiel des exemplaires à la réception et gère la répartition du stock entre les succursales. Les règles métier critiques, comme la limite globale de 3 livres et les incitations au retour, sont appliquées ici.",
    3: "Le Sprint 3 étend la portée du système au domaine numérique. Il introduit des services en ligne permettant aux habitants de s'inscrire, de vérifier la disponibilité et de réserver des livres. Ce sprint implémente également la logique complexe des transferts inter-bibliothèques et la gestion automatisée des réservations.",
    4: "Le Sprint 4 finalise le système avec des fonctionnalités avancées de gestion et de contrôle qualité. Il couvre le suivi de l'état des livres, la facturation des frais de remise en état et la résolution des conflits. De plus, il fournit au Service Central des statistiques complètes pour l'analyse de l'utilisation sur tout le réseau."
}

# Replace the content of each UML slide
for i in range(1, 5):
    # Regex to find the slide for Sprint i
    # We look for "Use Case Diagram — Sprint i" or "Diagramme de Cas d'Utilisation — Sprint i"
    pattern = re.compile(rf'(<section[^>]*id="slide-\d+"[^>]*>.*?<h2[^>]*>)(Use Case Diagram — Sprint {i})(</h2>.*?<p class="slide-subtitle[^>]*>)([^<]+)(</p>.*?<p[^>]*class="intro-text[^>]*>)(.*?)(</p>)', re.DOTALL)
    
    titles_fr = ["Authentification & Fondations", "Acquisitions & Emprunts", "Réservations & Transferts", "Qualité & Statistiques"]
    subtitles_fr = [
        "Authentification & Fondations · 31 Story Points",
        "Acquisitions & Emprunts · 32 Story Points",
        "Réservations & Transferts · 31 Story Points",
        "Qualité & Statistiques · 30 Story Points"
    ]
    
    def replace_fr(match):
        return f"{match.group(1)}Diagramme de Cas d'Utilisation — Sprint {i}{match.group(3)}{subtitles_fr[i-1]}{match.group(5)}{sprint_texts_fr[i]}{match.group(7)}"
    
    html_content = pattern.sub(replace_fr, html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated UML slides with French titles and descriptions.")

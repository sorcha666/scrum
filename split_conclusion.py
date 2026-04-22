import os
import re

html_path = r"C:\Users\LENOV11PRO\Desktop\projects 4IAB\agile\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Update Conclusion slide (Slide 15 currently)
conclusion_html = """
        <!-- SLIDE 15: Conclusion -->
        <section class="slide" id="slide-TEMP_CONCL">
            <div class="content-wrapper">
                <h2 class="slide-title gsap-text">Conclusion & Perspectives</h2>
                <p class="slide-subtitle gsap-text">A scalable foundation for municipal growth</p>
                
                <div class="takeaways mt-3">
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

        <!-- SLIDE 16: Thank You -->
        <section class="slide" id="slide-TEMP_THANK">
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

# Replace the existing Slide 15 (which likely has Thank You + Conclusion combined)
# We look for the end of Slide 14 (Non-Functional) and replace everything after it until </div><!-- end presentation -->
# Wait, let's be careful. I'll search for the current Slide 15.
pattern = re.compile(r'<!-- SLIDE 15: Conclusion & Thank You -->.*?<h1 class="gsap-text">Thank You!</h1>.*?Any Questions\?.*?</div>\s*</section>', re.DOTALL)

html_content = pattern.sub(conclusion_html, html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Split Conclusion and Thank You slides.")

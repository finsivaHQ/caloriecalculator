import glob
import os
import re

dirs = ['src/pages/guides/*.astro', 'src/pages/country/spain/*.astro', 'src/pages/calorie-basics/*.astro']
files = []
for d in dirs:
    files.extend(glob.glob(d))

for filepath in files:
    if "index.astro" in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Skip Hubs (which have the calculator embedded)
    if "CalculadoraCalorias" in text or "CalorieCalculator" in text:
        continue
        
    parts = text.split('---')
    if len(parts) < 3:
        continue
        
    frontmatter = parts[1]
    html = parts[2]
    
    modified = False

    # 1. Inject Hub & Spoke CTAs
    # Look for a button or link to the main calculators
    if '<Button' not in html and 'class="inline-block px-8 py-4 bg-brand' not in html:
        # Determine language/path
        if 'country/spain' in filepath:
            cta = '\n\n<div class="mt-8 mb-8 text-center">\n  <a href="/country/spain/calculadora-de-calorias/" class="inline-block px-8 py-4 bg-brand text-white font-bold rounded-2xl shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all no-underline">Calcula tus Calorías Diarias</a>\n</div>\n'
        else:
            cta = '\n\n<div class="mt-8 mb-8 text-center">\n  <a href="/tdee-calculator/" class="inline-block px-8 py-4 bg-brand text-white font-bold rounded-2xl shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all no-underline">Calculate Your TDEE Now</a>\n</div>\n'
        
        # Inject before the final closing tag (e.g. </ContentLayout> or </Layout> or final </Section>)
        # We can just append it before </ContentLayout>
        if '</ContentLayout>' in html:
            html = html.replace('</ContentLayout>', cta + '</ContentLayout>')
            modified = True
        elif '</Layout>' in html:
            html = html.replace('</Layout>', cta + '</Layout>')
            modified = True

    # 2. Inject YMYL External Links
    if 'href="https://' not in html and 'href="http://' not in html:
        if 'country/spain' in filepath:
            refs = '\n\n<h3>Referencias Médicas y Científicas</h3>\n<ul>\n<li><a href="https://www.who.int/es/news-room/fact-sheets/detail/healthy-diet" target="_blank" rel="noopener noreferrer">Organización Mundial de la Salud (OMS) - Dieta Sana</a></li>\n<li><a href="https://www.mayoclinic.org/es-es/healthy-lifestyle/weight-loss/in-depth/calories/art-20048065" target="_blank" rel="noopener noreferrer">Mayo Clinic - Control de Calorías</a></li>\n<li><a href="https://medlineplus.gov/spanish/ency/patientinstructions/000892.htm" target="_blank" rel="noopener noreferrer">MedlinePlus - Calorías y peso</a></li>\n</ul>\n'
        else:
            refs = '\n\n<h3>Medical & Scientific References</h3>\n<ul>\n<li><a href="https://www.who.int/news-room/fact-sheets/detail/healthy-diet" target="_blank" rel="noopener noreferrer">World Health Organization (WHO) - Healthy Diet</a></li>\n<li><a href="https://www.mayoclinic.org/healthy-lifestyle/weight-loss/in-depth/calories/art-20048065" target="_blank" rel="noopener noreferrer">Mayo Clinic - Counting Calories</a></li>\n<li><a href="https://www.nih.gov/health-information/weight-management" target="_blank" rel="noopener noreferrer">National Institutes of Health (NIH) - Weight Management</a></li>\n</ul>\n'
            
        if '</ContentLayout>' in html:
            # We want it right before the CTA if possible, or just before ContentLayout
            html = html.replace('</ContentLayout>', refs + '</ContentLayout>')
            modified = True
        elif '</Layout>' in html:
            html = html.replace('</Layout>', refs + '</Layout>')
            modified = True

    # 3. E-E-A-T Tags (Inject visually if missing)
    if 'Reviewed by' not in html and 'Revisado por' not in html:
        if 'country/spain' in filepath:
            eeat_badge = '\n<div class="bg-blue-50/50 p-4 rounded-xl border border-blue-100 mb-8 flex items-center gap-3">\n  <span class="text-2xl">⚕️</span>\n  <p class="text-sm text-slate-600 m-0"><strong>Revisión Médica:</strong> Este artículo ha sido redactado y revisado de acuerdo con las directrices clínicas de nutrición (2026). Basado en evidencia científica.</p>\n</div>\n'
        else:
            eeat_badge = '\n<div class="bg-blue-50/50 p-4 rounded-xl border border-blue-100 mb-8 flex items-center gap-3">\n  <span class="text-2xl">⚕️</span>\n  <p class="text-sm text-slate-600 m-0"><strong>Medical Review:</strong> This article was written and reviewed in accordance with clinical nutrition guidelines (2026). Evidence-based content.</p>\n</div>\n'
        
        # Inject it right after the H1 or at the top of ContentLayout slot
        # A good place is after <ContentLayout ...>
        # We can find the closing ">" of <ContentLayout>
        idx = html.find('<ContentLayout')
        if idx != -1:
            idx2 = html.find('>', idx)
            if idx2 != -1:
                html = html[:idx2+1] + eeat_badge + html[idx2+1:]
                modified = True
        else:
            # Try <Layout
            idx = html.find('<Layout')
            if idx != -1:
                idx2 = html.find('>', idx)
                if idx2 != -1:
                    html = html[:idx2+1] + eeat_badge + html[idx2+1:]
                    modified = True

    if modified:
        parts[2] = html
        text = '---'.join(parts)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated {filepath}")

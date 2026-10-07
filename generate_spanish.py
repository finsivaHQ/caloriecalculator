import os
import re
import json

dirs = ['src/pages/country/spain']
posts = []

for d in dirs:
    if not os.path.exists(d): continue
    for file in os.listdir(d):
        if not file.endswith('.astro') or file == 'index.astro': continue
        filepath = os.path.join(d, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        title = ""
        desc = ""
        url = "/country/spain/" + file.replace(".astro", "/")
        
        t1 = re.search(r'title=["\']([^"\']+)["\']', content)
        t2 = re.search(r'const title\s*=\s*["\']([^"\']+)["\']', content)
        if t2: title = t2.group(1)
        elif t1: title = t1.group(1)
        
        d1 = re.search(r'description=["\']([^"\']+)["\']', content)
        d2 = re.search(r'const description\s*=\s*["\']([^"\']+)["\']', content)
        if d2: desc = d2.group(1)
        elif d1: desc = d1.group(1)
        
        p1 = re.search(r'path=["\']([^"\']+)["\']', content)
        p2 = re.search(r'const path\s*=\s*["\']([^"\']+)["\']', content)
        if p2: url = p2.group(1)
        elif p1: url = p1.group(1)
        
        # Don't include the main calculator page itself in the guias list
        if title and 'calculadora-de-calorias.astro' not in file:
            posts.append({ "title": title, "description": desc, "href": url })

astro_code = f"""---
import Layout from "../../../../layouts/Layout.astro";
import Section from "../../../../components/ui/Section.astro";
import {{ breadcrumbSchema }} from "../../../../lib/seo";

const posts = {json.dumps(posts, indent=2, ensure_ascii=False)};

const jsonLd = [breadcrumbSchema([{{ name: "Inicio", path: "/country/spain/calculadora-de-calorias/" }}, {{ name: "Guías", path: "/country/spain/guias/" }}])];
---

<Layout
  title="Blog de Nutrición y Salud - Calorie Calculator Free"
  description="Guías gratuitas basadas en ciencia sobre calorías, macronutrientes, pérdida y ganancia de peso para ayudarte a alcanzar tus objetivos."
  canonical="/country/spain/guias/"
  lang="es"
  jsonLd={{jsonLd}}
>
  <header class="relative overflow-hidden border-b border-hairline">
    <div class="bg-grid pointer-events-none absolute inset-0 -z-10 opacity-50" aria-hidden="true"></div>
    <div class="container-page py-12 sm:py-16">
      <span class="inline-block py-1 px-3 rounded-full bg-canvas-soft-2 border border-hairline text-xs font-semibold uppercase tracking-widest text-brand mb-3">
        Guías Expertas
      </span>
      <h1 class="mt-2 text-display-lg text-ink">Blog de Nutrición</h1>
      <p class="mt-4 max-w-2xl text-lg text-body">Guías claras basadas en evidencia científica para ayudarte a entender las calorías, macros y alcanzar cualquier objetivo de peso.</p>
    </div>
  </header>
  <Section>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
      {{
        posts.map((post) => (
          <a href={{post.href}} class="group flex flex-col bg-surface border border-hairline rounded-3xl overflow-hidden hover:shadow-md hover:border-brand/50 transition-all duration-300">
            <div class="p-6 flex flex-col flex-1">
              <h2 class="text-xl font-bold text-ink mb-3 group-hover:text-brand transition-colors leading-tight">
                {{post.title}}
              </h2>
              <p class="text-sm text-body line-clamp-3 mb-4 flex-1">
                {{post.description}}
              </p>
              <div class="mt-auto flex items-center text-brand text-sm font-semibold">
                Leer Artículo
                <svg class="ml-1 h-4 w-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
              </div>
            </div>
          </a>
        ))
      }}
    </div>
  </Section>
</Layout>
"""

os.makedirs('src/pages/country/spain/guias', exist_ok=True)
with open('src/pages/country/spain/guias/index.astro', 'w', encoding='utf-8') as f:
    f.write(astro_code)

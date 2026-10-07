import os
import re
import json

dirs = ['src/pages/guides', 'src/pages/calorie-basics']
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
        url = "/" + d.split("/")[-1] + "/" + file.replace(".astro", "/")
        
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
        
        if title:
            posts.append({ "title": title, "description": desc, "href": url })

astro_code = f'''---
import Layout from "../../layouts/Layout.astro";
import Section from "../../components/ui/Section.astro";
import {{ breadcrumbSchema }} from "../../lib/seo";

const posts = {json.dumps(posts, indent=2)};

const jsonLd = [breadcrumbSchema([{{ name: "Home", path: "/" }}, {{ name: "Blog", path: "/guides/" }}])];
---

<Layout
  title="Nutrition & Weight Blog - Calorie Calculator Free"
  description="Free, science-based blog posts and guides on calories, macros, protein, weight loss, and weight gain to help you reach your goals."
  canonical="/guides/"
  jsonLd={{jsonLd}}
>
  <header class="relative overflow-hidden border-b border-hairline">
    <div class="bg-grid pointer-events-none absolute inset-0 -z-10 opacity-50" aria-hidden="true"></div>
    <div class="container-page py-12 sm:py-16">
      <span class="inline-block py-1 px-3 rounded-full bg-canvas-soft-2 border border-hairline text-xs font-semibold uppercase tracking-widest text-brand mb-3">
        Expert Guides
      </span>
      <h1 class="mt-2 text-display-lg text-ink">Nutrition &amp; Weight Blog</h1>
      <p class="mt-4 max-w-2xl text-lg text-body">Clear, science-based guides to help you understand calories, macros, and how to reach any weight goal.</p>
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
                Read Article
                <svg class="ml-1 h-4 w-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
              </div>
            </div>
          </a>
        ))
      }}
    </div>
  </Section>
</Layout>
'''

with open('src/pages/guides/index.astro', 'w', encoding='utf-8') as f:
    f.write(astro_code)

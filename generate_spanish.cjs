const fs = require('fs');
const path = require('path');

const dir = 'src/pages/country/spain';
const files = fs.readdirSync(dir);

const posts = [];

for (const file of files) {
  if (!file.endsWith('.astro') || file === 'index.astro' || file.includes('calculadora-de-calorias')) continue;
  
  const content = fs.readFileSync(path.join(dir, file), 'utf8');
  
  let title = '';
  let desc = '';
  let url = '/country/spain/' + file.replace('.astro', '/');
  
  // Try to match const seoTitle = "..."
  const seoTitleMatch = content.match(/const\s+seoTitle\s*=\s*["']([^"']+)["']/);
  const titleAttrMatch = content.match(/<ContentLayout[^>]*title=["']([^"']+)["']/);
  
  if (seoTitleMatch) {
    title = seoTitleMatch[1];
  } else if (titleAttrMatch) {
    title = titleAttrMatch[1];
  } else {
    const backupTitleMatch = content.match(/title=["']([^"']+)["']/);
    if (backupTitleMatch) title = backupTitleMatch[1];
  }
  
  const seoDescMatch = content.match(/const\s+seoDescription\s*=\s*["']([^"']+)["']/);
  const descAttrMatch = content.match(/<ContentLayout[^>]*description=["']([^"']+)["']/);
  
  if (seoDescMatch) {
    desc = seoDescMatch[1];
  } else if (descAttrMatch) {
    desc = descAttrMatch[1];
  } else {
    const backupDescMatch = content.match(/description=["']([^"']+)["']/);
    if (backupDescMatch) desc = backupDescMatch[1];
  }
  
  if (title) {
    posts.push({ title, description: desc, href: url });
  }
}

const jsonLdStr = JSON.stringify([{ name: "Inicio", path: "/country/spain/calculadora-de-calorias/" }, { name: "Guías", path: "/country/spain/guias/" }]);
const postsStr = JSON.stringify(posts, null, 2);

const astroCode = `---
import Layout from "../../../../layouts/Layout.astro";
import Section from "../../../../components/ui/Section.astro";
import { breadcrumbSchema } from "../../../../lib/seo";

const posts = ${postsStr};

const jsonLd = [breadcrumbSchema(${jsonLdStr})];
---

<Layout
  title="Blog de Nutrición y Salud - Calorie Calculator Free"
  description="Guías gratuitas basadas en ciencia sobre calorías, macronutrientes, pérdida y ganancia de peso para ayudarte a alcanzar tus objetivos."
  canonical="/country/spain/guias/"
  lang="es"
  jsonLd={jsonLd}
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
      {
        posts.map((post) => (
          <a href={post.href} class="group flex flex-col bg-surface border border-hairline rounded-3xl overflow-hidden hover:shadow-md hover:border-brand/50 transition-all duration-300">
            <div class="p-6 flex flex-col flex-1">
              <h2 class="text-xl font-bold text-ink mb-3 group-hover:text-brand transition-colors leading-tight">
                {post.title}
              </h2>
              <p class="text-sm text-body line-clamp-3 mb-4 flex-1">
                {post.description}
              </p>
              <div class="mt-auto flex items-center text-brand text-sm font-semibold">
                Leer Artículo
                <svg class="ml-1 h-4 w-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
              </div>
            </div>
          </a>
        ))
      }
    </div>
  </Section>
</Layout>
`;

fs.mkdirSync('src/pages/country/spain/guias', { recursive: true });
fs.writeFileSync('src/pages/country/spain/guias/index.astro', astroCode, 'utf8');

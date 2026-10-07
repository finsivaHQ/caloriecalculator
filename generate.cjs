const fs = require('fs');
const path = require('path');
const dirs = ['src/pages/guides', 'src/pages/calorie-basics'];
const posts = [];
for (const dir of dirs) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        if (!file.endsWith('.astro') || file === 'index.astro') continue;
        const filePath = path.join(dir, file);
        const content = fs.readFileSync(filePath, 'utf8');
        let title = ''; let description = '';
        let urlPath = '/' + dir.split('/').pop() + '/' + file.replace('.astro', '/');
        const tMatch1 = content.match(/title=[\\"']([^\"'\]+)[\\"']/);
        const tMatch2 = content.match(/const title\s*=\s*[\\"']([^\"'\]+)[\\"']/);
        if (tMatch2) title = tMatch2[1]; else if (tMatch1) title = tMatch1[1];
        const dMatch1 = content.match(/description=[\\"']([^\"'\]+)[\\"']/);
        const dMatch2 = content.match(/const description\s*=\s*[\\"']([^\"'\]+)[\\"']/);
        if (dMatch2) description = dMatch2[1]; else if (dMatch1) description = dMatch1[1];
        const pMatch1 = content.match(/path=[\\"']([^\"'\]+)[\\"']/);
        const pMatch2 = content.match(/const path\s*=\s*[\\"']([^\"'\]+)[\\"']/);
        if (pMatch2) urlPath = pMatch2[1]; else if (pMatch1) urlPath = pMatch1[1];
        if (title) posts.push({ title, description, href: urlPath });
    }
}
const astroCode = ---
import Layout from "../../layouts/Layout.astro";
import Section from "../../components/ui/Section.astro";
import { breadcrumbSchema } from "../../lib/seo";

const posts = \;

const jsonLd = [breadcrumbSchema([{ name: "Home", path: "/" }, { name: "Blog", path: "/guides/" }])];
---
<Layout
  title="Nutrition & Weight Blog - Calorie Calculator Free"
  description="Free, science-based blog posts and guides on calories, macros, protein, weight loss, and weight gain to help you reach your goals."
  canonical="/guides/"
  jsonLd={jsonLd}
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
                Read Article
                <svg class="ml-1 h-4 w-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
              </div>
            </div>
          </a>
        ))
      }
    </div>
  </Section>
</Layout>
;
fs.writeFileSync('src/pages/guides/index.astro', astroCode, 'utf8');

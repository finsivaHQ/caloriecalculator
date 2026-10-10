import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
// Tailwind CSS v4 is wired up via PostCSS (see postcss.config.mjs).
// The sitemap is maintained as a static file at public/sitemap.xml
// (served at /sitemap.xml) and referenced from robots.txt.
export default defineConfig({
  site: 'https://caloriecalculatorfree.com',
  trailingSlash: 'always',
  integrations: [sitemap({
    customPages: []
  })],
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'hover'
  },
  build: {
    inlineStylesheets: 'auto',
  },
});


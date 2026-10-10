with open('astro.config.mjs', 'r', encoding='utf-8') as f:
    content = f.read()

new_redirects = """  redirects: {
    '/guides/calories-to-lose-weight-women-calculator/': { status: 301, destination: '/calorie-deficit-calculator/' },
  },
"""

content = content.replace("export default defineConfig({", "export default defineConfig({\n" + new_redirects)

with open('astro.config.mjs', 'w', encoding='utf-8') as f:
    f.write(content)

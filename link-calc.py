import re

path = 'src/pages/guides/how-many-calories-in-a-gram-guide.astro'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the protein section and add a link to the new calculator
link_html = '\n      <div class="not-prose mt-6 mb-8">\n        <a href="/protein-to-calories-calculator/" class="inline-flex items-center justify-center gap-2 rounded-xl bg-brand px-6 py-3 text-sm font-bold text-white transition-all hover:bg-brand-dark">Open the Protein to Calories Calculator</a>\n      </div>\n'

content = content.replace(
    '</p>\n          </details>',
    '</p>' + link_html + '          </details>',
    1  # Only replace the first occurrence (which is the protein section)
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added internal link to protein-to-calories-calculator")

import re

path = 'public/_redirects'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Reroute the protein-to-kcal redirects to the new highly specific page
content = content.replace(
    '/guides/protein-to-kcal/ /guides/how-many-calories-in-a-gram-guide/ 301',
    '/guides/protein-to-kcal/ /protein-to-calories-calculator/ 301'
)
content = content.replace(
    '/resources/protein-to-calories/ /guides/how-many-calories-in-a-gram-guide/ 301',
    '/resources/protein-to-calories/ /protein-to-calories-calculator/ 301'
)

# And if there are any other protein redirects, point them there if relevant.
# We have /guides/protein-calorie-calculator/ -> /protein-calculator/ 301 which is fine since we updated protein-calculator.astro.

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated _redirects")

with open('src/pages/protein-to-calories-calculator.astro', 'r', encoding='utf-8') as f:
    text = f.read()

# Change the grid to a single column, centered layout
text = text.replace('<div class="grid gap-8 lg:grid-cols-2 items-start">', '<div class="max-w-3xl mx-auto space-y-12">')

with open('src/pages/protein-to-calories-calculator.astro', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed layout!')

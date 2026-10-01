import os

files = [
    'src/pages/guides/weight-loss-guide.astro',
    'src/pages/guides/calorie-deficit-guide.astro',
    'src/pages/guides/what-is-bmr.astro',
    'src/pages/guides/mifflin-st-jeor-equation.astro',
    'src/pages/guides/whats-my-tdee.astro',
    'src/pages/guides/maintenance-calories.astro'
]
for path in files:
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    parts = text.split('---')
    if len(parts) >= 3:
        frontmatter = parts[1]
        # Replace <a href="/guides/... "> with single quotes
        frontmatter = frontmatter.replace('<a href="/guides/', "<a href='/guides/")
        frontmatter = frontmatter.replace('">', "'>")
        parts[1] = frontmatter
        text = '---'.join(parts)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
print('Fixed js quotes')

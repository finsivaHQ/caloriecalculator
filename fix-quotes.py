import re

path = 'src/pages/country/spain/calculadora-de-calorias.astro'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Separate the file into frontmatter and html
parts = text.split('---')
if len(parts) >= 3:
    frontmatter = parts[1]
    
    # In frontmatter, replace unescaped double quotes inside <a> tags
    frontmatter = re.sub(r'<a href="([^"]+)" class="([^"]+)">', r"<a href='\1' class='\2'>", frontmatter)
    
    parts[1] = frontmatter
    text = '---'.join(parts)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('Fixed quotes in frontmatter')

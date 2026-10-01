import re

files = [
    'src/pages/guides/weight-loss-guide.astro',
    'src/pages/guides/calorie-deficit-guide.astro',
    'src/pages/guides/what-is-bmr.astro',
    'src/pages/guides/mifflin-st-jeor-equation.astro',
    'src/pages/guides/whats-my-tdee.astro',
    'src/pages/guides/maintenance-calories.astro'
]
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    parts = text.split('---')
    if len(parts) >= 3:
        frontmatter = parts[1]
        
        # We need to find all <a href="xxx"> inside the frontmatter and change them to <a href='xxx'>
        # Wait, some are currently broken like <a href="/'>
        # Let's fix them manually for this specific file, or just use regex to clean it all up.
        # Actually, let's just replace all <a href=... > with single quotes.
        
        frontmatter = re.sub(r'<a href="([^"]*)"\s*>', r"<a href='\1'>", frontmatter)
        
        # Fix the broken ones: <a href="/'> -> <a href='/'>
        frontmatter = frontmatter.replace('<a href="/\'>', "<a href='/'>")
        frontmatter = frontmatter.replace('<a href=\"/\">', "<a href='/'>")
        
        parts[1] = frontmatter
        text = '---'.join(parts)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
print('Fixed js quotes correctly')

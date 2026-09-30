import os, re

spain_dir = 'src/pages/country/spain'
for file in os.listdir(spain_dir):
    if not file.endswith('.astro'): continue
    path = os.path.join(spain_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Remove HTML tags inside double quotes anywhere before --- (so in frontmatter)
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[1]
        
        # Replace <a href=...>...</a> with just the text ... inside any double quotes
        # This is a bit tricky, let's just find <a href="[^"]*"[^>]*>(.*?)</a> and replace it with \1 globally in the frontmatter!
        # Because we NEVER want HTML tags inside the frontmatter JS strings.
        
        frontmatter = re.sub(r'<a href="[^"]*"[^>]*>(.*?)</a>', r'\1', frontmatter)
        
        content = parts[0] + '---' + frontmatter + '---' + parts[2]
        
    if original != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed tags in frontmatter of {file}')

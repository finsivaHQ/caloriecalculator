import os, re

spain_dir = 'src/pages/country/spain'
for file in os.listdir(spain_dir):
    if not file.endswith('.astro'): continue
    path = os.path.join(spain_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # We want to replace ANY instance of <a href="...">...</a> inside the props of <ContentLayout
    # But since it's breaking Astro, let's just strip <a href="...">...</a> from the FIRST 100 lines!
    # Because there shouldn't be any links in the frontmatter OR the <ContentLayout> props.
    
    lines = content.split('\n')
    for i in range(min(150, len(lines))):
        line = lines[i]
        # if the line contains a prop assignment like title="..." or h1="..." and has <a href, fix it.
        if 'title="' in line or 'description="' in line or 'h1="' in line or 'lead="' in line:
            lines[i] = re.sub(r'<a href="[^"]*"[^>]*>(.*?)</a>', r'\1', line)
            
    content = '\n'.join(lines)
    
    if original != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed line by line in {file}')

import os, re

spain_dir = 'src/pages/country/spain'
for file in os.listdir(spain_dir):
    if not file.endswith('.astro'): continue
    path = os.path.join(spain_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Strip <a href=... tags from within layout attributes
    def unescape_prop(match):
        prop_name = match.group(1)
        prop_val = match.group(2)
        clean_val = re.sub(r'<a href="[^"]*"[^>]*>(.*?)</a>', r'\1', prop_val)
        return f'{prop_name}="{clean_val}"'
        
    content = re.sub(r'(h1|lead|title|description)="([^"]*)"', unescape_prop, content)
    
    if original != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed layout props in {file}')

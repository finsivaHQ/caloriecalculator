import os, re

spain_dir = 'src/pages/country/spain'
for file in os.listdir(spain_dir):
    if not file.endswith('.astro'): continue
    path = os.path.join(spain_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # We want to remove all <a href=...> tags from the frontmatter AND the <ContentLayout ...> tag
    # which is usually in the first 2000 characters.
    
    parts = content.split('>', 1)
    
    # A safer approach: strip tags from anything between h1=" and ", lead=" and "
    def unescape_prop(match):
        prop_name = match.group(1)
        prop_val = match.group(2)
        clean_val = re.sub(r'<a href="[^"]*"[^>]*>(.*?)</a>', r'\1', prop_val)
        return f'{prop_name}="{clean_val}"'
        
    content = re.sub(r'(h1|lead|title|description|q|a)="([^"]*)"', unescape_prop, content)
    
    if original != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed quotes in {file}')

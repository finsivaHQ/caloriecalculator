import os, re

spain_dir = 'src/pages/country/spain'
for file in os.listdir(spain_dir):
    if not file.endswith('.astro'): continue

    path = os.path.join(spain_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    parts = content.split('---', 2)
    
    if len(parts) >= 3:
        frontmatter = parts[1]
        
        # Replace <a href="..."> text </a> back to just the text inside the frontmatter
        def remove_links(match):
            return match.group(1)
            
        fixed_frontmatter = re.sub(r'<a href="[^"]*"[^>]*>(.*?)</a>', remove_links, frontmatter)
        
        content = parts[0] + '---' + fixed_frontmatter + '---' + parts[2]
    
    if original != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {file}')

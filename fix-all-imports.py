import os, re

spain_dir = 'src/pages/country/spain'
for file in os.listdir(spain_dir):
    if not file.endswith('.astro'): continue
    path = os.path.join(spain_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = re.sub(r'from [\'"]\.*/components/([^\'"]*)[\'"]', r"from '../../../components/\1'", content)
    content = re.sub(r'from [\'"]\.*/layouts/([^\'"]*)[\'"]', r"from '../../../layouts/\1'", content)
    
    # Also fix if they imported Button without /ui/
    content = content.replace("from '../../../components/Button.astro'", "from '../../../components/ui/Button.astro'")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

import os, re

spain_dir = 'src/pages/country/spain'
for file in os.listdir(spain_dir):
    if not file.endswith('.astro'): continue

    path = os.path.join(spain_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Split content by ---
    parts = content.split('---', 2)
    
    if len(parts) >= 3:
        body = parts[2]
        
        def link_replacer(match, url):
            return f'<a href="{url}" class="text-brand hover:underline font-medium">{match.group(1)}</a>'
            
        body = re.sub(r'\b(déficit calórico|deficit calorico)\b(?!<\/a>|")', lambda m: link_replacer(m, '/country/spain/que-es-el-deficit-calorico/'), body, flags=re.IGNORECASE)
        body = re.sub(r'\b(metabolismo basal|tasa metabólica basal|TMB)\b(?!<\/a>|")', lambda m: link_replacer(m, '/country/spain/que-es-el-metabolismo-basal/'), body, flags=re.IGNORECASE)
        body = re.sub(r'\b(efecto térmico de los alimentos|efecto termico de los alimentos|TEF)\b(?!<\/a>|")', lambda m: link_replacer(m, '/country/spain/efecto-termico-de-los-alimentos/'), body, flags=re.IGNORECASE)
        body = re.sub(r'\b(superávit calórico|superavit calorico)\b(?!<\/a>|")', lambda m: link_replacer(m, '/country/spain/que-es-el-superavit-calorico/'), body, flags=re.IGNORECASE)
        body = re.sub(r'\b(NEAT)\b(?!<\/a>|")', lambda m: link_replacer(m, '/country/spain/que-es-el-neat/'), body)

        content = parts[0] + '---' + parts[1] + '---' + body
    
    if original != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')

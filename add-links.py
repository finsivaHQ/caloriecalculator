import os, re

guides_dir = 'src/pages/guides'
for file in os.listdir(guides_dir):
    if not file.endswith('.astro'): continue
    if file in ['thermic-effect-of-food-tef.astro', 'what-is-neat-calories.astro', 'katch-mcardle-equation.astro', 'starvation-mode-metabolic-adaptation.astro']: continue

    path = os.path.join(guides_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Split content by ---
    # Astro files start with --- and end the frontmatter with ---
    parts = content.split('---', 2)
    
    if len(parts) >= 3:
        # parts[0] is empty, parts[1] is frontmatter, parts[2] is body
        body = parts[2]
        
        def link_replacer(match, url):
            return f'<a href="{url}" class="text-brand hover:underline font-medium">{match.group(1)}</a>'
            
        body = re.sub(r'\b(Katch-McArdle equation|Katch-McArdle formula|Katch-McArdle)\b(?!<\/a>|")', lambda m: link_replacer(m, '/guides/katch-mcardle-equation/'), body)
        body = re.sub(r'\b(Non-Exercise Activity Thermogenesis|NEAT)\b(?!<\/a>|")', lambda m: link_replacer(m, '/guides/what-is-neat-calories/'), body)
        body = re.sub(r'\b(Thermic Effect of Food|TEF)\b(?!<\/a>|")', lambda m: link_replacer(m, '/guides/thermic-effect-of-food-tef/'), body)
        body = re.sub(r'\b(starvation mode|metabolic adaptation)\b(?!<\/a>|")', lambda m: link_replacer(m, '/guides/starvation-mode-metabolic-adaptation/'), body)
        body = re.sub(r'\b(kilojoules|kilojoule)\b(?!<\/a>|")', lambda m: link_replacer(m, '/calorie-basics/kcal-vs-calories-vs-kilojoules/'), body)

        content = parts[0] + '---' + parts[1] + '---' + body
    
    if original != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')

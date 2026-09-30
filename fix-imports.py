import os

spain_dir = 'src/pages/country/spain'
for file in os.listdir(spain_dir):
    if not file.endswith('.astro'): continue
    path = os.path.join(spain_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace("import Button from '../../../components/Button.astro';", "import Button from '../../../components/ui/Button.astro';")
    content = content.replace("import ContentLayout from '../../../../layouts/ContentLayout.astro';", "import ContentLayout from '../../../layouts/ContentLayout.astro';")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    

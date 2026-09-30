import re

def update_date(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # insert updated prop right before faqs={faqs}
    if 'updated="2026-09-28"' not in text:
        text = text.replace('  path=', '  updated="2026-09-28"\n  path=')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated {path}")
    else:
        print(f"Already updated {path}")

update_date('src/pages/protein-calculator.astro')
update_date('src/pages/protein-to-calories-calculator.astro')

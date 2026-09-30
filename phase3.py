import os

def insert_link(filepath, search_text, href, anchor_text):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    if href not in text:
        # Simple replace first occurrence of search text
        if search_text in text:
            text = text.replace(search_text, f'<a href="{href}">{anchor_text}</a>', 1)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)

insert_link('src/pages/guides/weight-loss-guide.astro', 'calorie deficit', '/guides/calorie-deficit-guide/', 'mathematical calorie deficit')
insert_link('src/pages/guides/calorie-deficit-guide.astro', 'weight loss', '/guides/weight-loss-guide/', 'holistic weight loss principles')
insert_link('src/pages/guides/what-is-bmr.astro', 'Mifflin', '/guides/mifflin-st-jeor-equation/', 'Mifflin-St Jeor equation')
insert_link('src/pages/guides/mifflin-st-jeor-equation.astro', 'other formulas', '/guides/bmr-tdee-formulas-mifflin-harris-benedict/', 'comparing other BMR formulas')
insert_link('src/pages/guides/whats-my-tdee.astro', 'maintenance calories', '/guides/maintenance-calories/', 'maintenance calories')
insert_link('src/pages/guides/maintenance-calories.astro', 'TDEE', '/guides/whats-my-tdee/', 'Total Daily Energy Expenditure (TDEE)')

print("Cannibalization differentiation links applied.")

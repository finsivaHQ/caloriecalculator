with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    text = f.read()

# Update title
text = text.replace(
    'title="Free Calorie Calculator: TDEE, Macros & Weight Loss"',
    'title="Calorie Calculator: Free Calculator for Calories & TDEE"'
)

# Update the intro paragraph
text = text.replace(
    'Calculate your daily energy needs. Uses the Mifflin-St Jeor equation.',
    'Calculate your daily energy needs. Use this free <strong>calculator for calories</strong> to instantly find your ideal maintenance, weight loss, or weight gain targets based on the highly accurate Mifflin-St Jeor equation.'
)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated homepage SEO!')

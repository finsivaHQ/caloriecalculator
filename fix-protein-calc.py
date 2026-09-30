import re

path = 'src/pages/protein-calculator.astro'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update title
content = content.replace(
    'title="Daily Protein Calculator | How Much Protein Do I Need?"',
    'title="Protein Calorie Calculator: How Much Protein Do I Need?"'
)

# Update H1
content = content.replace(
    'h1="Protein Calculator"',
    'h1="Protein Calorie Calculator"'
)

# Update description
content = content.replace(
    'description="Find out how much protein you need to eat every day. Our free protein calculator customizes targets for muscle gain, fat loss, or maintenance."',
    'description="Use our free protein calorie calculator to find out how many grams of protein you need to eat every day for muscle gain, fat loss, or maintenance."'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated protein-calculator.astro")


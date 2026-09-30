import os

path = 'src/pages/protein-calculator.astro'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Create internal links for the MachaRule Spiderweb!
# We want to link to /protein-to-calories-calculator/
if "/protein-to-calories-calculator/" not in text:
    replacements = {
        "grams of protein to calories": "<a href=\"/protein-to-calories-calculator/\" class=\"text-brand hover:underline font-medium\">grams of protein to calories</a>"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    
    # If it wasn't replaced because the phrase isn't there, let's append a link in a paragraph
    if "href=\"/protein-to-calories-calculator/" not in text:
        text = text.replace(
            "</p>\n    </div>\n  </Section>",
            '</p>\n      <p>If you already know exactly how many grams of protein you are eating and simply want to quickly convert those <a href="/protein-to-calories-calculator/" class="text-brand hover:underline font-medium">grams of protein to calories</a>, use our dedicated converter tool.</p>\n    </div>\n  </Section>'
        )

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Linked English Hub to Spokes!")

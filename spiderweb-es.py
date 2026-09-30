import os

path = 'src/pages/country/spain/calculadora-de-calorias.astro'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Create internal links for the MachaRule Spiderweb!
replacements = {
    "efecto térmico de los alimentos": "<a href=\"/country/spain/efecto-termico-de-los-alimentos/\" class=\"text-brand hover:underline font-medium\">efecto térmico de los alimentos</a>",
    "déficit calórico": "<a href=\"/country/spain/que-es-el-deficit-calorico/\" class=\"text-brand hover:underline font-medium\">déficit calórico</a>",
    "superávit calórico": "<a href=\"/country/spain/que-es-el-superavit-calorico/\" class=\"text-brand hover:underline font-medium\">superávit calórico</a>",
    "Tasa Metabólica Basal": "<a href=\"/country/spain/que-es-el-metabolismo-basal/\" class=\"text-brand hover:underline font-medium\">Tasa Metabólica Basal</a>"
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Linked Spanish Hub to Spokes!")

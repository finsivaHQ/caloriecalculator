with open('src/layouts/CalculatorLayout.astro', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('  lang?: string;', '  lang?: string;\n  updated?: string;')
text = text.replace("  lang = 'en',", "  lang = 'en',\n  updated,")
text = text.replace(
    'calculatorSchema(h1, description, path),',
    'calculatorSchema(h1, description, path),\n  ...(updated ? [{ "@context": "https://schema.org", "@type": "SoftwareApplication", "dateModified": updated }] : []),'
)
# Add visual "Last Updated" right under the h1 in the Layout.
text = text.replace(
    '<h1 class="text-3xl font-extrabold tracking-tight text-ink sm:text-4xl">{h1}</h1>',
    '<h1 class="text-3xl font-extrabold tracking-tight text-ink sm:text-4xl">{h1}</h1>\n          {updated && <p class="text-sm font-medium text-mute mt-2">Last Updated: {new Date(updated).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" })}</p>}'
)

with open('src/layouts/CalculatorLayout.astro', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')

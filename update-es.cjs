const fs = require('fs');
let content = fs.readFileSync('src/components/HeaderEs.astro', 'utf8');
content = content.replace(/\{ label: "Gu.*as", href: "\/guides\/" \},?\n?\s*/, '');
fs.writeFileSync('src/components/HeaderEs.astro', content, 'utf8');

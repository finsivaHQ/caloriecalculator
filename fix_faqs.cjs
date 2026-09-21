const fs = require('fs');
let code = fs.readFileSync('src/data/faqs.ts', 'utf8');
const regex = /\/\*\*\s*\n\s*\*\s*questions\.\s*Emitted\s*as\s*FAQPage\s*JSON-LD\s*on\s*\/food-calories-search\/\.\s*\n\s*\*\/\s*\nexport\s*const\s*FOOD_FAQS.*?];/s;
code = code.replace(regex, '');
fs.writeFileSync('src/data/faqs.ts', code, 'utf8');

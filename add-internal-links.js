const fs = require('fs');
const glob = require('glob'); // Not installed, using built-in fs

function replaceInFile(filePath, regex, replacement) {
  let content = fs.readFileSync(filePath, 'utf-8');
  const original = content;
  content = content.replace(regex, replacement);
  if (original !== content) {
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(Updated \);
  }
}

const files = fs.readdirSync('src/pages/guides').filter(f => f.endsWith('.astro')).map(f => 'src/pages/guides/' + f);

files.forEach(file => {
  // Skip the new articles to avoid self-linking
  if (file.includes('thermic-effect') || file.includes('what-is-neat') || file.includes('katch-mcardle') || file.includes('starvation')) return;
  
  // Link TEF
  replaceInFile(file, /\b(Thermic Effect of Food \(TEF\)|thermic effect of food)\b(?!<\/a>)/g, '<a href="/guides/thermic-effect-of-food-tef/" class="text-brand hover:underline font-medium">$&</a>');
  replaceInFile(file, /\bTEF\b(?!<\/a>)(?![^<]*>)/g, '<a href="/guides/thermic-effect-of-food-tef/" class="text-brand hover:underline font-medium">TEF</a>');
  
  // Link NEAT
  replaceInFile(file, /\b(Non-Exercise Activity Thermogenesis \(NEAT\)|non-exercise activity thermogenesis)\b(?!<\/a>)/g, '<a href="/guides/what-is-neat-calories/" class="text-brand hover:underline font-medium">$&</a>');
  replaceInFile(file, /\bNEAT\b(?!<\/a>)(?![^<]*>)/g, '<a href="/guides/what-is-neat-calories/" class="text-brand hover:underline font-medium">NEAT</a>');

  // Link Katch-McArdle
  replaceInFile(file, /\b(Katch-McArdle equation|Katch-McArdle formula|Katch-McArdle)\b(?!<\/a>)(?![^<]*>)/g, '<a href="/guides/katch-mcardle-equation/" class="text-brand hover:underline font-medium">$&</a>');

  // Link Starvation Mode
  replaceInFile(file, /\b(starvation mode|metabolic adaptation)\b(?!<\/a>)(?![^<]*>)/g, '<a href="/guides/starvation-mode-metabolic-adaptation/" class="text-brand hover:underline font-medium">$&</a>');
});

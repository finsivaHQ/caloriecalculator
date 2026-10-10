const fs = require('fs');
const path = require('path');

function processDir(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat.isDirectory()) {
      processDir(fullPath);
    } else if (fullPath.endsWith('.astro') || fullPath.endsWith('.tsx') || fullPath.endsWith('.ts')) {
      let content = fs.readFileSync(fullPath, 'utf8');
      
      // Replace variations of `prose prose-slate` or just `prose` to ensure `dark:prose-invert` is there.
      // But we must be careful not to duplicate dark:prose-invert.
      
      let changed = false;
      
      // Case 1: `prose prose-slate`
      if (content.includes('prose prose-slate') && !content.includes('dark:prose-invert')) {
        content = content.replace(/prose prose-slate/g, 'prose prose-slate dark:prose-invert');
        changed = true;
      }
      
      // Case 2: Some places have just `prose max-w-none` (e.g. about.astro)
      // Make sure we only replace `prose ` if it doesn't already have dark:prose-invert or prose-slate
      if (content.includes('class="prose ') && !content.includes('prose-slate') && !content.includes('dark:prose-invert')) {
        content = content.replace(/class="prose /g, 'class="prose prose-slate dark:prose-invert ');
        changed = true;
      }
      
      // Case 3: `class="prose"` directly
      if (content.includes('class="prose"') && !content.includes('dark:prose-invert')) {
        content = content.replace(/class="prose"/g, 'class="prose prose-slate dark:prose-invert"');
        changed = true;
      }

      if (changed) {
        fs.writeFileSync(fullPath, content, 'utf8');
        console.log(`Updated: ${fullPath}`);
      }
    }
  }
}

processDir(path.join(__dirname, 'src'));
console.log('Done.');
